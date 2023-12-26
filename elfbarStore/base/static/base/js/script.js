let burgerBtn = document.querySelector('.burger-btn');
let mobileMenu = document.querySelector('.header__mobile-menu')

burgerBtn.addEventListener('click', function() {
    mobileMenu.classList.toggle('open');
    burgerBtn.classList.toggle('open');
})