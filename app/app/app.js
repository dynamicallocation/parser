const Creatuser = document.querySelector('.CreateUser').addEventListener('submit', e => {
    e.preventDefault()
    const username = CreateUser.querySelector('.username').value
    const password = CreateUser.querySelector('.password').value 
    post('/createUser',{username,password})
})

function post(path,data) {

    return window.fetch(path,{
        method: 'POST',
        header: {
            'ACCEPT': 'applicatoin/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
}

