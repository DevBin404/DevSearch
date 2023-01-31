let tokenUrl = 'http://127.0.0.1:8000/api/users/token/'
let projectPage = 'file:///home/dev/Desktop/frontend%20in%20another%20server/project-list.html'

let form = document.getElementById('login-form')

form.addEventListener('submit', (e) => {
    e.preventDefault()
    
    let formData ={
        'username': form.username.value,
        'password': form.password.value
    }

    fetch(tokenUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData) 
    })

    .then(response => response.json())
    .then(data => {
        
        if (data.access) {
            localStorage.setItem('token', data.access)
            window.location= projectPage
        }
        else{
            alert('Username or password not correct')
        }
    })
} 
)