document.addEventListener('click', event => {
    const element = event.target;
    const is_req_button = element.classList.contains('request_button');
    if (is_req_button) {
        var name = document.querySelector(".name").value
        var password = document.querySelector(".password").value

        let response = fetch(`/get_user_UID?name=${name}&password=${password}`).then(response => response.text()).then(go_to_main_page)
        
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