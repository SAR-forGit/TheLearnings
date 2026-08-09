videoHeader  = "something"
function CreateCard(Thumbnail, videoHeader, Duration, Views, ChannelName, uploadDate){

    if (Views > 999 && Views < 1000000  ){
        Views = Math.floor(Views/1000) + "k";
    } 
    else if (Views > 999999 && Views < 1000000000){
        Views = Math.floor(Views / 1000000) + "M"
    }
    else if (Views > 999999999) {
        Views = (Math.floor(Views / 1000000000) + "B")
    }

    
    html = `<div class="card">
    <div id="thumbnail">
        <img src="${Thumbnail}" alt="Thumbnail">
        <p class="DurationCapsule">${Duration}</p>
        </div>
    
        <div id="TextContent">
        <h1 id="videoHeader">${videoHeader}</h1>
            <div id="OtherInfo">
            <p id="ChannelName">${ChannelName}</p>
            <p> • </p>
            <p id="">${Views}</p>
            <p> • </p>
            <p id="">${uploadDate}</p>
            </div></div>`
            
    document.querySelector(".cardSection").innerHTML = document.querySelector(".cardSection").innerHTML + html;
}

CreateCard("", "Cyberpunk 2077 ", "21:36", 9999999999, "SARs Officialis", "20 Dec 2026");
CreateCard("", "Nigga tryna eat me", "44:50", 1000000, "Code With Harry", "21 Nov 2026");
CreateCard("", "Google Pixel 11 Pro Sucks", "12:5", 9999999999, "SARs Tech Officialis", "26 July 2026")