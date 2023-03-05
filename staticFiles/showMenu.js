// desplegar menu en mobile
const menuIconMobile = document.querySelector('.menu-icon-mobile');
const menuDesplegable = document.querySelector('#menu-desplegable');


// cuando se hace click en el icono del menu, se despliega el menu
menuIconMobile.addEventListener('click', () =>{
    menuDesplegable.classList.toggle('visible');

    // animacion para girar el icono del menu
    menuIconMobile.classList.toggle('rotate');
});

// cuando se hace click en cualquier parte de la pagina, se oculta el menu
document.addEventListener('click', (event) => {
    

    if (!menuDesplegable.contains(event.target) && !menuIconMobile.contains(event.target)) {
      // oculta el menu
      menuDesplegable.classList.remove('visible');
  
      // gira el icono del menu a la posición original
      menuIconMobile.classList.remove('rotate');
      
      // agrega la clase para la animación de rotación inversa
      menuIconMobile.classList.add('rotate-back');
      
      // elimina la clase de rotación después de que se haya completado la animación
      setTimeout(() => {
        menuIconMobile.classList.remove('rotate-back');
      }, 500);
    }
  });