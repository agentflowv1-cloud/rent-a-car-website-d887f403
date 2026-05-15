import React from 'react';
import { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';

function CarModelDetails() {
    const { carModelId } = useParams();
    const [carModel, setCarModel] = useState(null);

    useEffect(() => {
        fetch(`http://localhost:8000/car-models/${carModelId}`)
            .then(response => response.json())
            .then(data => setCarModel(data))
            .catch(error => console.error('Error fetching car model:', error));
    }, [carModelId]);

    if (!carModel) return <div>Loading...</div>;

    return (
        <div>
            <h1>{carModel.name}</h1>
            <p>Year: {carModel.year}</p>
            <p>Horsepower: {carModel.horsepower}</p>
            <Link to='/car-models'>Back to car models</Link>
        </div>
    );
}

export default CarModelDetails;