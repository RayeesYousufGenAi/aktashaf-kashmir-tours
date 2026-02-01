// ===================================
// AKTASHAF KASHMIR - Main JavaScript
// Interactive functionality
// ===================================

// Wait for DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function () {

    // ===================================
    // STICKY HEADER
    // ===================================
    // ===================================
    // SMART STICKY HEADER
    // ===================================
    const header = document.getElementById('header');
    const headerHeight = header.offsetHeight;
    let lastScrollTop = 0;

    window.addEventListener('scroll', function () {
        let scrollTop = window.pageYOffset || document.documentElement.scrollTop;

        // Add/remove background on scroll
        if (scrollTop > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }

        // Smart hide/show logic
        if (scrollTop > lastScrollTop && scrollTop > headerHeight + 50) {
            // Scrolling down & past header - Hide
            header.classList.add('header-hidden');
        } else {
            // Scrolling up - Show
            header.classList.remove('header-hidden');
        }

        lastScrollTop = scrollTop <= 0 ? 0 : scrollTop; // For Mobile or negative scrolling
    }, { passive: true });

    // ===================================
    // MOBILE MENU TOGGLE
    // ===================================
    const mobileMenuToggle = document.getElementById('mobileMenuToggle');
    const nav = document.getElementById('nav');

    if (mobileMenuToggle) {
        mobileMenuToggle.addEventListener('click', function () {
            nav.classList.toggle('active');

            // Toggle icon
            const icon = this.querySelector('i');
            if (nav.classList.contains('active')) {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-times');
            } else {
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            }
        });
    }

    // Close mobile menu when clicking on a link
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', function () {
            if (window.innerWidth <= 768) {
                nav.classList.remove('active');
                const icon = mobileMenuToggle.querySelector('i');
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            }
        });
    });

    // ===================================
    // SMOOTH SCROLL FOR ANCHOR LINKS
    // ===================================
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href !== '#' && href.length > 1) {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    const offsetTop = target.offsetTop - headerHeight;
                    window.scrollTo({
                        top: offsetTop,
                        behavior: 'smooth'
                    });
                }
            }
        });
    });

    // ===================================
    // ACTIVE NAV LINK ON SCROLL
    // ===================================
    const sections = document.querySelectorAll('section[id]');

    function updateActiveNavLink() {
        const scrollY = window.pageYOffset;

        sections.forEach(section => {
            const sectionHeight = section.offsetHeight;
            const sectionTop = section.offsetTop - headerHeight - 50;
            const sectionId = section.getAttribute('id');
            const navLink = document.querySelector(`.nav-link[href="#${sectionId}"]`);

            if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
                navLinks.forEach(link => link.classList.remove('active'));
                if (navLink) {
                    navLink.classList.add('active');
                }
            }
        });
    }

    window.addEventListener('scroll', updateActiveNavLink);

    // ===================================
    // BOOKING FORM VALIDATION & SUBMISSION
    // ===================================
    // ===================================
    // BOOKING FORM VALIDATION & SUBMISSION
    // ===================================
    // JS Form handling removed to allow Netlify Forms to process submissions natively
    // We rely on HTML5 validation (required, type="email", etc.)


    // ===================================
    // POPULAR PACKAGES CAROUSEL
    // ===================================
    const carouselTrack = document.getElementById('carouselTrack');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');

    if (carouselTrack && prevBtn && nextBtn) {
        let currentIndex = 0;
        const cards = carouselTrack.querySelectorAll('.carousel-card');
        const totalCards = cards.length;
        let cardsToShow = getCardsToShow();

        function getCardsToShow() {
            if (window.innerWidth <= 768) return 1;
            if (window.innerWidth <= 1024) return 3;
            return 4;
        }

        function updateCarousel() {
            const cardWidth = cards[0].offsetWidth;
            const gap = 20;
            const offset = -(currentIndex * (cardWidth + gap));
            carouselTrack.style.transform = `translateX(${offset}px)`;
        }

        prevBtn.addEventListener('click', function () {
            if (currentIndex > 0) {
                currentIndex--;
                updateCarousel();
            }
        });

        nextBtn.addEventListener('click', function () {
            const maxIndex = totalCards - cardsToShow;
            if (currentIndex < maxIndex) {
                currentIndex++;
                updateCarousel();
            }
        });

        // Auto-rotate carousel every 5 seconds
        let autoRotate = setInterval(function () {
            const maxIndex = totalCards - cardsToShow;
            if (currentIndex < maxIndex) {
                currentIndex++;
            } else {
                currentIndex = 0;
            }
            updateCarousel();
        }, 5000);

        // Pause auto-rotate on hover
        carouselTrack.addEventListener('mouseenter', function () {
            clearInterval(autoRotate);
        });

        carouselTrack.addEventListener('mouseleave', function () {
            autoRotate = setInterval(function () {
                const maxIndex = totalCards - cardsToShow;
                if (currentIndex < maxIndex) {
                    currentIndex++;
                } else {
                    currentIndex = 0;
                }
                updateCarousel();
            }, 5000);
        });

        // Update carousel on window resize
        window.addEventListener('resize', function () {
            cardsToShow = getCardsToShow();
            currentIndex = 0;
            updateCarousel();
        });

        // Touch/swipe support for mobile
        let touchStartX = 0;
        let touchEndX = 0;

        carouselTrack.addEventListener('touchstart', function (e) {
            touchStartX = e.changedTouches[0].screenX;
        });

        carouselTrack.addEventListener('touchend', function (e) {
            touchEndX = e.changedTouches[0].screenX;
            handleSwipe();
        });

        function handleSwipe() {
            const swipeThreshold = 50;
            const diff = touchStartX - touchEndX;

            if (Math.abs(diff) > swipeThreshold) {
                if (diff > 0) {
                    // Swipe left - next
                    const maxIndex = totalCards - cardsToShow;
                    if (currentIndex < maxIndex) {
                        currentIndex++;
                        updateCarousel();
                    }
                } else {
                    // Swipe right - prev
                    if (currentIndex > 0) {
                        currentIndex--;
                        updateCarousel();
                    }
                }
            }
        }
    }

    // ===================================
    // TOUR FILTER DROPDOWNS
    // ===================================
    const tourFilters = document.querySelectorAll('.filter-dropdown select');

    tourFilters.forEach(filter => {
        filter.addEventListener('change', function () {
            const selectedValue = this.value;
            if (selectedValue) {
                console.log('Filter selected:', selectedValue);
                // In a real application, this would filter the tour packages
                // For now, we'll just log the selection
            }
        });
    });

    // ===================================
    // EMAIL SUBSCRIPTION FORM
    // ===================================
    const subscribeForm = document.querySelector('.subscribe-form');

    if (subscribeForm) {
        subscribeForm.addEventListener('submit', function (e) {
            e.preventDefault();

            const emailInput = this.querySelector('input[type="email"]');
            const email = emailInput.value;

            // Validate email
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(email)) {
                alert('Please enter a valid email address');
                return;
            }

            // Success message
            alert(`Thank you for subscribing!\n\nYou will receive our latest Kashmir tour packages and offers at ${email}`);

            // Reset form
            emailInput.value = '';

            // In a real application, send to server
            console.log('Subscription email:', email);
        });
    }

    // ===================================
    // ASK QUERY BUTTON
    // ===================================
    const btnQuery = document.querySelector('.btn-query');

    if (btnQuery) {
        btnQuery.addEventListener('click', function () {
            // Scroll to booking form
            const bookingSection = document.querySelector('.hero');
            if (bookingSection) {
                const offsetTop = bookingSection.offsetTop - headerHeight;
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    }

    // ===================================
    // FADE IN ANIMATION ON SCROLL
    // ===================================
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function (entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in-up');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Observe elements for animation
    const animateElements = document.querySelectorAll('.destination-card, .testimonial-card, .feature-item, .tour-package-card');
    animateElements.forEach(el => observer.observe(el));

    // ===================================
    // LAZY LOADING IMAGES
    // ===================================
    const images = document.querySelectorAll('img[data-src]');

    const imageObserver = new IntersectionObserver(function (entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.removeAttribute('data-src');
                imageObserver.unobserve(img);
            }
        });
    });

    images.forEach(img => imageObserver.observe(img));

    // ===================================
    // PREVENT FORM DOUBLE SUBMISSION
    // ===================================
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function () {
            const submitBtn = this.querySelector('button[type="submit"]');
            if (submitBtn) {
                submitBtn.disabled = true;
                setTimeout(() => {
                    submitBtn.disabled = false;
                }, 3000);
            }
        });
    });

    // ===================================
    // CITY AUTOCOMPLETE BEHAVIOR
    // ===================================
    const cityInputs = document.querySelectorAll('input[list="cities"]');

    cityInputs.forEach(input => {
        // Initially remove the list attribute to prevent default dropdown
        input.removeAttribute('list');

        input.addEventListener('input', function () {
            if (this.value.length >= 1) {
                // Restore list attribute when user starts typing
                if (!this.getAttribute('list')) {
                    this.setAttribute('list', 'cities');
                }
            } else {
                // Remove list attribute if input is empty
                this.removeAttribute('list');
            }
        });

        // Also handle focus - ensure list is hidden if empty
        input.addEventListener('focus', function () {
            if (this.value.length === 0) {
                this.removeAttribute('list');
            }
        });
    });

    // ===================================
    // CONSOLE WELCOME MESSAGE
    // ===================================
    console.log('%c🏔️ Welcome to AKTASHAF KASHMIR 🏔️', 'color: #FF6B00; font-size: 20px; font-weight: bold;');
    console.log('%cExplore the Paradise on Earth!', 'color: #FDB714; font-size: 14px;');
    console.log('%cContact: +91 9796664664 | aktashafkmr@gmail.com', 'color: #666; font-size: 12px;');

    // ===================================
    // MOBILE CTA BAR LOGIC
    // ===================================
    const mobileCtaBar = document.querySelector('.mobile-cta-bar');
    if (mobileCtaBar) {
        // Show immediately if on mobile
        if (window.innerWidth <= 768) {
            setTimeout(() => {
                mobileCtaBar.classList.add('visible');
                document.body.classList.add('mobile-cta-active');
            }, 1000); // 1s delay for effect
        }

        // Handle resize
        window.addEventListener('resize', function () {
            if (window.innerWidth <= 768) {
                mobileCtaBar.classList.add('visible');
                document.body.classList.add('mobile-cta-active');
            } else {
                mobileCtaBar.classList.remove('visible');
                document.body.classList.remove('mobile-cta-active');
            }
        });
    }

});

// ===================================
// UTILITY FUNCTIONS
// ===================================

// Format phone number
function formatPhoneNumber(phone) {
    const cleaned = phone.replace(/\D/g, '');
    const match = cleaned.match(/^(\d{3})(\d{3})(\d{4})$/);
    if (match) {
        return `(${match[1]}) ${match[2]}-${match[3]}`;
    }
    return phone;
}

// Validate Indian mobile number
function isValidIndianMobile(phone) {
    const cleaned = phone.replace(/\D/g, '');
    return /^[6-9]\d{9}$/.test(cleaned);
}

// Get current date in YYYY-MM-DD format
function getCurrentDate() {
    const today = new Date();
    const year = today.getFullYear();
    const month = String(today.getMonth() + 1).padStart(2, '0');
    const day = String(today.getDate()).padStart(2, '0');
    return `${year}-${month}-${day}`;
}

// ===================================
// PWA SERVICE WORKER & INSTALLATION
// ===================================
if ('serviceWorker' in navigator) {
    window.addEventListener('load', function () {
        navigator.serviceWorker.register('./sw.js').then(function (registration) {
            console.log('ServiceWorker registration successful with scope: ', registration.scope);
        }, function (err) {
            console.log('ServiceWorker registration failed: ', err);
        });
    });
}

let deferredPrompt;
const installButton = document.createElement('button');
installButton.style.display = 'none';
installButton.className = 'pwa-install-btn';
installButton.innerHTML = '<i class="fas fa-download"></i> Install App';
installButton.style.position = 'fixed';
installButton.style.bottom = '80px'; // Above mobile bar
installButton.style.left = '50%';
installButton.style.transform = 'translateX(-50%)';
installButton.style.zIndex = '9998';
installButton.style.padding = '10px 20px';
installButton.style.background = '#FDB714';
installButton.style.color = '#1a2332';
installButton.style.border = 'none';
installButton.style.borderRadius = '25px';
installButton.style.fontWeight = 'bold';
installButton.style.boxShadow = '0 4px 15px rgba(0,0,0,0.3)';
installButton.style.cursor = 'pointer';

document.body.appendChild(installButton); // Append to body

// Handle install prompt
window.addEventListener('beforeinstallprompt', (e) => {
    // Prevent Chrome 67 and earlier from automatically showing the prompt
    e.preventDefault();
    // Stash the event so it can be triggered later.
    deferredPrompt = e;
    // Update UI to notify the user they can add to home screen
    installButton.style.display = 'flex';
    installButton.style.alignItems = 'center';
    installButton.style.gap = '8px';
});

installButton.addEventListener('click', (e) => {
    // Hide our user interface that shows our A2HS button
    installButton.style.display = 'none';
    // Show the prompt
    deferredPrompt.prompt();
    // Wait for the user to respond to the prompt
    deferredPrompt.userChoice.then((choiceResult) => {
        if (choiceResult.outcome === 'accepted') {
            console.log('User accepted the A2HS prompt');
        } else {
            console.log('User dismissed the A2HS prompt');
        }
        deferredPrompt = null;
    });
});


// ===================================
// FLATPICKR DATE PICKER
// ===================================
const dateInputs = document.querySelectorAll('input[type="date"]');
if (dateInputs.length > 0 && typeof flatpickr !== 'undefined') {
    flatpickr('input[type="date"]', {
        minDate: "today",
        dateFormat: "Y-m-d",
        disableMobile: "true", // Force custom styled picker on mobile
        theme: "material_blue", // We will override with CSS
        onChange: function (selectedDates, dateStr, instance) {
            // Optional: Add logic if needed when date changes
        }
    });
} else if (dateInputs.length > 0) {
    // Fallback if script hasn't loaded yet (though we'll ensure it does)
    const today = new Date().toISOString().split('T')[0];
    dateInputs.forEach(input => input.setAttribute('min', today));
}

// ===================================
// MODERN ENHANCEMENTS
// ===================================

// Enhanced Image Lazy Loading with Fade-in Effect
document.addEventListener('DOMContentLoaded', function () {
    const lazyImages = document.querySelectorAll('img[loading="lazy"]');

    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    // Check if image is already loaded (cached)
                    if (img.complete && img.naturalWidth > 0) {
                        img.classList.add('loaded');
                    } else {
                        img.addEventListener('load', () => {
                            img.classList.add('loaded');
                        });
                    }
                    observer.unobserve(img);
                }
            });
        });

        lazyImages.forEach(img => imageObserver.observe(img));
    }

    // Scroll-triggered Animations
    const animateOnScroll = () => {
        const elements = document.querySelectorAll('.tour-package-card, .destination-card, .testimonial-card');

        const observer = new IntersectionObserver((entries) => {
            entries.forEach((entry, index) => {
                if (entry.isIntersecting) {
                    setTimeout(() => {
                        entry.target.classList.add('animate-fade-in-up');
                    }, index * 100); // Stagger animation
                    observer.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        });

        elements.forEach(el => observer.observe(el));
    };

    animateOnScroll();

    // Performance Monitoring (optional - for development)
    if (window.performance && window.performance.timing) {
        window.addEventListener('load', () => {
            setTimeout(() => {
                const perfData = window.performance.timing;
                const pageLoadTime = perfData.loadEventEnd - perfData.navigationStart;
                console.log(`%cPage Load Time: ${pageLoadTime}ms`, 'color: #00b894; font-weight: bold;');
            }, 0);
        });
    }

    // Add smooth hover effects to cards
    const cards = document.querySelectorAll('.tour-package-card, .destination-card, .premium-card');
    cards.forEach(card => {
        card.classList.add('hover-lift');
    });

    // Enhanced form feedback
    const formInputs = document.querySelectorAll('input, textarea, select');
    formInputs.forEach(input => {
        input.addEventListener('blur', function () {
            if (this.value.trim() !== '') {
                this.classList.add('filled');
            } else {
                this.classList.remove('filled');
            }
        });

        // Add validation feedback
        input.addEventListener('invalid', function (e) {
            e.preventDefault();
            this.classList.add('error');
        });

        input.addEventListener('input', function () {
            this.classList.remove('error');
        });
    });
});

// Debounce function for performance
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Optimized scroll handler
const handleScroll = debounce(() => {
    const scrolled = window.pageYOffset;
    const parallaxElements = document.querySelectorAll('[data-parallax]');

    parallaxElements.forEach(el => {
        const speed = el.dataset.parallax || 0.5;
        el.style.transform = `translateY(${scrolled * speed}px)`;
    });
}, 10);

window.addEventListener('scroll', handleScroll, { passive: true });

