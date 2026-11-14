const addItem = document.querySelector('#add_item');
const myList = document.querySelector('.my_list');

addItem.addEventListener('click', function () {
  const marker = document.createElement('li');
  marker.textContent = 'Item';
  myList.append(marker);
});
