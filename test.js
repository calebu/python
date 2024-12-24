type Person = { name: string; age: number; premeum?: boolean }; // Define the type
let myObj = { name: "Riyad", age: 22 }; // Assign myObj
const alAmin: Person = { name: "Jobayer", age: 26, premeum: true }; // Another object
let jobayer: Person = alAmin, sadik: Person = { name: "Sadik", age: 24 }; // Two objects in one line
const greetPerson = (personObj: Person): string => `Hello ${personObj.name}`; // Greet function
const personIsPremium = (personObj: Person): string => `${personObj.name}${personObj.premeum ?? ""}`; // Handle possible undefined
