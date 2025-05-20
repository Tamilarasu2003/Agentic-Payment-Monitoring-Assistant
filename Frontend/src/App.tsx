
import './App.css'

import React from 'react';
import FileUpload from './Components/FileUpload';

const App: React.FC = () => {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <FileUpload />
    </div>
  );
};

export default App;

