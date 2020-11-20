var style_variant = "inline-block"

document.addEventListener('click', event => {
    const element = event.target;
    const is_icon = element.classList.contains('icon')
    const is_search = element.classList.contains('search')
    const is_menu_variant = element.classList.contains('style_toogle')
    
    if (is_icon) {
        element.classList.toggle('no-view-icon');
        element.classList.toggle('view-icon');
        element.classList.toggle('icon_with_padding')
        element.parentNode.classList.toggle('secret-text')
        }

    if (is_search) {
        alert("Фича не сделана отвалите!!!")
    }

    if (is_menu_variant) {
        for (let puk of document.querySelectorAll(".account_card"))
            puk.classList.toggle('card_with_padding')}

   
    }
)