import React from 'react';
import './HomeScreen.css';
import CarModel from './CarModel';

const carModels = [
  {
    photo: 'https://example.com/car1.jpg',
    details: 'Car Model 1',
    description: 'This is car model 1'
  },
  {
    photo: 'https://example.com/car2.jpg',
    details: 'Car Model 2',
    description: 'This is car model 2'
  },
  {
    photo: 'https://example.com/car3.jpg',
    details: 'Car Model 3',
    description: 'This is car model 3'
  }
];

const HomeScreen: React.FC = () => {
  return (
    <div className='home-screen'>
      {carModels.map((carModel, index) => (
        <CarModel key={index} photo={carModel.photo} details={carModel.details} description={carModel.description} />
      ))}
    </div>
  );
};

export default HomeScreen;