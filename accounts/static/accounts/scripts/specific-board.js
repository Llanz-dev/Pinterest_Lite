const for_mobile_container = document.getElementById('for-mobile-container');
const for_mobile_button = document.getElementById('for-mobile-button');
const delete_board_button = document.getElementById('delete-board-button');
const delete_board_container = document.getElementById('delete-board-container');
const cancel_btn = document.getElementById('cancel-btn');
const whole_content = document.getElementById('whole-content');
const top_nav = document.getElementById('top-nav');
const profile = document.getElementById('profile');

// Keep track of whether the "delete board" container was opened by a button click
let isOpenedByButton = false;

// Handle click events on the plus button
for_mobile_button.addEventListener('click', () => {
    for_mobile_container.classList.toggle('show-mobile-container');
    for_mobile_button.classList.toggle('plus-button-click');
  });

  // Handle click events on the delete board button
delete_board_button.addEventListener('click', () => {
  // Set the body styles to disable scrolling and darken the background
  document.body.style.position = 'fixed';
  document.body.style.top = '0';
  document.body.style.bottom = '0';
  document.body.style.height = '100%';
  document.body.style.width = '100%';
  document.body.style.backgroundColor = '#333333';
  document.body.style.pointerEvents = 'none';
  document.body.style.overflowY = 'scroll';

  // Set the top navigation and search bar styles to match the dark background
  top_nav.style.backgroundColor = 'inherit';
  search_field.style.backgroundColor = '#333333';
  search_icon.style.backgroundColor = '#333333';

  // Set the profile icon to match the dark background
  profile.style.backgroundColor = '#333333';
  profile.style.filter = 'brightness(35%)';

  // Show the delete board container and darken the rest of the page
  delete_board_container.style.display = 'block';
  whole_content.style.filter = 'brightness(35%)';

  // Remember that the container was opened by a button click
  isOpenedByButton = true;
});

// Handle click events outside the delete board container
function handleClickOutside(event) {

  if (!isOpenedByButton && !delete_board_container.contains(event.target)) {
    // Reset the body styles to re-enable scrolling and restore the background
    document.body.style.position = 'static';
    document.body.style.backgroundColor = '#FEFEFF';
    document.body.style.pointerEvents = 'auto';
    document.body.style.overflowY = 'visible';

    // Reset the top navigation and search bar styles to match the light background
    top_nav.style.backgroundColor = '#FFFEFE';
    search_field.style.backgroundColor = '#E9ECEF';
    search_icon.style.backgroundColor = '#E9ECEF';

    // Hide the delete board container and restore the rest of the page
    delete_board_container.style.display = 'none';
    whole_content.style.filter = 'brightness(100%)';

    // Reset the profile icon to match the light background
    profile.style.backgroundColor = '#eeeeee';
    profile.style.filter = 'brightness(100%)';
  }

  // Reset the flag that indicates whether the container was opened by a button click
  isOpenedByButton = false;
}

// Add a click event listener to the document to handle clicks outside the container
document.addEventListener('click', handleClickOutside);
cancel_btn.addEventListener('click', (event) => {
      event.preventDefault();
      // Reset the body styles to re-enable scrolling and restore the background
      document.body.style.position = 'static';
      document.body.style.backgroundColor = '#FEFEFF';
      document.body.style.pointerEvents = 'auto';
      document.body.style.overflowY = 'visible';
  
      // Reset the top navigation and search bar styles to match the light background
      top_nav.style.backgroundColor = '#FFFEFE';
      search_field.style.backgroundColor = '#E9ECEF';
      search_icon.style.backgroundColor = '#E9ECEF';
  
      // Hide the delete board container and restore the rest of the page
      delete_board_container.style.display = 'none';
      whole_content.style.filter = 'brightness(100%)';
  
      // Reset the profile icon to match the light background
      profile.style.backgroundColor = '#eeeeee';
      profile.style.filter = 'brightness(100%)';
});
