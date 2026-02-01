// Mobile CTA Bar - Show/Hide on Scroll
(function () {
    'use strict';

    // Only run on mobile devices
    if (window.innerWidth > 768) return;

    const mobileCTABar = document.querySelector('.mobile-cta-bar');
    if (!mobileCTABar) return;

    let lastScrollTop = 0;
    let scrollTimeout;

    function handleScroll() {
        clearTimeout(scrollTimeout);

        scrollTimeout = setTimeout(function () {
            const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

            // Show CTA bar after scrolling down 300px
            if (scrollTop > 300) {
                mobileCTABar.classList.add('visible');
                document.body.classList.add('mobile-cta-active');
            } else {
                mobileCTABar.classList.remove('visible');
                document.body.classList.remove('mobile-cta-active');
            }

            lastScrollTop = scrollTop;
        }, 100); // Debounce scroll events
    }

    // Listen to scroll events
    window.addEventListener('scroll', handleScroll, { passive: true });

    // Check initial scroll position
    handleScroll();
})();
