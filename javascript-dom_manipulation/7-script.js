/* eslint-disable */
document.addEventListener("DOMContentLoaded", () => {
    const apiUrl = "https://swapi-api.hbtn.io/api/films/?format=json";
    const listElement = document.getElementById("list_movies");
  
    fetch(apiUrl)
      .then(response => response.json())
      .then(data => {
        const films = data.results;
        films.forEach(film => {
          const listItem = document.createElement("li");
          listItem.textContent = film.title;
          listElement.appendChild(listItem);
        });
      })
      .catch(error => {
        console.error("Erreur lors de la récupération des films :", error);
      });
  });
  