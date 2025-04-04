/* eslint-disable */
document.addEventListener("DOMContentLoaded", () => {
    // URL de l'API
    const apiUrl = "https://swapi-api.hbtn.io/api/people/5/?format=json";
  
    // Récupération de l'élément HTML
    const characterDiv = document.getElementById("character");
  
    // Appel à l'API avec Fetch
    fetch(apiUrl)
      .then(response => response.json()) // convertir la réponse en JSON
      .then(data => {
        characterDiv.textContent = data.name; // insérer le nom dans la div
      })
      .catch(error => {
        console.error("Erreur lors de la récupération du personnage :", error);
        characterDiv.textContent = "Erreur de chargement";
      });
  });
  