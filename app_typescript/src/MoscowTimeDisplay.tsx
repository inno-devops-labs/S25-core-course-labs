import { useState, useEffect } from 'react';

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
            hour12: false,
        });
    };

    return (
        <div>
            <h2>Current time in Moscow</h2>
            <span>{formatTime(moscowTime)}</span>
        </div>
    );
};

export default MoscowTimeDisplay;
