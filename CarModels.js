import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

function CarModels() {
    const [carModels, setCarModels] = useState([]);

    useEffect(() => {
        fetch('http://localhost:8000/car-models/')
            .then(response => response.json())
            .then(data => setCarModels(data))
            .catch(error => console.error('Error fetching car models:', error));
    }, []);

    return (
        <div>
            <h1>Car Models</h1>
            <ul>
                {carModels.map(carModel => (
                    <li key={carModel.id}>
                        <Link to={`/car-models/${carModel.id}`}>{carModel.name}</Link>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default CarModels;