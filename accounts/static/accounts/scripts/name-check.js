const edit_profile_button = document.getElementById('edit-profile-btn');
const has_name = document.getElementById('has-name').textContent;

function handleClick(event) {
  if (has_name === 'None') {
    if (event.target !== edit_profile_button) {
        event.preventDefault();
        alert('Click the "Edit Profile" button');
    }
  }
}

document.body.addEventListener('click', handleClick);
