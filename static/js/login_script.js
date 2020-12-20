document.addEventListener('click', event => {
    const element = event.target;
    const is_req_button = element.classList.contains('request_button');
    if (is_req_button) {
        var name = document.querySelector(".name").value
        var password = document.querySelector(".password").value
        var telephone = document.querySelector(".telephone").value
        
        //let response = fetch(`/main?name=${name}&password=${password}&telephone = ${telephone}`).then(response => response.text()).then(go_to_main_page)
        window.open(`/main?name=${name}&password=${password}&telephone=${telephone}&UID=None`)
        //document.body.children[0].children[0].href = `/main?UID=${UID}`

        }
    }
)

function go_to_main_page(UID) {
    if (UID == "Неверный пароль") {
        alert("Неверный пароль")
    }
    else {
        alert("Успешно")
        window.open(`/main?UID=${UID}`)
    }
}