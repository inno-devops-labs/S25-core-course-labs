import React, { useEffect, useState } from 'react';
import { fetchTZs, TimeZone } from '../api/tzgetter';
import { fetchTime, TimeNow } from '../api/timegetter';

const MainPage = () => {
    const [timeZones, setTimeZones] = useState<TimeZone[]>([]);
    const [selectedCity, setSelectedCity] = useState<string>("");
    const [currentTime, setCurrentTime] = useState<string>("");
    const [loading, setLoading] = useState<boolean>(false);
    const [error, setError] = useState<string | null>(null);

    // Fetch time zones when the component mounts
    useEffect(() => {
        const loadTimeZones = async () => {
            try {
                const data = await fetchTZs();
                console.log("Fetched time zones:", data); // Debugging statement
                setTimeZones(data);
            } catch (error) {
                console.log("Loading error", error);
                setError("Error with loading");
            }
        };
        loadTimeZones();
    }, []);

    // Fetch current time for the selected city
    useEffect(() => {
        let intervalId: NodeJS.Timeout;

        if (selectedCity) {
            const fetchCurrentTime = async () => {
                try {
                    setLoading(true);
                    const timeData = await fetchTime(selectedCity);
                    console.log("Fetched time data:", timeData); // Debugging statement
                    setCurrentTime(timeData.time); // Corrected the field name to match the API response
                    setError(null);
                } catch (error) {
                    console.error("Error with loading time:", error);
                    setError("Error with loading time");
                } finally {
                    setLoading(false);
                }
            };

            fetchCurrentTime(); // Initial time fetch
            intervalId = setInterval(fetchCurrentTime, 1000); // Subsequent time fetches
        }

        return () => {
            if (intervalId) {
                clearInterval(intervalId);
            }
        };
    }, [selectedCity]);

    // Handle city selection change
    const handleCityChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
        setSelectedCity(event.target.value);
        setCurrentTime(""); // Reset current time
    };

    return (
        <div>
            <h1>Current Time</h1>
            <div className="dropdown">
                <select value={selectedCity} onChange={handleCityChange}>
                    <option value="">--Choose the city--</option>
                    {timeZones.map(city => (
                        <option key={city.id} value={city.name}>
                            {city.name}
                        </option>
                    ))}
                </select>
            </div>
            {loading && <p>Loading...</p>}
            {currentTime && (
                <div>
                    <p>{currentTime}</p>
                </div>
            )}
            {error && <p>{error}</p>}
        </div>
    );
};

export default MainPage;
