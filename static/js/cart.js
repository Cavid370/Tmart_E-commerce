function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken2 = getCookie('csrftoken');

const addCart = {
    addProductCart(ProductID, Quantity) {
        return fetch('http://localhost:8000/api/basket/', {
            method: 'POST',
            headers: {
                'Content-type': 'application/json',
                'X-CSRFToken': csrftoken2,
                'Authorization': `Bearer ${localStorage.getItem('user-token')}`
            },
            body: JSON.stringify({
                'product': ProductID,
                'quantity': Quantity
            })
        }).then(response => response.json()).then(data => {
            if (data.success) {
                window.alert(data.message);
            }
        })
    }
}

const deleteProduct_Basket = {
    deleteProductBasket(ProductID) {
        return fetch('http://localhost:8000/api/basket/', {
            method: 'DELETE',
            headers: {
                'Content-type': 'application/json',
                'X-CSRFToken': csrftoken2,
                'Authorization': `Bearer ${localStorage.getItem('user-token')}`
            },
            body: JSON.stringify({
                'product': ProductID
            })
        });
    }
}

function functionAddToBasket(ProductID) {
    const quantity = 1;
    addCart.addProductCart(ProductID, quantity);
}

function AddToBasketInDetail(ProductID) {
    const quantity = parseInt(document.getElementById('qty').value);
    addCart.addProductCart(ProductID, quantity);
}


function removeBasket(ProductID) {
    deleteProduct_Basket.deleteProductBasket(ProductID)
}

