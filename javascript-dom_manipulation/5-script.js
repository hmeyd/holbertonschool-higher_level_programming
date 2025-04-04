/* eslint-disable */
document.addEventListener("DOMContentLoaded", () => {
    
    const UpdatButton = document.getElementById("update_header");
    const Header = document.querySelector("header");
    
    UpdatButton.addEventListener("click", () => {
        Header.textContent = "New Header!!!";
    });
});
