import React from "react";

const Sidebar = ({
	availableSports,
	onFilterSportsToShow,
	datesToShow,
	onFilterDatesToShow,
	betAmount,
	setBetAmount,
}) => {
	return (
		<div className="sidebar">
			<div className="d-flex flex-row justify-content-between align-items-center mb-2">
				<p className="side-header">Bet Amount</p>
				<p id="bet-amount" className="side-header">
					${betAmount}
				</p>
			</div>

			<input
				type="range"
				className="form-range mb-3"
				min="5"
				max="500"
				step="5"
				defaultValue={betAmount}
				onChange={(e) => setBetAmount(parseInt(e.target.value))}
				id="bet-amount-slider"
			></input>
			<hr />
			<p className="side-header">Filter by Sport</p>
			<select
				id="sports-filter"
				className="form-select mb-4"
				aria-label="Default select example"
				onChange={(e) => onFilterSportsToShow(e.target.value)}
			>
				<option key={0} value="all">
					All Sports
				</option>
				{availableSports.map((sport, idx) => (
					<option key={idx + 1} value={sport}>
						{sport.toUpperCase()}
					</option>
				))}
			</select>
			<p className="side-header">Filter by Date</p>
			<select
				id="dates-filter"
				className="form-select mb-4"
				aria-label="Default select example"
				onChange={(e) => onFilterDatesToShow(e.target.value)}
			>
				<option selected value="all">
					All Dates
				</option>
				{["Today", "Future"].map((date, idx) => (
					<option key={idx + 1} value={date}>
						{date}
					</option>
				))}
			</select>
			<hr />
		</div>
	);
};

export default Sidebar;
