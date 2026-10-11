import mongoose from "mongoose";

const EmployeeInfoSchema = new mongoose.Schema({
    name: String,
    salary: Number,
    language: String,
    city: String,
    isManager: Boolean
});

export const EmployeeInfoForMongo = mongoose.model('Employee', EmployeeInfoSchema);