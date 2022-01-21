import React from "react";
import MatchupCard from "./MatchupCard";

const MatchupGrid = ({
	filteredMatchups,
	indexOfFirstMatchup,
	indexOfLastMatchup,
	sortMatchupsBy,
	betAmount,
}) => {
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

	// Return the team object for the better team to bet on in a matchup.
	// const getBetterTeamToBet = (betAmount, matchup) => {
	// 	if (
	// 		getExpectedProfit(betAmount, matchup.team_1) >=
	// 		getExpectedProfit(betAmount, matchup.team_2)
	// 	) {
	// 		return matchup.team_1;
	// 	} else {
	// 		return matchup.team_2;
	// 	}
	// };

	// Smarter of two matchups is the one with the best possible bet.
	// Soonest and farthest are date-driven.
	const sortedAndFilteredMatchups = filteredMatchups.sort(
		(matchupA, matchupB) => {
			if (sortMatchupsBy === "smartest") {
				return (
					Math.max(
						getExpectedProfit(betAmount, matchupB.team_1),
						getExpectedProfit(betAmount, matchupB.team_2)
					) -
					Math.max(
						getExpectedProfit(betAmount, matchupA.team_1),
						getExpectedProfit(betAmount, matchupA.team_2)
					)
				);
			} else if (sortMatchupsBy === "soonest") {
				return new Date(matchupA.datetime) - new Date(matchupB.datetime);
			} else if (sortMatchupsBy === "farthest") {
				return new Date(matchupB.datetime) - new Date(matchupA.datetime);
			}
		}
	);

	const paginatedMatchups = sortedAndFilteredMatchups.slice(
		indexOfFirstMatchup,
		indexOfLastMatchup
	);

	return (
		<div className="matchup-grid">
			{paginatedMatchups.map((matchup, idx) => (
				<MatchupCard
					key={idx}
					matchup={matchup}
					betAmount={betAmount}
					getProfitOnWin={getProfitOnWin}
					getExpectedProfit={getExpectedProfit}
					// // getExpectedROI={getExpectedROI}
					// getBetterTeamToBet={getBetterTeamToBet}
				></MatchupCard>
			))}
		</div>
	);
};

export default MatchupGrid;
