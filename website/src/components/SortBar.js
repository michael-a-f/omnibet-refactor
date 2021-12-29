import React from "react";

const SortBar = ({ matchupCount, onFilterSports }) => {
  return (
    <div className="d-flex flex-row justify-content-between mb-4">
      <div id="sort-by">
        <select
          id="sort-by"
          className="form-select"
          aria-label="Default select example"
          onChange={(e) => onFilterSports(e.target)}
        >
          <option selected value="smartest">
            Smartest bets first
          </option>
          <option value="underdogs">Biggest underdogs first</option>
          <option value="favorites">Biggest favorites first</option>
        </select>
      </div>
      <div id="matchup-count">
        <p>Showing 1-20 out of {matchupCount} games</p>
      </div>
    </div>
  );
};

export default SortBar;
