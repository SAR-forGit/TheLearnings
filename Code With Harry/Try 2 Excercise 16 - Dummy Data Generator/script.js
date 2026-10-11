const button = document.getElementById("GenerateButton");
const EmployeeShowArea = document.getElementById("EmployeeInfo");

button.addEventListener("click", async() => {
    const response = await fetch("/generate", {method: "POST"});
    const data = await response.json();

    EmployeeShowArea.innerHTML = `
    <h2>${data.employee.name}</h2>
    <p>salary: ${data.employee.salary}</P>
    <p>language: ${data.employee.city}</P>
    <p>city: ${data.employee.isManager}</P>
    <p>isManager: ${data.employee.language}</P>
    `
})