(function () {
  function revealAnimated() {
    document.querySelectorAll('.et_animated').forEach(function (el) {
      el.style.opacity = '1';
      el.style.transform = 'none';
      el.style.webkitAnimation = 'none';
      el.style.animation = 'none';
    });
  }

  function initSliders() {
    document.querySelectorAll('.et_pb_slider').forEach(function (slider) {
      var slides = Array.prototype.slice.call(slider.querySelectorAll('.et_pb_slide'));
      if (slides.length < 2) {
        if (slides.length === 1) {
          slides[0].style.opacity = '1';
          slides[0].classList.add('et-pb-active-slide');
        }
        return;
      }

      var parent = slides[0].parentElement; // .et_pb_slides

      // Set up parent as positioned container.
      // Do NOT set minHeight inline — let CSS @media queries handle responsive sizing.
      parent.style.position = 'relative';
      parent.style.overflow = 'hidden';

      // Stack all slides absolutely. Set display:block inline to override
      // Divi's embedded CSS rule: .et_pb_slider .et_pb_slide { display:none }.
      slides.forEach(function (slide) {
        slide.style.display = 'block';
        slide.style.position = 'absolute';
        slide.style.top = '0';
        slide.style.left = '0';
        slide.style.width = '100%';
        slide.style.opacity = '0';
        slide.style.transition = 'opacity 1s ease-in-out';
        slide.style.pointerEvents = 'none';
      });

      var current = 0;

      // Show the first slide instantly (no fade-in on load)
      slides[0].style.transition = 'none';
      slides[0].style.opacity = '1';
      slides[0].style.pointerEvents = 'auto';
      slides[0].classList.add('et-pb-active-slide');

      // Re-enable transition after first paint so subsequent swaps crossfade
      requestAnimationFrame(function () {
        requestAnimationFrame(function () {
          slides[0].style.transition = 'opacity 1s ease-in-out';
        });
      });

      var speedMatch = slider.className.match(/et_slider_speed_(\d+)/);
      var speed = speedMatch ? parseInt(speedMatch[1]) : 7000;

      setInterval(function () {
        // Fade out the current slide
        slides[current].style.opacity = '0';
        slides[current].style.pointerEvents = 'none';
        slides[current].classList.remove('et-pb-active-slide');

        // Advance and fade in the next slide
        current = (current + 1) % slides.length;
        slides[current].style.opacity = '1';
        slides[current].style.pointerEvents = 'auto';
        slides[current].classList.add('et-pb-active-slide');
      }, speed);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
      revealAnimated();
      initSliders();
    });
  } else {
    revealAnimated();
    initSliders();
  }
})();
