import mongoose, { mongo } from 'mongoose';
import express from 'express';
import EmployeeInfo from './data/EmployeeInfo.js';
import { EmployeeInfoForMongo } from './models/EmployeeModelSchema.js';

let conn = await mongoose.connect("mongodb://localhost:27017/")
    .then(() => console.log("Connected Succesfully"))
    .catch((err => console.error('❌ MongoDB connection error:', err)));

const app = express();

app.use(express.static("public"));

app.post("/generate", async (req, res) => {
    try {
        const EmployeeInformation = new EmployeeInfoForMongo({
            name: EmployeeInfo().FullName,
            salary: EmployeeInfo().Salary,
            language: EmployeeInfo().ProgrammingLanguage,
            city: EmployeeInfo().city,
            isManager: EmployeeInfo().isManager
        })
        await EmployeeInformation.save();
    }
    catch (error) {
        console.log(error);
        res.status(500).json({
            message: "Failed to add employee"
        });
    }
})

app.listen(3000, () => {
    console.log(`Example app listening on port ${3000}`);
});