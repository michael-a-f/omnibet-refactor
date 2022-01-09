import React from "react";
import { useState, useEffect } from "react";

const Sidebar = ({
	availableSports,
	onFilterMatchups,
	betAmount,
	setBetAmount,
}) => {
	const [sliderValue, setSliderValue] = useState(25);
	return (
		<div className="sidebar">
			<p>Filter by Sport</p>
			<select
				id="sports-filter"
				className="form-select mb-4"
				aria-label="Default select example"
				onChange={(e) => onFilterMatchups(e.target)}
			>
				<option key={0} value="all">
					All Sports
				</option>
				{availableSports.map((sport_name, idx) => (
					<option key={idx + 1} value={sport_name}>
						{sport_name.toUpperCase()}
					</option>
				))}
			</select>
			<p>Filter by Date</p>
			<select
				id="dates-filter"
				className="form-select"
				aria-label="Default select example"
				onChange={(e) => onFilterMatchups(e.target)}
			>
				<option selected value="all">
					All Dates
				</option>
				<option value="today">Today Only</option>
			</select>

			<div className="d-flex flex-row justify-content-between align-items-center mt-5">
				<p>Bet Amount</p>
				<p>${betAmount}</p>
			</div>

			<input
				type="range"
				className="form-range"
				min="5"
				max="500"
				step="5"
				defaultValue={betAmount}
				onChange={(e) => setBetAmount(parseInt(e.target.value))}
				id="bet-amount-slider"
			></input>
		</div>
	);
};

export default Sidebar;
