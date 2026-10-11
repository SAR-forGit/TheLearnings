import mongoose from "mongoose";
import express from "express";
import EmployeeInfo from "./data/EmployeeInfo.js";
import { EmployeeInfoSchema } from "./view/EmployeeInfoSchema.js";

const app = express();
let conn = await mongoose.connect("/mongodb://localhost:27017/EmployeeDetails")
    .then(() => console.log("MongoDB Connected Succesfully"))
    .catch((error) => console.error('MongoDB connection error: ', error))

app.use(express.static("public"));

app.post('/generate', async (req, res) => {
    try {
        const EmployeeInformation = new EmployeeInfoSchema({
            name: EmployeeInfo().FullName,
            salary: EmployeeInfo().Salary,
            language: EmployeeInfo().Language,
            city: EmployeeInfo().City,
            isManager: EmployeeInfo().isManager
        })
        await EmployeeInformation.save();
    }
    catch (error){
        console.log(error);
     }
})

app.listen(3000, () => {
    console.log(`Example app listening on port ${3000}`);
});
