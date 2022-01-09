import React from "react";

const SortBar = ({ matchupCount, onFilterMatchups }) => {
	return (
		<div className="d-flex flex-row justify-content-between mb-4">
			<div>
				<select
					id="sort-by"
					className="form-select"
					aria-label="Default select example"
					onChange={(e) => onFilterMatchups(e.target)}
				>
					<option selected value="smartest">
						Smartest bets first
					</option>
					<option value="soonest">Soonest games first</option>
					<option value="farthest">Soonest games last</option>
				</select>
			</div>
			<div id="matchup-count">
				<p>Showing 1-20 out of {matchupCount} games</p>
			</div>
		</div>
	);
};

export default SortBar;
