import React from "react";
import MatchupCard from "./MatchupCard";

const MatchupGrid = ({ matchups, betAmount, matchupFilters }) => {
	// Get the profit ($ amount) of a team's best bet if that bet wins.
	const getProfitOnWin = (betAmount, team) => {
		return betAmount * (team.money_multiplier - 1);
	};

	// Get the expected profit ($ amount) of a team's bet.
	const getExpectedProfit = (betAmount, team) => {
		const profitIfWin = getProfitOnWin(betAmount, team);
		const expectedProfit =
			profitIfWin * team.win_probability -
			betAmount * (1 - team.win_probability);
		return expectedProfit;
	};

	// // Get the expected ROI of a team's best bet.
	// const getExpectedROI = (betAmount, team) => {
	// 	const expectedReturn = getExpectedProfit(betAmount, team);
	// 	return (betAmount + expectedReturn) / betAmount - 1;

	// 	// let moneyMultiplier = team.money_multiplier;
	// 	// if (!moneyMultiplier) {
	// 	// 	moneyMultiplier = 0;
	// 	// } else {
	// 	// 	moneyMultiplier = moneyMultiplier;
	// 	// }
	// 	// DEBUGGING
	// 	// const teamName = team.full_name;
	// 	// const prizeOnWin = team.money_multiplier * betAmount;
	// 	// const profitOnWin = getProfitOnWin(team);
	// 	// let winProbability = team.win_probability;
	// 	// if (!winProbability) {
	// 	// 	winProbability = 0;
	// 	// } else {
	// 	// 	winProbability = winProbability;
	// 	// }
	// 	// const profitOnLoss = -betAmount;
	// 	// const expectedProfitCoded = getExpectedProfit(team);
	// 	// const expectedProfitManual =
	// 	// 	profitOnWin * winProbability + profitOnLoss * (1 - winProbability);

	// 	// console.log(`Team: ${teamName}`);
	// 	// console.log(`Money Multiplier: ${moneyMultiplier}`);
	// 	// console.log(`Prize On Win: $${prizeOnWin}`);
	// 	// console.log(`Profit On Win: $${profitOnWin}`);
	// 	// console.log(`Win Probability: ${winProbability}`);
	// 	// console.log(`Profit on Loss: $${-betAmount}`);
	// 	// console.log(`Expected Profit Code: $${expectedProfitCoded}`);
	// 	// console.log(`Expected Profit Manual: $${expectedProfitManual}`);
	// 	// console.log("");
	// };

	const isToday = (someDate) => {
		const today = new Date();
		return (
			someDate.getDate() == today.getDate() &&
			someDate.getMonth() == today.getMonth() &&
			someDate.getFullYear() == today.getFullYear()
		);
	};

	const filterByDate = (matchup) => {
		if (matchupFilters.dates.includes("all")) {
			return true;
		} else {
			const isGameToday = isToday(new Date(matchup.datetime));
			return isGameToday;
		}
	};

	// Return the team object for the better team to bet on in a matchup.
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

	return (
		<div className="matchup-grid">
			{matchups
				.filter((matchup) => {
					return (
						matchupFilters.sports.includes(matchup.sport) &&
						filterByDate(matchup)
					);
				})
				.sort((matchA, matchB) => {
					if (matchupFilters.sort_by == "soonest") {
						return new Date(matchA.datetime) - new Date(matchB.datetime);
					} else if (matchupFilters.sort_by == "farthest") {
						return new Date(matchB.datetime) - new Date(matchA.datetime);
					} else if (matchupFilters.sort_by == "smartest") {
						return (
							Math.max(
								getExpectedProfit(betAmount, matchB.team_1),
								getExpectedProfit(betAmount, matchB.team_2)
							) -
							Math.max(
								getExpectedProfit(betAmount, matchA.team_1),
								getExpectedProfit(betAmount, matchA.team_2)
							)
						);
					}
				})
				.map((matchup, idx) => (
					<MatchupCard
						key={idx}
						matchup={matchup}
						betAmount={betAmount}
						// getProfitOnWin={getProfitOnWin}
						// getExpectedProfit={getExpectedProfit}
						// // getExpectedROI={getExpectedROI}
						// getBetterTeamToBet={getBetterTeamToBet}
					></MatchupCard>
				))}
		</div>
	);
};

export default MatchupGrid;
