/*!
* Start Bootstrap - Scrolling Nav v5.0.5 (https://startbootstrap.com/template/scrolling-nav)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-scrolling-nav/blob/master/LICENSE)
*/
//
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            offset: 74,
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

});

// Up Arrow
// browser window scroll (in pixels) after which the "back to top" link is shown
var offset = 300,

// browser window scroll (in pixels) after which the "back to top" link opacity is reduced
offset_opacity = 1200,

//duration of the top scrolling animation (in ms)
scroll_top_duration = 700,

//grab the "back to top" link
$back_to_top = document.querySelector('.cd-top');

// hide or show the "back to top" link
window.addEventListener('scroll', function(e) {
  (window.scrollY > offset) ? $back_to_top.classList.add("cd-is-visible") : $back_to_top.classList.remove('cd-is-visible', 'cd-fade-out');
});

//smooth scroll to top
$back_to_top.addEventListener('click', function(e) {
  e.preventDefault();
  scroll({
   top: 0,
    behavior: "smooth"
  });
});