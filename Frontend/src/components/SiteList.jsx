/* eslint-disable no-use-before-define */
/* eslint-disable react-hooks/exhaustive-deps */
import React, { useState, useEffect } from 'react';
import "./sitelist.css";

function SiteList() {
  const [apiKey, setApiKey] = useState('');
  const [sites, setSites] = useState([]);
  const [filteredSites, setFilteredSites] = useState([]);
  const [sortBy, setSortBy] = useState('');
  const [filterBy, setFilterBy] = useState('');
  const [error, setError] = useState('');

  useEffect(() => {
    fetchSites();
  }, []);

  const fetchSites = async () => {
    try {
      const apiKeyHeader = 'secret'; 
      const url = '/api/2022-04-15/sites'; 
  
      const response = await fetch(url, {
        headers: {
          'X-Voltus-API-Key': apiKeyHeader,
        },
      });
  
      if (response.ok) {
        const data = await response.json();
        setSites(data.sites);
        setFilteredSites(data.sites);
        setError('');
      } else {
        setError('Error fetching sites');
      }
    } catch (error) {
      setError('Error fetching sites');
    }
  };
    
  const handleSortBy = (attribute) => {
    let sortedSites = [...filteredSites];
    sortedSites.sort((a, b) => a[attribute].localeCompare(b[attribute]));
    setFilteredSites(sortedSites);
    setSortBy(attribute);
  };

  const handleFilterBy = (attribute) => {
    if (attribute === 'all') {
      setFilteredSites(sites);
    } else {
      const filtered = sites.filter((site) =>
        site.name.toLowerCase().includes(attribute.toLowerCase()) ||
        site.locationId.toLowerCase().includes(attribute.toLowerCase())
      );
      setFilteredSites(filtered);
    }
    setFilterBy(attribute);
  };

  return (
    <div className="container">
      {/* Render error message if there's an error */}
      {error}
      <h1>Voltus Site List</h1>
      <div className="input-container">
        <label>API Key:</label>
        <input
          type="text"
          value={apiKey}
          onChange={(e) => setApiKey(e.target.value)}
        />
        <button onClick={fetchSites}>Fetch Sites</button>
      </div>
      <div className="filter-container">
        <label>Sort By:</label>
        <select
          value={sortBy}
          onChange={(e) => handleSortBy(e.target.value)}
        >
          <option value="">None</option>
          <option value="name">Name</option>
          <option value="locationId">Location ID</option>
          {/* Add more attributes for sorting */}
        </select>
        <label>Filter By:</label>
        <input
          type="text"
          value={filterBy}
          onChange={(e) => handleFilterBy(e.target.value)}
          placeholder="Enter Name or Location ID"
        />
      </div>
      <table>
        <thead>
          <tr>
            <th>Site Name</th>
            <th>Location ID</th>
            {/* Add more table headers for additional details */}
          </tr>
        </thead>
        <tbody>
          {filteredSites.map((site) => (
            <tr key={site.id}>
              <td>{site.name}</td>
              <td>{site.locationId}</td>
              {/* Render more table cells for additional details */}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default SiteList;


