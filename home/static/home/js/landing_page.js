const is_user_logged_in = document.getElementById('is-user-logged-in').textContent;

if (is_user_logged_in === 'AnonymousUser') {
    // For Register and Log in.
    const log_in = document.getElementById('log-in');
    const sign_up = document.getElementById('sign-up');
    let form = null;

    log_in.onclick = () => {
        form = 'log-in';
        form_display(form, 35);
    }

    sign_up.onclick = () => {
        form = 'sign-up';
        form_display(form, 35);
    } 

    const form_display = (form, brightness_percent) => {
        if (form === 'log-in') {
            login_display(brightness_percent);
        } else {
            signup_display(brightness_percent);
        }
    }

    const top_nav = document.getElementById('top-nav');
    const login_container = document.getElementById('login-container');
    const signup_container = document.getElementById('signup-container');
    const modal = document.getElementById('modal');
    const weeknight_dinner = document.getElementById('weeknight-dinner');

    const login_display = (brightness_percent) => {
        login_container.style.display = 'block';
        top_nav.style.backgroundColor = 'initial';
        log_in.style.backgroundColor = '#a1a1a1'
        sign_up.style.backgroundColor = '#a1a1a1'
        modal.style.backgroundColor = 'white';
        document.body.style.position = "fixed";
        document.body.style.overflowY = "scroll";
        document.body.style.backgroundColor = "#666767";
        weeknight_dinner.style.filter = "brightness(" + brightness_percent + "%)";

    }

    const signup_display = (brightness_percent) => {
        signup_container.style.display = 'block';
        top_nav.style.backgroundColor = 'initial'
        log_in.style.backgroundColor = '#a1a1a1'
        sign_up.style.backgroundColor = '#a1a1a1';
        modal.style.backgroundColor = 'white';
        document.body.style.position = "fixed";
        document.body.style.overflowY = "scroll";
        document.body.style.backgroundColor = "#666767";
        weeknight_dinner.style.filter = "brightness(" + brightness_percent + "%)";
    }

    const login_close_button = document.getElementById('login-close-button');
    const signup_close_button = document.getElementById('signup-close-button');
    login_close_button.onclick = () => {
        login_container.style.display = 'none';
        log_in.style.backgroundColor = '#E70223'
        sign_up.style.backgroundColor = '#EFEFEF'
        document.body.style.position = "static";
        document.body.style.overflowY = "auto";
        document.body.style.backgroundColor = "white";
        weeknight_dinner.style.filter = "brightness(100%)";
    }

    signup_close_button.onclick = () => {
        signup_container.style.display = 'none';
        log_in.style.backgroundColor = '#E70223'
        sign_up.style.backgroundColor = '#EFEFEF'
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
}
