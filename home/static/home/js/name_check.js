const profile_button = document.getElementById('profile');
const has_name = document.getElementById('has-name').textContent;
console.log(has_name);
function handleClick(event) {
  if (has_name === 'None') {
    if (event.target !== profile_button) {
      event.preventDefault();
      alert('Click the "N" letter on navbar to set your name!');
    }
  }
}

document.body.addEventListener('click', handleClick);
