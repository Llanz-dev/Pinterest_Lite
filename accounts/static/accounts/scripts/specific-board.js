const for_mobile_container = document.getElementById('for-mobile-container');
const for_mobile_button = document.getElementById('for-mobile-button');

// Handle click events on the plus button
for_mobile_button.addEventListener('click', () => {
    for_mobile_container.classList.toggle('show-mobile-container');
    for_mobile_button.classList.toggle('plus-button-click');
  });
