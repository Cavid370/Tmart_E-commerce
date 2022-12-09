var subscription_form = document.getElementById('subscription-form');

subscription_form.addEventListener('submit', function (event) {
    event.preventDefault();
    let email = document.getElementById('subscription-email');
    console.log(email.value);
    const data = { email: email.value };
    fetch('http://localhost:8000/api/subscribe/', {
        method: 'POST', // or 'PUT'
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
        .then((response) => {
            if(response.ok){
                alert('Successfully subscribed')
            }else{
                alert("Error!")
            }
        })
        .then((data) => {
            console.log('Success:', data);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
});
