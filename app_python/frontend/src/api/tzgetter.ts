import axios from "axios";
import { BASE_URL } from "./api";

// Define the interface for the time zone response
export interface TimeZone {
    id: number;
    name: string;
    timezone: string;
}

// Function to fetch all available time zones
export const fetchTZs = async (): Promise<TimeZone[]> => {
    try {
        const endpoint = BASE_URL + '/times';
        const response = await axios.get<TimeZone[]>(endpoint);
        return response.data;
    } catch (error) {
        console.error("Error loading available cities:", error);
        throw error;
    }
};
