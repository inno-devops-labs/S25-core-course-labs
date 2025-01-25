import './App.css';

function App() {
  const currentTime = new Date().toLocaleTimeString('en-US', {
    timeZone: 'Europe/Moscow',
  });
  return (
    <main>
      <h1>Current time in Moscow: {currentTime}</h1>
    </main>
  );
}

export default App;
