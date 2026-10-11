import mongoose from "mongoose";

const EmployeeInfo = new mongoose.Schema({
    name: String,
    salary: Number,
    language: String,
    city: String,
    isManager: Boolean
});

export const EmployeeInfoSchema = mongoose.model('Employee', EmployeeInfo);