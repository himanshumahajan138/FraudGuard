const loginForm = document.getElementById('login-form');
const registerForm = document.getElementById('register-form'); // Assuming you have a separate form with this ID

// Check if login form exists
if (loginForm) {
    loginForm.addEventListener('submit', function (event) {
        // Check if username and password fields are empty
        const username = document.getElementById('username').value.trim();
        const password = document.getElementById('password').value.trim();

        // Remove any previous error messages
        const errorMessages = document.querySelectorAll('.error-message');
        errorMessages.forEach(message => message.remove());

        
        if (username === '' || password === '') {
            event.preventDefault(); // Prevent form submission
            const message = username === '' && password === ''
            ? 'Please enter username and password.'
            : 'Please enter a missing field. New user? Register here.';
            alert(message); // Or display the message in a more user-friendly way
        }

        if (username === '') {
            event.preventDefault(); // Prevent form submission
            const usernameField = document.getElementById('username');
            usernameField.classList.add('error');  // Add error class for styling
            const usernameError = document.createElement('p');
            usernameError.classList.add('error-message');
            usernameError.textContent = 'Username cannot be empty.';
            usernameField.parentNode.insertBefore(usernameError, usernameField.nextSibling);
        } else {
            usernameField.classList.remove('error'); // Remove error class if username is filled
        }

        if (password === '') {
            event.preventDefault(); // Prevent form submission
            const passwordField = document.getElementById('password');
            passwordField.classList.add('error');  // Add error class for styling
            const passwordError = document.createElement('p');
            passwordError.classList.add('error-message');
            passwordError.textContent = 'Password cannot be empty.';
            passwordField.parentNode.insertBefore(passwordError, passwordField.nextSibling);
        } else {
            passwordField.classList.remove('error'); // Remove error class if password is filled
        }
    });
}

if (registerForm) {
    registerForm.addEventListener('submit', function (event) {
        // Remove any previous error messages
        const errorMessages = document.querySelectorAll('.error-message');
        errorMessages.forEach(message => message.remove());

        // Get form field values
        const username = document.getElementById('username').value.trim();
        const email = document.getElementById('email').value.trim();
        const password = document.getElementById('password').value.trim();
        const confirmPassword = document.getElementById('confirm_password').value.trim();  // Assuming this ID for confirm password

        // Username validation
        if (username === '') {
            event.preventDefault(); // Prevent form submission
            const usernameField = document.getElementById('username');
            usernameField.classList.add('error');  // Add error class for styling
            const usernameError = document.createElement('p');
            usernameError.classList.add('error-message');
            usernameError.textContent = 'Username cannot be empty.';
            usernameField.parentNode.insertBefore(usernameError, usernameField.nextSibling);
        } else {
            usernameField.classList.remove('error'); // Remove error class if username is filled
        }

        // Email validation
        if (email === '') {
            event.preventDefault(); // Prevent form submission
            const emailField = document.getElementById('email');
            emailField.classList.add('error');  // Add error class for styling
            const emailError = document.createElement('p');
            emailError.classList.add('error-message');
            emailError.textContent = 'Email cannot be empty.';
            emailField.parentNode.insertBefore(emailError, emailField.nextSibling);
        } else if (!/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email)) {
            event.preventDefault(); // Prevent form submission
            const emailField = document.getElementById('email');
            emailField.classList.add('error');  // Add error class for styling
            const emailError = document.createElement('p');
            emailError.classList.add('error-message');
            emailError.textContent = 'Invalid email format.';
            emailField.parentNode.insertBefore(emailError, emailField.nextSibling);
        } else {
            emailField.classList.remove('error'); // Remove error class if email is valid
        }

        // Password validation
        if (password === '') {
            event.preventDefault(); // Prevent form submission
            const passwordField = document.getElementById('password');
            passwordField.classList.add('error');  // Add error class for styling
            const passwordError = document.createElement('p');
            passwordError.classList.add('error-message');
            passwordError.textContent = 'Password cannot be empty.';
            passwordField.parentNode.insertBefore(passwordError, passwordField.nextSibling);
        } else {
            passwordField.classList.remove('error'); // Remove error class if password is filled
        }

        // Confirm password validation
        if (confirmPassword === '') {
            event.preventDefault(); // Prevent form submission
            const confirmPasswordField = document.getElementById('confirm_password');
            confirmPasswordField.classList.add('error');  // Add error class for styling
            const confirmPasswordError = document.createElement('p');
            confirmPasswordError.classList.add('error-message');
            confirmPasswordError.textContent = 'Confirm password cannot be empty.';
            confirmPasswordField.parentNode.insertBefore(confirmPasswordError, confirmPasswordField.nextSibling);
        } else if (password !== confirmPassword) {
            event.preventDefault(); // Prevent form submission
            const confirmPasswordField = document.getElementById('confirm_password');
            confirmPasswordField.classList.add('error');  // Add error class for styling
            const confirmPasswordError = document.createElement('p');
            confirmPasswordError.classList.add('error-message');
            confirmPasswordError.textContent = 'Passwords do not match.';
            confirmPasswordField.parentNode.insertBefore(confirmPasswordError, confirmPasswordField.nextSibling);
        } else {
            confirmPasswordField.classList.remove('error'); // Remove error class if passwords match
        }
        // ... existing validation logic ...


        // If all validations pass, form submission can proceed
        // (You don't need to explicitly prevent default here if all checks passed)
    });
}
