let countdown;
const timerDisplay = document.getElementById("timer");
const startButton = document.getElementById("start");
const resetButton = document.getElementById("reset");
const minutesInput = document.getElementById("minutes");
const secondsInput = document.getElementById("seconds");

startButton.addEventListener("click", startTimer);
resetButton.addEventListener("click", resetTimer);

function sendMetric(eventType) {
  fetch("/metrics", {
    method: "POST",
    body: JSON.stringify({ event: eventType }),
    headers: { "Content-Type": "application/json" }
  }).catch(err => console.error("Failed to send metric:", err));
}

function startTimer() {
  const minutes = parseInt(minutesInput.value) || 0;
  const seconds = parseInt(secondsInput.value) || 0;
  let totalTime = minutes * 60 + seconds;

  if (totalTime <= 0) {
    alert("Please set a valid time!");
    return;
  }

  clearInterval(countdown);
  sendMetric("start_timer");

  countdown = setInterval(() => {
    const mins = Math.floor(totalTime / 60);
    const secs = totalTime % 60;
    timerDisplay.textContent = `${String(mins).padStart(2, "0")}:${String(secs).padStart(2, "0")}`;

    if (totalTime <= 0) {
      clearInterval(countdown);
      alert("Time is up!");
      sendMetric("timer_finished");
    }

    totalTime--;
  }, 1000);
}

function resetTimer() {
  clearInterval(countdown);
  timerDisplay.textContent = "00:00";
  minutesInput.value = "";
  secondsInput.value = "";
  sendMetric("reset_timer");
}
