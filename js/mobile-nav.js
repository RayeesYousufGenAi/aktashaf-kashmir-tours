// ===================================
// MOBILE BOTTOM NAVIGATION
// iOS-style app navigation
// ===================================

document.addEventListener('DOMContentLoaded', function () {
    // Only add mobile nav on mobile devices
    if (window.innerWidth <= 768) {
        addMobileBottomNav();
        setActiveNavItem();
    }
});

function addMobileBottomNav() {
    // Check if nav already exists
    if (document.querySelector('.mobile-bottom-nav')) return;

    const nav = document.createElement('nav');
    nav.className = 'mobile-bottom-nav';
    nav.innerHTML = `
        <a href="index.html" class="nav-item" data-page="index">
            <i class="fas fa-home"></i>
            <span>Home</span>
        </a>
        <a href="domestic.html" class="nav-item" data-page="domestic">
            <i class="fas fa-map-marked-alt"></i>
            <span>Domestic</span>
        </a>
        <a href="international.html" class="nav-item" data-page="international">
            <i class="fas fa-globe-asia"></i>
            <span>International</span>
        </a>
        <a href="blogs.html" class="nav-item" data-page="blogs">
            <i class="fas fa-blog"></i>
            <span>Blogs</span>
        </a>
        <a href="contact.html" class="nav-item" data-page="contact">
            <i class="fas fa-envelope"></i>
            <span>Contact</span>
        </a>
    `;

    document.body.appendChild(nav);
}

function setActiveNavItem() {
    const currentPage = window.location.pathname.split('/').pop().replace('.html', '') || 'index';
    const navItems = document.querySelectorAll('.nav-item');

    navItems.forEach(item => {
        if (item.dataset.page === currentPage) {
            item.classList.add('active');
        }
    });
}

// Add haptic feedback simulation on touch
if ('ontouchstart' in window) {
    document.addEventListener('touchstart', function (e) {
        if (e.target.closest('.nav-item, button, .btn')) {
            // Visual feedback
            e.target.style.transform = 'scale(0.95)';
            setTimeout(() => {
                e.target.style.transform = '';
            }, 100);
        }
    });
}
