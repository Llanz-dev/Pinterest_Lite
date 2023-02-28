const is_user_logged_in = document.getElementById('is-user-logged-in').textContent;

if (is_user_logged_in === 'AnonymousUser') {
    // For Register and Log in.
    const log_in = document.getElementsByClassName('log-in');
    const sign_up = document.getElementsByClassName('sign-up');
    const login_container = document.getElementById('login-container');
    const signup_container = document.getElementById('signup-container');
    const modal = document.getElementById('modal');
    const weeknight_dinner = document.getElementById('weeknight-dinner');
    const login_close_button = document.getElementById('login-close-button');
    const signup_close_button = document.getElementById('signup-close-button');
    console.log('Not user logged in', is_user_logged_in);
    let form = null;
    log_in[0].onclick = () => {
        form = 'log-in';
        form_display(form, 35);
    }
    log_in[1].onclick = () => {
        form = 'log-in';
        form_display(form);
    }
    sign_up[0].onclick = () => {
        form = 'sign-up';
        form_display(form, 35);
    }
    sign_up[1].onclick = () => {
        form = 'sign-up';
        form_display(form, 100);
    }

    const form_display = (form, brightness_percent) => {
        if (form == 'log-in') {
            login_display(brightness_percent);
        } else {
            signup_display(brightness_percent);
        }
    }

    const login_display = (brightness_percent) => {
        login_container.style.display = 'block';
        modal.style.backgroundColor = 'white';
        document.body.style.position = "fixed";
        document.body.style.overflowY = "scroll";
        document.body.style.backgroundColor = "gray";
        weeknight_dinner.style.filter = "brightness(" + brightness_percent + "%)";
    }

    const signup_display = (brightness_percent) => {
        signup_container.style.display = 'block';
        modal.style.backgroundColor = 'white';
        document.body.style.position = "fixed";
        document.body.style.overflowY = "scroll";
        document.body.style.backgroundColor = "gray";
        weeknight_dinner.style.filter = "brightness(" + brightness_percent + "%)";
    }

    login_close_button.onclick = () => {
        login_container.style.display = 'none';
        document.body.style.position = "static";
        document.body.style.overflowY = "auto";
        document.body.style.backgroundColor = "white";
        weeknight_dinner.style.filter = "brightness(100%)";
    }

    signup_close_button.onclick = () => {
        signup_container.style.display = 'none';
        document.body.style.position = "static";
        document.body.style.overflowY = "auto";
        document.body.style.backgroundColor = "white";
        weeknight_dinner.style.filter = "brightness(100%)";
    }

    const signup_form_link = document.getElementById('signup-form-link');
    signup_form_link.onclick = () => {
        signup_display(35);
        login_container.style.display = 'none';
    }

    const login_form_link = document.getElementById('login-form-link');
    login_form_link.onclick = () => {
        login_display(35);
        signup_container.style.display = 'none';
    }
} else {    
    search();

    function search() {
        // For search field.
        const search_field = document.getElementById('search-field');
        const search_icon = document.getElementById('search-icon');
        search_field.onclick = () => {
            search_icon.style.display = 'none';
            search_field.style.borderTopLeftRadius = '60px';
            search_field.style.borderBottomLeftRadius = '60px';
            search_field.style.padding = '.6rem 1rem';
            search_field.style.backgroundColor = 'rgb(224, 224, 224)';        
        }
        search_field.onmouseenter = () => {
            search_field.style.backgroundColor = 'rgb(224, 224, 224)';
            search_icon.style.backgroundColor = 'rgb(224, 224, 224)';
        }
        search_field.onmouseleave = () => {
            search_field.style.backgroundColor = '#E9ECEF';
            search_icon.style.backgroundColor = '#E9ECEF';
        }
        document.onclick = () => {
            // Check if the clicked element is inside the target element
            if (!search_field.contains(event.target)) {
                search_icon.style.display = 'flex';
                search_field.style.borderTopLeftRadius = '0';
                search_field.style.borderBottomLeftRadius = '0';
                search_field.style.padding = '.6rem .6rem .6rem 0';
                search_field.style.backgroundColor = '#E9ECEF'; 
            }
        }
    }
    
}


