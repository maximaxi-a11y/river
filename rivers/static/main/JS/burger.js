const burgerMenu = document.getElementById('burger-menu');
const navbar = document.getElementById('navbar');

burgerMenu.addEventListener('click', () => {
    navbar.classList.toggle('active');
    burgerMenu.classList.toggle('active');
});

// Close sidebar when clicking outside of it
document.addEventListener('click', (event) => {
    if (!navbar.contains(event.target) && !burgerMenu.contains(event.target)) {
        navbar.classList.remove('active');
        burgerMenu.classList.remove('active');
    }
});