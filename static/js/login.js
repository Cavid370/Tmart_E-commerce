let form = document.getElementById("login-form")
form.addEventListener('submit', async function(event) {

    let postData = {
        username: form.username.value,
        password: form.password.value
    }

    let response = await fetch(`http://localhost:8000/api/token/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(postData)
    })
    if (response.ok) {
        let data = await response.json()
        console.log(JSON.stringify(data))
        //alert(JSON.stringify(data))
        localStorage.setItem('user-detail', JSON.stringify(data))
        localStorage.setItem('user-token', data.access)
        //alert(localStorage.getItem('user-token'))  
    }
})