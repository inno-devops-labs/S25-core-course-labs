import { useState, useEffect } from "react";
import { DateTime } from "luxon";
import "./App.css";

function App() {
  /* using state in react to make the website self render everysecond and update the time*/

  const [time, setTime] = useState(getMoscowTime());
  /*This function use the luxon library to get the time based on the time zone then I am converting the time using toFormat function*/ 
  function getMoscowTime() {
    return DateTime.now().setZone("Europe/Moscow").toFormat("HH:mm:ss");
  }

  useEffect(() => {
    const interval = setInterval(() => {
      setTime(getMoscowTime());
    }, 1000);

    return () => clearInterval(interval); // Cleanup interval on unmount
  }, []);

  return (
    <div className="hero"> 
      <div className="container">
        <div className="clock">
          <span id="hrs">{time.split(":")[0]}</span>
          <span>:</span>
          <span id="min">{time.split(":")[1]}</span>
          <span>:</span>
          <span id="sec">{time.split(":")[2]}</span>
        </div>
      </div>
    </div>
  );
}

export default App;
