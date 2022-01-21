import React from "react";
import Sidebar from "./Sidebar";
import { useState, useEffect } from "react";
import ContentArea from "./ContentArea";

const OmniBet = ({ availableSports, unfilteredMatchups }) => {
	const [sportsToShow, setSportsToShow] = useState([...availableSports]);
	const [datesToShow, setDatesToShow] = useState(["Today", "Future"]);
	const [betAmount, setBetAmount] = useState(200);
	// const [filteredMatchups, setFilteredMatchups] = useState(unfilteredMatchups);

	const onFilterSportsToShow = (selection) => {
		if (selection === "all") {
			setSportsToShow([...availableSports]);
		} else {
			setSportsToShow([selection]);
		}
	};

	const onFilterDatesToShow = (selection) => {
		if (selection === "all") {
			setDatesToShow(["Today", "Future"]);
		} else {
			setDatesToShow([selection]);
		}
	};

	const isTodayOrPast = (someDate) => {
		const today = new Date();
		return (
			someDate.getDate() <= today.getDate() &&
			someDate.getMonth() <= today.getMonth() &&
			someDate.getFullYear() <= today.getFullYear()
		);
	};

	const DateFilterHelper = (matchup) => {
		const isGameTodayOrPast = isTodayOrPast(new Date(matchup.datetime));
		const isGameInFuture = !isGameTodayOrPast;

		if (!datesToShow.includes("Today")) {
			// If filter doesn't include today, only show future matchups
			return isGameInFuture;
		} else if (!datesToShow.includes("Future")) {
			// If filter doesn't include future, only show today
			return isGameTodayOrPast;
		} else {
			// Filter includes both Today and Future, so show all
			return true;
		}
	};

	const filteredMatchups = unfilteredMatchups.filter((matchup) => {
		return sportsToShow.includes(matchup.sport) && DateFilterHelper(matchup);
	});

	return (
		<section id="main-content">
			<div className="container py-5">
				<div className="row">
					<div className="col-xl-3 pb-4">
						<Sidebar
							availableSports={availableSports}
							onFilterSportsToShow={onFilterSportsToShow}
							datesToShow={datesToShow}
							onFilterDatesToShow={onFilterDatesToShow}
							betAmount={betAmount}
							setBetAmount={setBetAmount}
						/>
					</div>
					<div className="col-xl-9">
						<ContentArea
							filteredMatchups={filteredMatchups}
							betAmount={betAmount}
						/>
					</div>
				</div>
			</div>
		</section>
	);
};

export default OmniBet;
