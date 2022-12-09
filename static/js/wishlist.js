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
const csrftoken = getCookie('csrftoken');

const addProduct = {
    addProductWishlist(ProductID) {
        return fetch('http://localhost:8000/api/wishlist/', {
            method: 'POST',
            headers: {
                'Content-type': 'application/json',
                'X-CSRFToken': csrftoken,     
                'Authorization': `Bearer ${localStorage.getItem('user-token')}`
            },
            body: JSON.stringify({
                'product': ProductID
            })
        }).then(response => response.json()).then(data => {
            if (data.success) {
                window.alert(data.message);
            }
        })
    }
}

const deleteProduct = {
    deleteProductWishlist(ProductID) {
        return fetch('http://localhost:8000/api/wishlist/', {
            method: 'DELETE',
            headers: {
                'Content-type': 'application/json',
                'X-CSRFToken': csrftoken,
                'Authorization': `Bearer ${localStorage.getItem('user-token')}`
            },
            body: JSON.stringify({
                'product': ProductID
            })
        });
    }
}
function functionAddToWishlist(ProductID) {
    addProduct.addProductWishlist(ProductID);
}
function removeWishlist(ProductID) {
    deleteProduct.deleteProductWishlist(ProductID)
}