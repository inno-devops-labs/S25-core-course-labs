document.addEventListener('DOMContentLoaded', () => {
  const timeDisplay = document.getElementById('time-display');
  const copyButton = document.getElementById('copy-btn');
  let timeOffset = 0;

  async function initClock() {
    try {
      const response = await fetch('/api/moscow_time');
      const data = await response.json();
      const serverTime = new Date(data.time);
      timeOffset = serverTime - Date.now();
      updateClock();
      setInterval(updateClock, 1000);
    } catch (error) {
      console.error('Error fetching time:', error);
      timeDisplay.textContent += ' (client time)';
      setInterval(updateClock, 1000);
    }
  }

  function updateClock() {
    const moscowTime = new Date(Date.now() + timeOffset);
    const timeString = moscowTime.toLocaleString('en-GB', {
      timeZone: 'Europe/Moscow',
      year: 'numeric',
      month: '2-digit',
      day: '2-digit',
      hour: '2-digit',
      minute: '2-digit',
      second: '2-digit',
      hour12: false
    }).replace(/\//g, '-').replace(',', '');

    timeDisplay.querySelector('.time-text').textContent = timeString;
  }

  copyButton.addEventListener('click', async () => {
    try {
      const text = timeDisplay.querySelector('.time-text').textContent;
      await navigator.clipboard.writeText(text);
      copyButton.classList.add('copy-success');
      setTimeout(() => copyButton.classList.remove('copy-success'), 2000);
    } catch (err) {
      console.error('Copy failed:', err);
    }
  });

  initClock();
});


