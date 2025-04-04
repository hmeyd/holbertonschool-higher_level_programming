/* eslint-disable */
document.addEventListener("DOMContentLoaded", function () {
    const add_item = document.getElementById("add_item");
    const myliste = document.querySelector(".my_list");
    
    add_item.addEventListener("click", function () { 
        const NewItem = document.createElement("li");
        NewItem.textContent ="Item";
        myliste.appendChild(NewItem);
    });
});
