// Get DOM elements
const whole_content = document.getElementById('whole-content');
const top_nav = document.getElementById('top-nav');
const create_board_button = document.getElementById('create-board-button');
const create_board_container = document.getElementById('create-board-container');
const pinterest_logo = document.getElementById('pinterest-logo');
const profile = document.getElementById('profile');
const is_pin_builder = document.getElementById('is-pin-builder');

// Keep track of whether the "create board" container was opened by a button click
let isOpenedByButton = false;
const is_board_available = document.getElementById('is-board-available');
if (is_board_available !== null) {
  // Handle click events on the create board button
  create_board_button.addEventListener('click', () => {
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

  // Show the create board container and darken the rest of the page
  create_board_container.style.display = 'block';
  whole_content.style.filter = 'brightness(35%)';

  // Set the pinterest logo to match the dark background
  pinterest_logo.style.filter = 'brightness(35%)';

  // Remember that the container was opened by a button click
  isOpenedByButton = true;
});
}


// Handle click events outside the create board container
function handleClickOutside(event) {
  if (!isOpenedByButton && !create_board_container.contains(event.target)) {
    // Reset the body styles to re-enable scrolling and restore the background
    document.body.style.position = 'static';
    // If pin builder file then change to its own color background.
    if (is_pin_builder === null) {
      document.body.style.backgroundColor = '#FEFEFF';
    } else {
      document.body.style.backgroundColor = '#E8E8E9';
    }
    document.body.style.pointerEvents = 'auto';
    document.body.style.overflowY = 'visible';

    // Reset the top navigation and search bar styles to match the light background
    top_nav.style.backgroundColor = '#FFFEFE';
    search_field.style.backgroundColor = '#E9ECEF';
    search_icon.style.backgroundColor = '#E9ECEF';

    // Hide the create board container and restore the rest of the page
    create_board_container.style.display = 'none';
    whole_content.style.filter = 'brightness(100%)';

    // Reset the profile icon to match the light background
    profile.style.backgroundColor = '#eeeeee';
    profile.style.filter = 'brightness(100%)';

    // Reset the pinterest icon to match the light background
    pinterest_logo.style.filter = 'brightness(100%)';      
  }

  // Reset the flag that indicates whether the container was opened by a button click
  isOpenedByButton = false;
}

// Add a click event listener to the document to handle clicks outside the container
document.addEventListener('click', handleClickOutside);
