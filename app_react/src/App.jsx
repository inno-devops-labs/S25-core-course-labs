import { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [currentTime, setCurrentTime] = useState('');

  useEffect(() => {
    fetchCurrentTime();
    const intervalId = setInterval(fetchCurrentTime, 1000); // Update every second
    return () => clearInterval(intervalId);
  }, []);

  const fetchCurrentTime = async () => {
    try {
      const date = new Date().toLocaleString("en-US", {timeZone: "Europe/Moscow"});
      const formattedTime = date.toLocaleString('en-US', {
        timeZone: 'Europe/Moscow',
        hour12: false,
      });
      setCurrentTime(formattedTime);
    } catch (error) {
      console.error('Error fetching the current time:', error);
      setCurrentTime('Unable to retrieve time');
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Current Time in Moscow</h1>
        <p>{currentTime}</p>
      </header>
    </div>
  );
}

export default App;