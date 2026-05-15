import React from 'react';
import './CarModel.css';

interface CarModelProps {
  photo: string;
  details: string;
  description: string;
}

const CarModel: React.FC<CarModelProps> = ({ photo, details, description }) => {
  return (
    <div className='car-model'>
      <img src={photo} alt='Car Model' />
      <h2>{details}</h2>
      <p>{description}</p>
    </div>
  );
};

export default CarModel;