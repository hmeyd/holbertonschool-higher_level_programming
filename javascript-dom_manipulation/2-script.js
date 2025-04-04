/* eslint-disable */
document.addEventListener("DOMContentLoaded", () => {
    const RedHeader = document.getElementById("red_header");
    const Header = document.querySelector("header");
    
    RedHeader.addEventListener('click', () => { 
        Header.classList.add("red")
    });
});
