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