// Get DOM elements
const plus_button = document.getElementById('plus-button');
const plus_container = document.getElementById('plus-container');

// Handle click events on the plus button
plus_button.addEventListener('click', () => {
    plus_container.classList.toggle('show');
    plus_button.classList.toggle('plus-button-click');
  });
  