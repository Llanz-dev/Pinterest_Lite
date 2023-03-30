const search_field = document.getElementById('search-field');
const search_icon = document.getElementById('search-icon');

search_field.onclick = () => {
    search_icon.style.display = 'none';
    search_field.style.borderTopLeftRadius = '60px';
    search_field.style.borderBottomLeftRadius = '60px';
    search_field.style.padding = '.6rem 1rem';
    search_field.style.backgroundColor = 'rgb(224, 224, 224)';        
}

search_field.onmouseenter = () => {
    search_field.style.backgroundColor = 'rgb(224, 224, 224)';
    search_icon.style.backgroundColor = 'rgb(224, 224, 224)';
}

search_field.onmouseleave = () => {
    search_field.style.backgroundColor = '#E9ECEF';
    search_icon.style.backgroundColor = '#E9ECEF';
}

document.onclick = () => {
    // Check if the clicked element is inside the target element
    if (!search_field.contains(event.target)) {
        search_icon.style.display = 'flex';
        search_field.style.borderTopLeftRadius = '0';
        search_field.style.borderBottomLeftRadius = '0';
        search_field.style.padding = '.6rem .6rem .6rem 0';
    }
}