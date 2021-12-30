import React from "react";
import MatchupCard from "./MatchupCard";

const MatchupGrid = ({ matchups, betAmount, matchupFilters }) => {
	// Get the profit ($ amount) of a team's best bet if that bet wins.
	const getProfitOnWin = (team) => {
		let money_multiplier = team.money_multiplier;
		if (!money_multiplier) {
			money_multiplier = 0;
		}
		const prizeOnWin = betAmount * money_multiplier;
		const profitOnWin = prizeOnWin - betAmount;
		return profitOnWin;
	};

	// Get the expected profit ($ amount) of a team's bet.
	const getExpectedProfit = (team) => {
		const profitIfWin = getProfitOnWin(team);
		const expectedProfit =
			profitIfWin * team.win_probability -
			betAmount * (1 - team.win_probability);
		return expectedProfit;
	};

	// Get the expected ROI of a team's best bet.
	const getExpectedROI = (team) => {
		return (betAmount + getExpectedProfit(team)) / betAmount - 1;

		// let moneyMultiplier = team.money_multiplier;
		// if (!moneyMultiplier) {
		// 	moneyMultiplier = 0;
		// } else {
		// 	moneyMultiplier = moneyMultiplier;
		// }
		// DEBUGGING
		// const teamName = team.full_name;
		// const prizeOnWin = team.money_multiplier * betAmount;
		// const profitOnWin = getProfitOnWin(team);
		// let winProbability = team.win_probability;
		// if (!winProbability) {
		// 	winProbability = 0;
		// } else {
		// 	winProbability = winProbability;
		// }
		// const profitOnLoss = -betAmount;
		// const expectedProfitCoded = getExpectedProfit(team);
		// const expectedProfitManual =
		// 	profitOnWin * winProbability + profitOnLoss * (1 - winProbability);

		// console.log(`Team: ${teamName}`);
		// console.log(`Money Multiplier: ${moneyMultiplier}`);
		// console.log(`Prize On Win: $${prizeOnWin}`);
		// console.log(`Profit On Win: $${profitOnWin}`);
		// console.log(`Win Probability: ${winProbability}`);
		// console.log(`Profit on Loss: $${-betAmount}`);
		// console.log(`Expected Profit Code: $${expectedProfitCoded}`);
		// console.log(`Expected Profit Manual: $${expectedProfitManual}`);
		// console.log("");
	};

	// Return the team object for the better team to bet on in a matchup.
	const getBetterTeamToBet = (matchup) => {
		if (
			getExpectedProfit(matchup.team_1) >= getExpectedProfit(matchup.team_2)
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
					return matchupFilters.sports.includes(matchup.sport);
					// && matchupFilters.dates.includes(matchup.date)
				})
				.sort((matchA, matchB) => {
					return (
						Math.max(
							getExpectedProfit(matchB.team_1),
							getExpectedProfit(matchB.team_2)
						) -
						Math.max(
							getExpectedProfit(matchA.team_1),
							getExpectedProfit(matchA.team_2)
						)
					);
				})
				.map((matchup, idx) => (
					<MatchupCard
						key={idx}
						matchup={matchup}
						betAmount={betAmount}
						getProfitOnWin={getProfitOnWin}
						getExpectedProfit={getExpectedProfit}
						getExpectedROI={getExpectedROI}
						getBetterTeamToBet={getBetterTeamToBet}
					></MatchupCard>
				))}
		</div>
	);
};

export default MatchupGrid;
