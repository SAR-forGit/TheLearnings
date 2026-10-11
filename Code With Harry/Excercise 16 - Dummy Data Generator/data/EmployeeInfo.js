const EmployeeInfo =() => {
let FirstName = [
    "hary", "john", "Tony", "Tom", "Peter", "Bruce"
]

let LastName = [
    "Richardson", "Quilss", "Stark", "Dickson",
]

let ProgrammingLanguages = [
    "Javascript", "TypeScript", "Java", "Python", "C++"
]

let Cities = [
    'Ney York',  'New Jersery', 'Chicago', 'Los Angeles', 'Washington'
]

let isManager = [true, false]

return{
    FullName: FirstName[Math.floor(Math.random() * FirstName.length)] + " " + LastName[Math.floor(Math.random() * LastName.length)], 
    Salary: Math.floor(1 + Math.random() * 50)* 1000, 
    ProgrammingLanguage: ProgrammingLanguages[Math.floor(Math.random() * ProgrammingLanguages.length)],
    city: Cities[Math.floor(Math.random() * Cities.length)],
    isManager: isManager[Math.floor(Math.random() * isManager.length)],
}
}

export default EmployeeInfo;