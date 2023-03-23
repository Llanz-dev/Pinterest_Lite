// Get DOM elements
const plus_button = document.getElementById('plus-button');
const plus_container = document.getElementById('plus-container');
const whole_content = document.getElementById('whole-content');
const top_nav = document.getElementById('top-nav');
const create_board_button = document.getElementById('create-board-button');
const create_board_container = document.getElementById('create-board-container');
const profile = document.getElementById('profile');

// Keep track of whether the "create board" container was opened by a button click
let isOpenedByButton = false;

// Handle click events on the plus button
plus_button.addEventListener('click', () => {
  plus_container.classList.toggle('show');
  plus_button.classList.toggle('plus-button-click');
});

// Handle click events on the create board button
create_board_button.addEventListener('click', () => {
  // Set the body styles to disable scrolling and darken the background
  document.body.style.position = 'fixed';
  document.body.style.backgroundColor = '#333333';
  document.body.style.pointerEvents = 'none';
  document.body.style.overflowY = 'scroll';

  // Set the top navigation and search bar styles to match the dark background
  top_nav.style.backgroundColor = 'inherit';
  search_field.style.backgroundColor = '#333333';
  search_icon.style.backgroundColor = '#333333';

  // Show the create board container and darken the rest of the page
  create_board_container.style.display = 'block';
  whole_content.style.filter = 'brightness(35%)';

  // Set the profile icon to match the dark background
  profile.style.backgroundColor = '#333333';

  // Remember that the container was opened by a button click
  isOpenedByButton = true;
});

// Handle click events outside the create board container
function handleClickOutside(event) {
  if (!isOpenedByButton && !create_board_container.contains(event.target)) {
    // Reset the body styles to re-enable scrolling and restore the background
    document.body.style.position = 'static';
    document.body.style.backgroundColor = '#FEFEFF';
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
  }

  // Reset the flag that indicates whether the container was opened by a button click
  isOpenedByButton = false;
}

// Add a click event listener to the document to handle clicks outside the container
document.addEventListener('click', handleClickOutside);
