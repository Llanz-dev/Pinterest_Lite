const search_field = document.getElementById('search-field');
const search_icon = document.getElementById('search-icon');
const arrow_down_button = document.getElementById('arrow-down-button');

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

is_arrow_clicked = true;

const plus_container = document.getElementById('plus-container');
const dropdown_container = document.getElementById('dropdown-container');
const file_name = document.getElementById('file-name');

arrow_down_button.onclick = () => {
    // This if statement function is only for Profile page.
    if (file_name !== null && file_name.textContent === 'profile') {
        var styles_dropdown = window.getComputedStyle(dropdown_container)
        const display_dropdown = styles_dropdown.getPropertyValue('display');  
        var styles_button = window.getComputedStyle(plus_container);
        const display_plus = styles_button.getPropertyValue('display'); 
        if (display_plus === 'block' && display_dropdown === 'none') {
            dropdown_container.style.display = 'block';
            plus_container.style.display = 'none';
            plus_button.classList.remove('plus-button-click');            
        } else if (display_plus === 'none' && display_dropdown === 'block') {
            dropdown_container.style.display = 'none';
            plus_container.style.display = 'none';
            plus_button.classList.remove('plus-button-click');            
        } else {
            dropdown_container.style.display = 'block';
        }
    } else {
        var styles_dropdown = window.getComputedStyle(dropdown_container)
        const display_dropdown = styles_dropdown.getPropertyValue('display');  
        if (display_dropdown === 'none') {
            dropdown_container.style.display = 'block';
        } else {
            dropdown_container.style.display = 'none';
        }
    }

   

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