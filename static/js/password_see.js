document.addEventListener('click', event => {
    const element = event.target;
    var UID = document.querySelector(".UID").getAttribute("UID")
    var ID = document.querySelector(".UID").getAttribute("ID")
    
    const is_exit = element.classList.contains('out') || element.classList.contains('out_card')
    const is_del = element.classList.contains('delete_card') || element.classList.contains('delete')
    
    const is_icon_view = element.classList.contains('icon')
    const is_copy_icon = element.classList.contains('copy')  
    
    if (is_icon_view) {
        element.classList.toggle('no-view-icon');
        element.classList.toggle('view-icon');
        element.parentNode.classList.toggle('secret-text')
    }
    
    if (is_copy_icon) {
        var data = element.parentNode.parentNode.children[2].children[0].innerHTML
        navigator.clipboard.writeText(data)
        alert("Скопировано!")
    }   
    
    if (is_del) {
        if (confirm("Вы действительно хотите удалить аккаунт?")) {
            let promise = fetch(`/del_account?UID=${UID}&ID=${ID}`)
            window.open(`/passwords?UID=${UID}`)
        }
    }

    if (is_exit) {
        window.open(`/passwords?UID=${UID}`)
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