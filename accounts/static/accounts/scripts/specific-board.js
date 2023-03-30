for_mobile = document.getElementById('for-mobile');
for_mobile_button = document.getElementById('for-mobile-button');

// Handle click events on the plus button
for_mobile_button.addEventListener('click', () => {
    for_mobile.classList.toggle('show');
  });