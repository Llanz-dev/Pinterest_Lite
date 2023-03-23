const plus_button = document.getElementById('plus-button');
const plus_container = document.getElementById('plus-container');

plus_button.onclick = () => {
    plus_container.classList.toggle("show");
    plus_button.classList.toggle("plus-button-click");
}

const whole_content = document.getElementById('whole-content');
const top_nav = document.getElementById('top-nav');
const create_board_button = document.getElementById('create-board-button');
const create_board_container = document.getElementById('create-board-container');
const profile = document.getElementById('profile');
let isOpenedByButton = false;

create_board_button.onclick = () => {
    document.body.style.position = "fixed";
    document.body.style.backgroundColor = "#333333";
    document.body.style.pointerEvents = "none";
    document.body.style.overflowY = "scroll";
    top_nav.style.backgroundColor = "inherit";
    profile.style.backgroundColor = '#333333 !important';
    whole_content.style.filter = "brightness(35%)";
    search_field.style.backgroundColor = '#333333';
    search_icon.style.backgroundColor = '#333333';
    create_board_container.style.display = 'block';
    profile.style.backgroundColor = '#333333';
    isOpenedByButton = true;
  };
  
  function handleClickOutside(event) {
    if (!isOpenedByButton && !create_board_container.contains(event.target)) {
        document.body.style.position = "static";
        document.body.style.backgroundColor = "#FEFEFF";
        document.body.style.pointerEvents = "auto";
        document.body.style.overflowY = "visible";
        top_nav.style.backgroundColor = "#FFFEFE";
        profile.style.backgroundColor = '#eeeeee';
        whole_content.style.filter = "brightness(100%)";
        search_field.style.backgroundColor = '#E9ECEF';
        search_icon.style.backgroundColor = '#E9ECEF';
        create_board_container.style.display = 'none';
    }
    isOpenedByButton = false;
  }
  
  document.addEventListener('click', handleClickOutside);