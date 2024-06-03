document.addEventListener("DOMContentLoaded", function() {
    const contactForm = document.getElementById('contactForm');
    const successMessage = document.getElementById('form-message-success');
    const warningMessage = document.getElementById('form-message-warning');

    contactForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission behavior

        // Here you can add additional form validation or handling if needed

        // Display the success message
        successMessage.style.display = 'block';

        // Optionally hide the form after submission
        contactForm.style.display = 'none';
    });
});

