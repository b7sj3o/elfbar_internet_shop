function decrease(index) {
    let inp = document.getElementById(`product-value_${index}`)
    if (inp.value > 1) inp.value--;

     
}

function increase(index) {
    let inp = document.getElementById(`product-value_${index}`)
    if (inp.value < 100) inp.value++;
    const price = document.getElementById(`product-price_${index}`)
    if (inp.value === '2') {
        price.textContent = '280 грн / шт';
    } else if (inp.value === '3') {
        price.textContent = '270 грн / шт';
    }
}

function changeValue(index) {
    let inp = document.getElementById(`product-value_${index}`);
    if (inp.value < 1) {
        inp.value = 1;
    } else if (inp.value > 100) {
        inp.value = 100;
    }
}


$(document).on('submit', `.addToCart_form`, function(e) {
    e.preventDefault()
    const id = e.target.id.slice(-1)
    $.ajax({
        type: 'POST',
        url: `/create/${id}/`,
        data: {
            image: $(`#product-image_${id}`).val(),
            name: $(`#product-name_${id}`).val(),
            chosen_flavour: $(`#product-flavour_${id}`).val(),
            price: $(`#product-price_${id}`).val(),
            quantity: $(`#product-value_${id}`).val(),
            csrfmiddlewaretoken: $(`input[name=csrfmiddlewaretoken]`).val()
        },
        success: function(data) {
            $(".fixed-cart").addClass("animate");
            $(".fixed-cart-text").addClass("animate");
            $(".fixed-cart-text").html(`= ${data} uah`)
            setTimeout(() => {
                $(".fixed-cart").removeClass("animate");
                $(".fixed-cart-text").removeClass("animate"); 
            }, 1000);
        },
    })
})