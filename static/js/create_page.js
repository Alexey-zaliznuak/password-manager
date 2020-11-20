document.addEventListener('click', event => {
    const element = event.target;
    const is_delete = element.classList.contains('create_button');

    if (is_delete) {
        const service = document.body.children[0].children[0].children[1].value
        const email = document.body.children[0].children[1].children[1].value
        const password = document.body.children[0].children[2].children[1].value
        const double_password = document.body.children[0].children[3].children[1].value
        const UID = document.body.children[0].id
        
        console.log(service,email,password,double_password,UID)
        if (password == double_password) {
            var request = new XMLHttpRequest();
            request.open("POST", `/create_account?UID=${UID}&service=${service}&email=${email}&password=${password}`)
            request.send();
            alert("Успешно")
            }
        else {
            alert("Пароли не совпадаю!")
        }
        
        }
    }
)