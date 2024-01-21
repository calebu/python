terraform {
    required_providers {
      aws = {
        source = "hashicorp/aws"
        version = "~> 4.0.0"
      }
    }
}

variable "db_password" { type= string } 

resource "aws_security_group" "aws_sg" {
  name = "jenkins security group from terraform"

    ingress {
    description = "SSH from the internet"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "Jenkins port"
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

}

data "aws_ami" "amazon-linux-ami" {
  most_recent = true
  owners      = ["amazon"]
  filter {
    name   = "owner-alias"
    values = ["amazon"]
  }


  filter {
    name   = "name"
    values = ["al2023-ami-2023.2.20231018.2-kernel-6.1-x86_64"]
  }

}

resource "aws_instance" "Jenkins-Server" {

  ami                         = data.aws_ami.amazon-linux-ami.id
  instance_type               = "t2.micro"
  vpc_security_group_ids      = [aws_security_group.aws_sg.id]
  associate_public_ip_address = true
  user_data = <<EOF
#!/bin/bash
sudo echo var.db_password > /home/ec2-user/test-smog
sudo yum update –y
sudo wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo
sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io-2023.key
sudo yum upgrade
sudo dnf install java-17-amazon-corretto -y
sudo export JAVA_OPTS="-Djenkins.install.runSetupWizard=false"
yum install jenkins -y
systemctl enable jenkins
systemctl start jenkins
sudo wget http://localhost:8080/jnlpJars/jenkins-cli.jar
jenkins_pass=$(sudo cat /var/lib/jenkins/secrets/initialAdminPassword)
java -jar jenkins-cli.jar -auth admin:$jenkins_pass -s http://localhost:8080 install-plugin configuration-as-code
java -jar jenkins-cli.jar -auth admin:$jenkins_pass -s http://localhost:8080 install-plugin credentials
systemctl stop jenkins

sudo cat <<EOL >> /var/lib/jenkins/jcasc.yaml
jenkins:
  systemMessage: "Jenkins configured automatically by Jenkins Configuration as Code plugin\n\n"
  globalNodeProperties:
  - envVars:
      env:
      - key: VARIABLE1
        value: foo
      - key: VARIABLE2
        value: bar
EOL
sudo chown jenkins:jenkins /var/lib/jenkins/jcasc.yaml
sudo sed -i "s/# Arbitrary additional arguments to pass to Jenkins./Environment=\"JAVA_OPTS=-Djava.awt.headless=true -Djenkins.install.runSetupWizard=false -Dcasc.jenkins.config=\/var\/lib\/jenkins\/jcasc.yaml\"/" /usr/lib/systemd/system/jenkins.service
sudo systemctl daemon-reload
sudo systemctl start jenkins

EOF
  tags = {
    Name = "Jenkins Server"
  }

}

output "jenkins-instance_id" {
  value = aws_instance.Jenkins-Server.id
}
