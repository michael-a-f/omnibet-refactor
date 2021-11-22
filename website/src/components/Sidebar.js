import React from "react";

const Sidebar = ({ availableSports }) => {
	return (
		<div className="sidebar">
			<h2>Search Games:</h2>
			<select className="form-select" aria-label="Default select example">
				<option selected>All Sports</option>
				{availableSports.map((sport_name, idx) => (
					<option key={idx} value={idx}>
						{sport_name.toUpperCase()}
					</option>
				))}
			</select>
			<select className="form-select" aria-label="Default select example">
				<option selected>All Dates</option>
				<option value="1">Today</option>
				<option value="2">Upcoming</option>
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
