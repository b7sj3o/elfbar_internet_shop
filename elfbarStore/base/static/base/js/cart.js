function decrease(index, price) {
    let inp = document.getElementById(`product-value_${index}`)
    if (inp.value > 1) inp.value--;

    changePrice(index, price)
}

function increase(index, price) {
    let inp = document.getElementById(`product-value_${index}`)
    if (inp.value < 100) inp.value++;

    changePrice(index, price)
}

function changeValue(index, price) {
    let inp = document.getElementById(`product-value_${index}`);
    if (inp.value < 1) {
        inp.value = 1;
    } else if (inp.value > 100) {
        inp.value = 100;
    }

    changePrice(index, price)
}

function changePrice(productId, price) {
    priceInput = document.getElementById(productId);
    let quantity = parseInt(document.getElementById('product-value_' + productId).value);
    priceInput.textContent = (quantity * price).toFixed(2) + 'грн.'

    generalPrice()
    
}

document.addEventListener('DOMContentLoaded', function() {
        let prices = document.querySelectorAll('.cart-product__price');

        prices.forEach(price => {
            let id = price.id
            let pricePerOne = parseFloat(price.textContent);
            let quantity = parseInt(document.getElementById('product-value_' + id).value);
            
            price.textContent = (quantity * pricePerOne).toFixed(2) + 'грн.'
        })
        generalPrice()
    });

function generalPrice() {
    let prices = document.querySelectorAll('.cart-product__price');
    let generalPriceInput = document.querySelector('.cart-product__general')
    let generalPrice = 0;

        prices.forEach(price => {
            generalPrice += parseFloat(price.textContent);
        })
    generalPriceInput.innerHTML = 'Загальна ціна:  <div class="fw-bold" style="margin-left: 5px;">' + generalPrice + ' грн.</div>';
}