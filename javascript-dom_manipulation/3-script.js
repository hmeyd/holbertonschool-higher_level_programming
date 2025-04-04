/* eslint-disable */
document.addEventListener("DOMContentLoaded", function () {
    const ToggleButton = document.getElementById("toggle_header");
    const Header = document.querySelector("header");
    
    ToggleButton.addEventListener("click", function () { 
        if (Header.classList.contains("red")) {
            Header.classList.replace("red", "green");
        } else {
            Header.classList.replace("green", "red");
        }
    });
});
