// Mobile Menu Toggle
const mobileMenuToggle = document.getElementById('mobile-menu-toggle');
const mainNav = document.getElementById('main-nav');

if (mobileMenuToggle && mainNav) {
  mobileMenuToggle.addEventListener('click', () => {
    mainNav.classList.toggle('active');
  });
}

// Hero Slider
const slides = document.querySelectorAll('.slide');
const dotsContainer = document.getElementById('slider-dots');

if (slides.length > 0 && dotsContainer) {
  let currentSlide = 0;
  const slideInterval = 8000; // 8 seconds per slide
  let sliderTimer;

  // Create dots
  slides.forEach((_, index) => {
    const dot = document.createElement('div');
    dot.classList.add('dot');
    if (index === 0) dot.classList.add('active');
    dot.addEventListener('click', () => goToSlide(index));
    dotsContainer.appendChild(dot);
  });

  const dots = document.querySelectorAll('.dot');

  function goToSlide(index) {
    // Remove active class from current
    slides[currentSlide].classList.remove('active');
    dots[currentSlide].classList.remove('active');

    // Update current slide
    currentSlide = index;

    // Add active class to new current
    slides[currentSlide].classList.add('active');
    dots[currentSlide].classList.add('active');

    // Reset timer
    resetTimer();
  }

  function nextSlide() {
    let newIndex = currentSlide + 1;
    if (newIndex >= slides.length) newIndex = 0;
    goToSlide(newIndex);
  }

  function resetTimer() {
    clearInterval(sliderTimer);
    sliderTimer = setInterval(nextSlide, slideInterval);
  }

  // Start timer initially
  resetTimer();
}

// Sticky Header
const header = document.getElementById('main-header');
if (header) {
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      header.style.boxShadow = '0 10px 30px rgba(0, 0, 0, 0.15)';
      header.style.padding = '0.5rem 0';
    } else {
      header.style.boxShadow = '0 4px 12px rgba(0, 0, 0, 0.08)';
      header.style.padding = '1rem 0';
    }
  });
}
