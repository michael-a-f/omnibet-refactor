import React from "react";

const SortBar = ({ matchupCount }) => {
	return (
		<div className="d-flex flex-row justify-content-between mb-4">
			<div id="sort-by">
				<select className="form-select" aria-label="Default select example">
					<option selected>Smartest bets first</option>
					<option value="1">Biggest underdogs first</option>
					<option value="2">Biggest favorites first</option>
				</select>
			</div>
			<div id="matchup-count">
				<p>Showing 1-20 out of {matchupCount} games</p>
			</div>
		</div>
	);
};

export default SortBar;
