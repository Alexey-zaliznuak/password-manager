document.addEventListener('click', event => {
    const element = event.target;
    const is_delete = element.classList.contains('delete');
    var url_active = false
    if (is_delete & !url_active) {
        url_active = true
        var UID = document.body.children[0].id
        var _id = document.body.children[0].children[0].children[0].id
        var request = new XMLHttpRequest();

        request.open("GET", `/del_account?id=${_id}&UID=${UID}`)
        request.send();
        
        document.body.children[0].children[0].href = `/main?UID=${UID}`

        }
    }
)