import axios from "axios";
import { BASE_URL } from "./api";

// Define the interface for the time response
export interface TimeNow {
    name: string;
    time: string;
}

// Function to fetch the current time for a given city
export const fetchTime = async (cityName: string): Promise<TimeNow> => {
    try {
        const endpoint = `${BASE_URL}/times/${cityName}`;
        const response = await axios.get<TimeNow>(endpoint);
        return response.data;
    } catch (error) {
        console.error("Error loading time:", error);
        throw error;
    }
};
