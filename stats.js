const link = pyodide.globals.get("req");
var username = "Zach Hill";
var decades = 2;
var decadeStartYear = 2010;
const years = [2010, 2013, 2022];
const welcome = document.getElementsByClassName("welcome")
                
document.getElementById("dynamic-link").href = link;
    
if (username !== "") {
    for (let i = 0; i < welcome.length; i++) {
        welcome[i].style.display = "block";
    
        }
    }
else {
    for (let i = 0; i < welcome.length; i++) {
        welcome[i].style.display = "none";
        }
    }
    
function welcomeText() {
    document.getElementById("welcomeText").innerHTML = username;
    
    }
//generates buttons to display data in decades  
buttonContainer = document.getElementById("decadesContainer");
    
if (decades !== 0) {
    for (let i = 0; i < decades; i++) {
        let buttonLabel = String(decadeStartYear) + "'s";
        const button = document.createElement("button");
        button.textContent = buttonLabel;
        //button.addEventListener("click",  summonYears);
        buttonContainer.appendChild(button);
        decadeStartYear = decadeStartYear + 10;
        }
    }
    
/*function summonYears() {
    let container = {}
    for (let i = 0; i < years.length; i++) {
        let buttonLabel = String(years[i])
        if (years[i]) {
            const button = document.createElement("button");
            button.textContent = buttonLabel;
            //button.addEventListener("click", placeHolder)
            container.appendChild(button);
            }
    
    document.getElementById("yearsContainer").innerHTML = container
    
    }*/