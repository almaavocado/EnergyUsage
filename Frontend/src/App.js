import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import SiteList from './components/SiteList';
import Home from './components/home/Home.jsx';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/sites" element={<SiteList />} />
      </Routes>
    </Router>
  );
}

export default App;
