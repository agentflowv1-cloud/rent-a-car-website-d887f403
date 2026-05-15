import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import CarModelDetails from './CarModelDetails';
import CarModels from './CarModels';

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path='/car-models' element={<CarModels />} />
                <Route path='/car-models/:carModelId' element={<CarModelDetails />} />
            </Routes>
        </BrowserRouter>
    );
}

export default App;