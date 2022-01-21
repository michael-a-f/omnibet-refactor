import React from "react";

const SortBar = ({ setSortMatchupsBy }) => {
	return (
		<div>
			<select
				id="sort-by"
				className="form-select"
				aria-label="Default select example"
				onChange={(e) => setSortMatchupsBy(e.target.value)}
			>
				<option selected value="smartest">
					Smartest bets first
				</option>
				<option value="soonest">Soonest games first</option>
				<option value="farthest">Soonest games last</option>
			</select>
		</div>
	);
};

export default SortBar;
