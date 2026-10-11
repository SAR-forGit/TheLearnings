const EmployeeInfo = () => {
    const firstName = ['Tom', 'John', 'Peter', 'Sarah', 'Sam', 'Chris', 'Richard'],
    lastName = ['Richardson', 'Quills', 'Parker', 'Rhoades', 'Dickson', 'Hanson'],
    PrgrammingLanguages = ['C++', "C#", 'JavaScript', 'Python', 'Java', 'Ruby', 'GoLang', "Rust"],
    Cities = ['New York', 'New Jersey', 'Chicago', 'Los Angeles', 'Manhattan', "Queens"]
    isManager = [true, false];

    return{
        FullName: firstName[Math.floor(Math.random()*firstName.length)] + " " + lastName[Math.floor(Math.random * lastName.length)],
        Salary: Math.floor(1+Math.random() * 50) * 1000,
        Language: PrgrammingLanguages[Math.floor(Math.random()*PrgrammingLanguages.length)],
        City: Cities[Math.floor(Math.random*Cities.length)],
        isManager: isManager[Math.floor(Math.random*isManager.length)]
    }
}

export default EmployeeInfo;