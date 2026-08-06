getFacts = async() => {
    response = await fetch("")
    // console.log(response);
    data = await response.json();
    // console.log(data);
};

getFacts();



