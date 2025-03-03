let counter = 0;

const cookie = document.getElementById('cookie');
const counterElement = document.getElementById('counter');

cookie.addEventListener('click', function() {
    counter++;
    counterElement.textContent = counter;
});
