import fs from "fs/promises"
import fsn from "fs"
import path from "path"

const basepath = "C:\\Users\\sarfo\\Desktop\\Days Or Dies\\Exercise 15";

let files = await fs.readdir(basepath);

for (const item of files){
    // console.log("running for ", item);
    
    let extension = item.split(".")[item.split(".").length - 1];
    if(extension != "js" && extension != "json" && item.split(".").length > 1){
        if(fsn.existsSync(path.join(basepath, extension))){
            fs.rename(path.join(basepath, item), path.join(basepath, extension, item))
        }
        else{
            fs.mkdir(extension);
            fs.rename(path.join(basepath, item), path.join(basepath, extension, item))
        }
        console.log(item);
    }
}