function updateTime() {
    fetch('/ct')
        .then(response => response.json())
        .then(data => {
            document.getElementById('ct').textContent = data.ct;
        });
}

setInterval(updateTime, 1000);
