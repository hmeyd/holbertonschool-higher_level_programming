/* eslint-disable */
document.addEventListener("DOMContentLoaded", () => {
    const url = "https://hellosalut.stefanbohacek.dev/?lang=fr";
  
    fetch(url)
      .then(response => response.json())
      .then(data => {
        document.getElementById("hello").textContent = data.hello;
      })
      .catch(error => {
        console.error("Erreur lors du fetch :", error);
      });
  });
  