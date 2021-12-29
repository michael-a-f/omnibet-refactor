import React from "react";

const Sidebar = ({ availableSports, onFilterMatchups }) => {
  return (
    <div className="sidebar">
      <h2>Search Games:</h2>
      <select
        id="sports-filter"
        className="form-select"
        aria-label="Default select example"
        onChange={(e) => onFilterMatchups(e.target)}
      >
        <option selected value="all">
          All Sports
        </option>
        {availableSports.map((sport_name, idx) => (
          <option key={idx} value={sport_name}>
            {sport_name.toUpperCase()}
          </option>
        ))}
      </select>
      <select
        id="dates-filter"
        className="form-select"
        aria-label="Default select example"
        onChange={(e) => onFilterMatchups(e.target)}
      >
        <option selected value="all">
          All Dates
        </option>
        <option value="today">Today</option>
        <option value="future">Upcoming</option>
      </select>
      <label htmlFor="bet-amount-slider" className="form-label">
        Bet Amount
      </label>
      <input
        type="range"
        className="form-range"
        min="0"
        max="5"
        step="0.5"
        id="bet-amount-slider"
      ></input>
    </div>
  );
};

export default Sidebar;
