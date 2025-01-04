function login() {
    const email = document.getElementById('email').value.trim(); // Trim whitespace
    const password = document.getElementById('password').value.trim();

    if (!email || !password) {
        alert('Please fill in both email and password.');
        return;
    }

    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/auth/login-request', true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                // Redirect on successful login
                window.location.href = '/catalog/catalog-page';
            } else {
                try {
                    const errorResponse = JSON.parse(xhr.responseText); // Parse error message if it's JSON
                    alert('Login failed: ' + (errorResponse.message || xhr.responseText));
                } catch (e) {
                    alert('Login failed: ' + xhr.responseText);
                }
            }
        }
    };

    // Send the encoded form data
    xhr.send('email=' + encodeURIComponent(email) + '&password=' + encodeURIComponent(password));
}
