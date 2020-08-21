document.addEventListener('click', event => {
    const element = event.target;
    const is_icon = element.classList.contains('no-view-icon') ||
                    element.classList.contains('view-icon');
    if (is_icon) {
        element.classList.toggle('no-view-icon');
        element.classList.toggle('view-icon');
        element.parentNode.classList.toggle('secret-text');
    }
});