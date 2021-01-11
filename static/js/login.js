document.addEventListener('click', event => {
    const element = event.target;
    const is_req_button = element.classList.contains('request_button');

    if (is_req_button) {
        var name = document.querySelector(".name").value
        var password = document.querySelector(".password").value
        var telephone = document.querySelector(".telephone").value
        

        var promise = fetch(`/find_account?name=${name}&password=${password}&telephone=${telephone}&UID=None&create=0`)

        //        text = password_promice(name, password, telephone).then
        console.log(promise)
        if (text == "Успешно") {
            window.open(`/find_account?name=${name}&password=${password}&telephone=${telephone}&UID=None&create=0`)
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

async function password_promice(name, password, telephone) {
    let promise = await fetch(`/find_account?name=${name}&password=${password}&telephone=${telephone}&UID=None&create=0`)
    promise = await promise.text()

    if (promise != "Успешно") {
        alert(promise) 
    }
    else {
        return Promise.resolve(promise)
    }
}

time_update()