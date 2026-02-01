// ===================================
// PREMIUM FORM HANDLING
// No redirects - inline success messages
// ===================================

document.addEventListener('DOMContentLoaded', function () {
    // Handle all Netlify forms
    const forms = document.querySelectorAll('form[data-netlify="true"]');

    forms.forEach(form => {
        form.addEventListener('submit', handleFormSubmit);
    });
});

async function handleFormSubmit(e) {
    e.preventDefault();

    const form = e.target;
    const submitBtn = form.querySelector('button[type="submit"]');
    const formData = new FormData(form);

    // Show loading state
    const originalBtnText = submitBtn.innerHTML;
    submitBtn.disabled = true;
    submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending...';

    try {
        const response = await fetch('/', {
            method: 'POST',
            headers: { "Content-Type": "application/x-www-form-urlencoded" },
            body: new URLSearchParams(formData).toString()
        });

        if (response.ok) {
            // Show success message
            showSuccessMessage(form);
            form.reset();
        } else {
            throw new Error('Form submission failed');
        }
    } catch (error) {
        // Show error message
        showErrorMessage(form);
    } finally {
        // Reset button
        submitBtn.disabled = false;
        submitBtn.innerHTML = originalBtnText;
    }
}

function showSuccessMessage(form) {
    // Remove any existing messages
    const existingMsg = form.querySelector('.form-message');
    if (existingMsg) existingMsg.remove();

    // Create success message
    const successMsg = document.createElement('div');
    successMsg.className = 'form-message success-message';
    successMsg.innerHTML = `
        <div class="message-icon">
            <i class="fas fa-check-circle"></i>
        </div>
        <div class="message-content">
            <h4>Thank You!</h4>
            <p>Your message has been received. We'll get back to you within 24 hours.</p>
        </div>
    `;

    // Insert message
    form.insertBefore(successMsg, form.firstChild);

    // Animate in
    setTimeout(() => successMsg.classList.add('show'), 10);

    // Scroll to message
    successMsg.scrollIntoView({ behavior: 'smooth', block: 'center' });

    // Auto-hide after 8 seconds
    setTimeout(() => {
        successMsg.classList.remove('show');
        setTimeout(() => successMsg.remove(), 300);
    }, 8000);
}

function showErrorMessage(form) {
    // Remove any existing messages
    const existingMsg = form.querySelector('.form-message');
    if (existingMsg) existingMsg.remove();

    // Create error message
    const errorMsg = document.createElement('div');
    errorMsg.className = 'form-message error-message';
    errorMsg.innerHTML = `
        <div class="message-icon">
            <i class="fas fa-exclamation-circle"></i>
        </div>
        <div class="message-content">
            <h4>Oops!</h4>
            <p>Something went wrong. Please try again or call us directly.</p>
        </div>
    `;

    // Insert message
    form.insertBefore(errorMsg, form.firstChild);

    // Animate in
    setTimeout(() => errorMsg.classList.add('show'), 10);

    // Scroll to message
    errorMsg.scrollIntoView({ behavior: 'smooth', block: 'center' });

    // Auto-hide after 6 seconds
    setTimeout(() => {
        errorMsg.classList.remove('show');
        setTimeout(() => errorMsg.remove(), 300);
    }, 6000);
}
