let burgerBtn = document.querySelector('.burger-btn');
let mobileMenu = document.querySelector('.header__mobile-menu')

burgerBtn.addEventListener('click', function() {
    mobileMenu.classList.toggle('open');
    burgerBtn.classList.toggle('open');
})

let addProductBtn = document.getElementById('add-product');
let addProductList = document.getElementById('header__add');
addProductBtn.addEventListener('click', function() {
    addProductList.classList.toggle('open')
})