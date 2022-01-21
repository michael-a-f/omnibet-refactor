import React, { useEffect } from "react";
import BetGrade from "./BetGrade";
import TeamBet from "./TeamBet";
import { useState } from "react";

const MatchupCard = ({
	matchup,
	betAmount,
	getProfitOnWin,
	getExpectedProfit,
}) => {
	const team_1_expectedProfit = getExpectedProfit(betAmount, matchup.team_1);
	const team_2_expectedProfit = getExpectedProfit(betAmount, matchup.team_2);

	let betterTeamToBet;
	if (team_1_expectedProfit >= team_2_expectedProfit) {
		betterTeamToBet = matchup.team_1;
	} else {
		betterTeamToBet = matchup.team_2;
	}
	// const getBetterTeamToBet = (matchup) => {
	// 	if (team_1_expectedProfit >= team_2_expectedProfit) {
	// 		return matchup.team_1;
	// 	} else {
	// 		return matchup.team_2;
	// 	}
	// };

	// Default selection is the team with highest expected ROI.
	const [selectedTeam, setSelectedTeam] = useState(
		() =>
			// getBetterTeamToBet(matchup)
			betterTeamToBet
	);

	// const profitonWin = getProfitOnWin(betAmount, selectedTeam);
	// const expectedProfit = getExpectedProfit(betAmount, selectedTeam);
	// const profitOnWin = betAmount * (selectedTeam.money_multiplier - 1);
	// const expectedProfit =
	// 	profitOnWin * selectedTeam.win_probability -
	// 	betAmount * (1 - selectedTeam.win_probability);
	const expectedROI =
		(betAmount + getExpectedProfit(betAmount, selectedTeam)) / betAmount - 1;

	// // When matchup changes, recalculate the better team to bet on.
	useEffect(() => {
		// setSelectedTeam(getBetterTeamToBet(matchup));
		setSelectedTeam(betterTeamToBet);
	}, [matchup]);

	const title = `${matchup.sport.toUpperCase()}: ${matchup.team_1.full_name} @ 
  	${matchup.team_2.full_name}`;

	// Convert backend datetime to "Mon, Jan 1 12:00PM" format.
	const datetime = new Date(matchup.datetime);

	// Date
	const months = [
		"Jan",
		"Feb",
		"Mar",
		"Apr",
		"May",
		"Jun",
		"Jul",
		"Aug",
		"Sept",
		"Oct",
		"Nov",
		"Dec",
	];
	const days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
	const month = months[datetime.getMonth()];
	const dayOfWeek = days[datetime.getDay()];
	const dayOfMonth = datetime.getDate();
	const formatted_date = `${dayOfWeek}, ${month} ${dayOfMonth}`;

	// Time
	let hr = datetime.getHours();
	let min = datetime.getMinutes();
	if (min < 10) {
		min = "0" + min;
	}
	let ampm = "AM";
	if (hr > 12) {
		hr -= 12;
		ampm = "PM";
	} else if (hr == 12) {
		ampm = "PM";
	}
	const formatted_time = `${hr}:${min}${ampm}`;

	return (
		<div className="matchup-card d-flex flex-column justify-content-between">
			<div className="matchup-card-header">
				<p className="m-0">{title}</p>
				<p className="matchup-date">
					{formatted_date} {formatted_time}
				</p>
			</div>

			<div className="matchup-card-body">
				{[matchup.team_1, matchup.team_2].map((team, idx) => (
					<TeamBet
						key={idx}
						sport={matchup.sport}
						team={team}
						selectedTeam={selectedTeam}
						profitOnWin={getProfitOnWin(betAmount, team)}
						expectedProfit={getExpectedProfit(betAmount, team)}
						setSelectedTeam={setSelectedTeam}
					></TeamBet>
				))}
			</div>

			<BetGrade
				betAmount={betAmount}
				selectedTeam={selectedTeam}
				expectedROI={expectedROI}
			></BetGrade>
		</div>
	);
};

export default MatchupCard;
