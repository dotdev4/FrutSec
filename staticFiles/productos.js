import axios from 'axios';

document.addEventListener('DOMContentLoaded', () => {
  // Enviar solicitud AJAX al servidor Flask para obtener los productos de la categoría "semillas"
  axios.get('/productos/semillas')
    .then(response => {
      // Crear una card para cada producto y agregarla al elemento HTML correspondiente
      const productos_semillas = document.querySelector('#productos-semillas');
      response.data.forEach(producto => {
        const card = `
          <div class="card">
            <div class="card-body">
              <h5 class="card-title">${producto.nombre}</h5>
              <p class="card-text">Categoría: ${producto.categoria}</p>
            </div>
          </div>
        `;
        productos_semillas.insertAdjacentHTML('beforeend', card);
      });
    })
    .catch(error => {
      console.error(error);
    });
});