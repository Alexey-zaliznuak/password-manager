document.addEventListener('click', event => {
    const element = event.target;
    const is_req_button = element.classList.contains('request_button');

    if (is_req_button) {
        var name = document.querySelector(".name").value
        var password = document.querySelector(".password").value
        var telephone = document.querySelector(".telephone").value
        
        registartion_promice(name, password, telephone)
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

async function registartion_promice(name, password, telephone) {
    let promise = await fetch(`/registration_permission?name=${name}&password=${password}&telephone=${telephone}&UID=None&create=0`)
    promise = await promise.text()

    if (promise != "Успешно") {
        alert(promise) 
    }
    else {
        window.open(`/passwords?name=${name}&password=${password}&telephone=${telephone}&UID=None&create=0`)
    }
}

time_update()