const showNavbar = (toggleId, navId, bodyId, headerId) => {
  const toggle = document.getElementById(toggleId),
    nav = document.getElementById(navId),
    bodypd = document.getElementById(bodyId),
    headerpd = document.getElementById(headerId);

  // Validate that all variables exist
  if (toggle && nav && bodypd && headerpd) {
    toggle.addEventListener('click', () => {
      // show navbar
      nav.classList.toggle('show');
      // change icon
      toggle.classList.toggle('bx-x');
      // add padding to body
      bodypd.classList.toggle('body-pd');
      // add padding to header
      headerpd.classList.toggle('body-pd');
    });
  }
};

const copyLink = (e) => {
  let target = $(e.target);
  navigator.clipboard.writeText(target.data('link'));
};

$(document).ready(() => {
  showNavbar('header-toggle', 'nav-bar', 'body-pd', 'header');
  $('span.copy-link').on('click', copyLink);
});
