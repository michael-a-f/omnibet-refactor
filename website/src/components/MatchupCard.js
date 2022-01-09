import React, { useEffect } from "react";
import BetGrade from "./BetGrade";
import TeamBet from "./TeamBet";
import { useState } from "react";

const MatchupCard = ({
	matchup,
	betAmount,
	// getProfitOnWin,
	// getExpectedProfit,
	// getBetterTeamToBet,
}) => {
	const getProfitOnWin = (betAmount, team) => {
		return betAmount * (team.money_multiplier - 1);
	};

	const getExpectedProfit = (betAmount, team) => {
		const profitOnWin = getProfitOnWin(betAmount, team);
		return (
			profitOnWin * team.win_probability -
			betAmount * (1 - team.win_probability)
		);
	};

	const getBetterTeamToBet = (matchup) => {
		if (
			getExpectedProfit(betAmount, matchup.team_1) >=
			getExpectedProfit(betAmount, matchup.team_2)
		) {
			return matchup.team_1;
		} else {
			return matchup.team_2;
		}
	};
	// Default selection is the team with highest expected ROI.
	const [selectedTeam, setSelectedTeam] = useState(() =>
		getBetterTeamToBet(matchup)
	);

	// const profitonWin = getProfitOnWin(betAmount, selectedTeam);
	// const expectedProfit = getExpectedProfit(betAmount, selectedTeam);
	const profitOnWin = betAmount * (selectedTeam.money_multiplier - 1);
	const expectedProfit =
		profitOnWin * selectedTeam.win_probability -
		betAmount * (1 - selectedTeam.win_probability);
	const expectedROI = (betAmount + expectedProfit) / betAmount - 1;

	// const expectedROI = betAmount + expectedProfit;
	const getExpectedROI = (betAmount, team) => {
		const expectedReturn = getExpectedProfit(betAmount, team);
		return (betAmount + expectedReturn) / betAmount - 1;
	};

	// When matchup changes, recalculate the better team to bet on.
	useEffect(() => {
		setSelectedTeam(getBetterTeamToBet(matchup));
	}, [matchup]);

	// When the selected bet changes, compute its expected ROI to use
	// in grading the bet.
	let selectedTeamsExpectedROI = getExpectedROI(betAmount, selectedTeam);
	// useEffect(() => {
	// 	selectedTeamsExpectedROI = getExpectedROI(betAmount, selectedTeam);
	// }, [selectedTeam]);

	const title = `${matchup.sport.toUpperCase()}: ${matchup.team_1.full_name} @ 
  	${matchup.team_2.full_name}`;

	// Convert backend datetime to "Mon, Jan 1 12:00PM" format.
	const datetime = new Date(matchup.datetime);
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
	const shortMonth = months[datetime.getMonth()];
	const dayOfWeek = days[datetime.getDay()];
	const dayNumber = datetime.getDate();
	let hr = datetime.getHours();
	let min = datetime.getMinutes();
	if (min < 10) {
		min = "0" + min;
	}
	let ampm = "AM";
	if (hr > 12) {
		hr -= 12;
		ampm = "PM";
	}
	const formatted_date = `${dayOfWeek}, ${shortMonth} ${dayNumber}`;
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
