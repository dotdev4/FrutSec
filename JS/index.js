// CARROUSEL

// Variables
const carousel = document.querySelector('.carousel');
const carouselItems = document.querySelector('.carousel-inner');
let isDragging = false;
let startPosition = 0;
let currentTranslate = 0;
let prevTranslate = 0;
let animationID = 0;
let currentPosition;

// Capturar el evento de arrastre
carousel.addEventListener('mousedown', dragStart);
carousel.addEventListener('touchstart', dragStart);
carousel.addEventListener('mouseup', dragEnd);
carousel.addEventListener('touchend', dragEnd);
carousel.addEventListener('mousemove', drag);
carousel.addEventListener('touchmove', drag);

// Funciones
function dragStart(e){
    e.type === 'touchstart' ? startPosition = e.touches[0].clientX :
    startPosition = e.clientX;
    isDragging = true;
    animationId = requestAnimationFrame(animation);
}

function drag(e){
    if(isDragging){
        e.type === 'touchmove' ? currentPosition = e.touches[0].clientX :
        currentPosition = e.clientX;
    } else {
        currentTranslate = prevTranslate + currentPosition - startPosition;
    }
}

function dragEnd(){
    cancelAnimationFrame(animationId);
    isDragging = false;
    prevTranslate = currentTranslate;
}

function animation(){
    carouselItems.style.transform = `translateX(${currentTranslate}px)`;
    if(isDragging) requestAnimationFrame(animation);
}