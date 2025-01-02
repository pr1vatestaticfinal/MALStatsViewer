const username = "username";
const decades = [2010, 2020];
const years = [2013, 2014, 2022];

//when username is received, text is shown
if (username == "username") {
    const welcome = document.querySelector(".welcome");
    welcome.textContent = "Welcome, " + username;
}

if (decades != null) {
    const dropdown = document.getElementById("decades-choices");
    dropdown.innerHTML = "";

    for (let i = 0; i < decades.length; i++) {
        const button = document.createElement("button");
        button.onclick = () => {
            //someFunction(decades[i]); //PLACEHOLDER FUNCTION FIX WHEN COOKIE DATA IS IMPLEMENTED
            dropdown.style.display = "none";
            console.log("you have selected", decades[i]);
        };
        button.textContent = decades[i] + "'s";
        dropdown.appendChild(button);
    }
}

const toggleDecades = document.getElementById("decades-toggle");
const decadesContent = document.getElementById("decades-choices");

toggleDecades.addEventListener("click", () => {
    const isVisible = decadesContent.style.display === "block";
    decadesContent.style.display = isVisible ? "none" : "block";
});

if (years != null) {
    const dropdown = document.getElementById("years-choices");
    dropdown.innerHTML = "";

    for (let i = 0; i < years.length; i++) {
        const button = document.createElement("button");
        button.onclick = () => {
            //someFunction(years[i]); //PLACEHOLDER FUNCTION FIX WHEN COOKIE DATA IS IMPLEMENTED
            dropdown.style.display = "none";
            console.log("you have selected", years[i]);
        };
        button.textContent = years[i];
        dropdown.appendChild(button);
    }
}

const toggleYears = document.getElementById("years-toggle");
const yearsContent = document.getElementById("years-choices");

toggleYears.addEventListener("click", () => {
    const isVisible = yearsContent.style.display === "block";
    yearsContent.style.display = isVisible ? "none" : "block";
    decadesContent.style.display = "none";
});

document.addEventListener("click", (event) => {
    if (!event.target.closest("#timeContainer")) {
        yearsContent.style.display = "none";
        decadesContent.style.display = "none";
    }
});