import { useEffect, useState } from "react";

function App() {
  // State to hold the current time
  const [time, setTime] = useState<string>("");

  useEffect(() => {
    // Function to update the time
    const updateTime = () => {
      const now = new Date();

      // Options for formatting the time with Moscow timezone
      const options: Intl.DateTimeFormatOptions = {
        timeZone: "Europe/Moscow",
        hour: "2-digit",
        minute: "2-digit",
        second: "2-digit",
      };

      // Update the state with the current time in Moscow
      setTime(new Intl.DateTimeFormat("en-GB", options).format(now));
    };

    // Initialize time update
    updateTime();
  }, []); // This effect runs only once when the component mounts

  return (
    <div className="flex items-center justify-center min-h-screen min-w-screen bg-gradient-to-r from-indigo-800 to-purple-900 text-white text-center">
      <div className="bg-[#00000055] p-6 rounded-2xl shadow-lg">
        <h1 className="text-3xl font-bold mb-2">Current Time in Moscow</h1>
        <p className="text-xl">{time}</p>
      </div>
    </div>
  );
}

export default App;
