document.addEventListener('click', event => {
    const element = event.target;

    const is_icon_view = element.classList.contains('icon')
    const is_copy_icon = element.classList.contains('copy')  
    const is_del_card = element.classList.contains('delete_card')
                     || element.classList.contains('delete')
    
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
    
    // if (is_del_card) {
    //     if (confirm("Choose Yes or Not")) {
    //         var variable = document.body.children[0].id
    //         var request = new XMLHttpRequest();

    //         request.open("POST", `/del?id=${variable}`)
    //         request.send();
    //         }
    //     }   
    }        
)
