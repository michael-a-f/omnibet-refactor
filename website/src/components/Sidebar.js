import React from "react";

const Sidebar = () => {
	return (
		<div className="sidebar">
			<h2>Search Games:</h2>
			<select class="form-select" aria-label="Default select example">
				<option selected>All Sports</option>
				<option value="1">MLB</option>
				<option value="2">NBA</option>
				<option value="3">NHL</option>
				<option value="4">NFL</option>
				<option value="5">NCAA Football</option>
				<option value="6">Boxing</option>
				<option value="7">UFC</option>
				<option value="8">Tennis</option>
				<option value="9">eSports</option>
			</select>
			<select class="form-select" aria-label="Default select example">
				<option selected>All Dates</option>
				<option value="1">Today</option>
				<option value="2">Upcoming</option>
			</select>
			<label for="bet-amount-slider" class="form-label">
				Bet Amount
			</label>
			<input
				type="range"
				class="form-range"
				min="0"
				max="5"
				step="0.5"
				id="bet-amount-slider"
			></input>
		</div>
	);
};

export default Sidebar;
