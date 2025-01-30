import React, { useEffect, useState } from "react";

const App: React.FC = () => {
  const [time, setTime] = useState<string>("");
  useEffect(() => {
    const intervalId = setInterval(() => {
      const moscowTime = new Date().toLocaleString("ru-RU", {
        timeZone: "Europe/Moscow",
        hour: "2-digit",
        minute: "2-digit",
        second: "2-digit",
      });
      setTime(moscowTime);
    }, 100);
    return () => clearInterval(intervalId);
  }, []);

  return (
    <div>
      <div className="time-container">
        <h2>Moscow Time</h2>
        <h1>{time}</h1>
      </div>
    </div>
  );
};

export default App;
