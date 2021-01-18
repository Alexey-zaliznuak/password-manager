document.addEventListener('click', event => {
    const element = event.target;
    const is_create = element.classList.contains('create_button');
    const UID = document.querySelector('.create_field').id
    
    if (is_create) {
        const service = document.querySelector('.service_input').value
        const email = document.querySelector('.email_input').value
        const password = document.querySelector('.password_input').value
        const double_password = document.querySelector('.password_double_input').value
        
        console.log(service,email,password,double_password,UID)
        if (password == double_password) {
            let promise = fetch(`/create_account?UID=${UID}&service=${service}&email=${email}&password=${password}`)
            alert(promise)
            window.open(`/passwords?UID=${UID}`)
            }
        else {
            alert("Пароли не совпадаю!")
            }
        }
    }
)
function time_update() {
    var hour = new Date().getHours()
    var minute = new Date().getMinutes()

    if (hour < 10) {
        hour = `0${hour}`
    }
    
    if (minute < 10) {
        minute = `0${minute}`
    }

    document.querySelector(".time").innerHTML = `${hour}:${minute}`
    setTimeout(time_update, 1000)
}
time_update()