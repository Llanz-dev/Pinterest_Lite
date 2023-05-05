// Get DOM elements
const plus_button = document.getElementById('plus-button');
// Handle click events on the plus button
plus_button.addEventListener('click', () => {
    plus_button.classList.toggle('plus-button-click');
    var styles_dropdown = window.getComputedStyle(dropdown_container);
    const display_dropdown = styles_dropdown.getPropertyValue('display');
    var styles_plus = window.getComputedStyle(plus_container);
    const display_plus = styles_plus.getPropertyValue('display');
    if (display_plus === 'none' && display_dropdown === 'block') {
        dropdown_container.style.display = 'none';
        plus_container.style.display = 'block';
    } else if (display_plus === 'block' && display_dropdown === 'none') {
        dropdown_container.style.display = 'none';
        plus_container.style.display = 'none';
    } else {
        plus_container.style.display = 'block';

    }
});
  