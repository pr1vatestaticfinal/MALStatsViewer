import { getUsername } from "./get_username.mjs";

const username = getUsername();
const decades = [];
const years = [2013, 2014, 2022];
const numOfAnimes = 5

//when username is received, text is shown
if (username == "username") {
    const welcome = document.querySelector(".welcome");
    welcome.textContent = "Welcome, " + username;
}

getDecades(years);

//exactly what it sounds like
function getDecades(year) {
    for (let i = 0; i < year.length; i++) {
        if (2000 <= year[i] && year[i] < 2010 && !decades.includes(2000)) {
            decades.push(2000);
        }
        else if (2010 <= year[i] && year[i] < 2020 && !decades.includes(2010)) {
            decades.push(2010);
        }
        else if (2020 <= year[i] && year[i] < 2030 && !decades.includes(2020)) {
            decades.push(2020);
        }
    }
}

//checks if dropdown menu needs to be updated
if (decades != null) {
    const dropdown = document.getElementById("decades-choices");
    dropdown.innerHTML = "";
    
    //creates dropdown menu options
    for (let i = 0; i < decades.length; i++) {
        const button = document.createElement("button");
        button.onclick = () => {
            decadeChosen(decades[i]);
            dropdown.style.display = "none";
            console.log("you have selected", decades[i]);
        };
        button.textContent = decades[i] + "'s";
        dropdown.appendChild(button);
    }
}

const toggleDecades = document.getElementById("decades-toggle");
const decadesContent = document.getElementById("decades-choices");

//shows options when decades button is clicked
toggleDecades.addEventListener("click", () => {
    const isVisible = decadesContent.style.display === "block";
    decadesContent.style.display = isVisible ? "none" : "block";
});

//checks if years dropdown menu needs to be updated
if (years != null) {
    const dropdown = document.getElementById("years-choices");
    dropdown.innerHTML = "";

    //adds menu options in years
    for (let i = 0; i < years.length; i++) {
        const button = document.createElement("button");
        button.onclick = () => {
            yearChosen(years[i]);
            dropdown.style.display = "none";
            console.log("you have selected", years[i]);
        };
        button.textContent = years[i];
        dropdown.appendChild(button);
    }
}

const toggleYears = document.getElementById("years-toggle");
const yearsContent = document.getElementById("years-choices");

//displays options when years button is clicked
toggleYears.addEventListener("click", () => {
    const isVisible = yearsContent.style.display === "block";
    yearsContent.style.display = isVisible ? "none" : "block";
    decadesContent.style.display = "none";
});

//hides menu options when site is clicked on
document.addEventListener("click", (event) => {
    if (!event.target.closest("#timeContainer")) {
        yearsContent.style.display = "none";
        decadesContent.style.display = "none";
    }
});

const toggleAllTime = document.getElementById("alltime-toggle");
toggleAllTime.onclick = () => {allTimeChosen()};

//REMEMBER TO STORE UPDATED NUMOFANIMES IN ANOTHER VAR WHEN DATA IS IMPLEMENTED
function decadeChosen(decade) {
    var added = document.querySelector(".added");
    added.textContent = "You have added " + numOfAnimes + " entries during the " + decade + "'s";
}

function yearChosen(year) {
    var added = document.querySelector(".added");
    added.textContent = "You have added " + numOfAnimes + " entries in " + year;
}

function allTimeChosen() {
    var added = document.querySelector(".added");
    added.textContent = "You have added " + numOfAnimes + " entries in total";
}