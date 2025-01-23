import {useState, useEffect} from 'react';

const MoscowTimeDisplay = () => {
    const [moscowTime, setMoscowTime] = useState(new Date());

    useEffect(() => {
        const timer = setInterval(() => {
            setMoscowTime(new Date());
        }, 1000);

        return () => clearInterval(timer);
    }, []);

    const formatTime = (date: Date) => {
        return date.toLocaleString('ru-RU', {
            timeZone: 'Europe/Moscow',
            hour: '2-digit',
            minute: '2-digit',
            second: '2-digit',
            hour12: false
        });
    };

    return (
        <div className="text-center mt-4 p-3 bg-gray-100 rounded-lg">
            <h2 className="text-xl font-bold mb-2">Current time in Moscow</h2>
            <div className="text-3xl font-mono">{formatTime(moscowTime)}</div>
        </div>
    );
};

export default MoscowTimeDisplay;