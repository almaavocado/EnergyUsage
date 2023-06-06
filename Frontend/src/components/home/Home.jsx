import React from "react";
import { Link } from 'react-router-dom';
import "./home.css"

function Home() {
  return (
    <div className="home-container">
      <h1>Welcome to Voltus Site List</h1>
      <p>Please have your API key ready to fetch and display your site list.</p>
      <Link to="/sites" className="button-link">Go to Site List</Link>
    </div>
  );
}

export default Home;
