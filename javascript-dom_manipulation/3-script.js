const toggleheader = document.querySelector('#toggle_header');
const header = document.querySelector('header');
toggleheader.addEventListener('click', function () {
  header.classList.toggle('green');
  header.classList.toggle('red');
});
