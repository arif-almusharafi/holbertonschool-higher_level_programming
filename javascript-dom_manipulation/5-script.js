const updateheader = document.querySelector('#update_header');
const header = document.querySelector('header');
updateheader.addEventListener('click', function () {
    header.textContent = 'New Header!!!';
});
