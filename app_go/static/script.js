function incrementCounter() {
    fetch('/increment')
        .then(response => response.text())
        .then(data => {
            document.getElementById('counter').innerText = data;
        });
}
