
let slides = document.querySelector('.slides');
let index = 0;
const totalSlides = slides.children.length;

// Function to update slide
function updateSlide() {
    slides.style.transform = `translateX(-${index * 100}%)`;
}

// Auto slide every 3 seconds
let autoSlide = setInterval(() => {
    index = (index + 1) % totalSlides;
    updateSlide();
}, 2000);

// Previous & Next buttons
document.querySelector('.prev').addEventListener('click', () => {
    index = (index - 1 + totalSlides) % totalSlides;
    updateSlide();
    resetInterval();
});

document.querySelector('.next').addEventListener('click', () => {
    index = (index + 1) % totalSlides;
    updateSlide();
    resetInterval();
});

// Reset interval after manual navigation
function resetInterval() {
    clearInterval(autoSlide);
    autoSlide = setInterval(() => {
        index = (index + 1) % totalSlides;
        updateSlide();
    }, 3000);
}

