function updateTime() {
    const timeDisplay = document.getElementById('time');
    let currentTime = new Date();
    currentTime.setHours(currentTime.getUTCHours() + 3);
    let hours = currentTime.getHours().toString().padStart(2, '0');
    let minutes = currentTime.getMinutes().toString().padStart(2, '0');
    let seconds = currentTime.getSeconds().toString().padStart(2, '0');
    timeDisplay.textContent = `${hours}:${minutes}:${seconds}`;
}

setInterval(updateTime, 1000);