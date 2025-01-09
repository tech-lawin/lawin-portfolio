"use client";

import { useEffect, useState } from 'react';

export default function Home() {
    const [data, setData] = useState(null);

    useEffect(() => {
        // Fetch data from the Flask backend
        fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/test`)
            .then((response) => response.json())
            .then((json) => setData(json))
            .catch((error) => console.error('Error fetching data:', error));
    }, []);

    return (
        <div style={{ padding: '20px', fontFamily: 'Arial' }}>
            <h1>Welcome to Lawin's Portfolio</h1>
            {data ? (
                <p>Backend says: {data.message}</p>
            ) : (
                <p>Loading data from backend...</p>
            )}
        </div>
    );
}
