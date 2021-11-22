import React from "react";
import TeamBet from "./TeamBet";

const MatchupCard = ({ matchup }) => {
	let mm1 = matchup.team_1.money_multiplier;
	let mm2 = matchup.team_2.money_multiplier;
	if (mm1 == null) {
		mm1 = 0;
	}
	if (mm2 == null) {
		mm2 = 0;
	}

	let betAmount = 200;
	let team1WinAmt = (betAmount * mm1).toFixed(0) - betAmount;
	let team2WinAmt = (betAmount * mm2).toFixed(0) - betAmount;

	let team1ExpVal = (
		team1WinAmt * matchup.team_1.win_probability -
		betAmount * (1 - matchup.team_1.win_probability)
	).toFixed(0);
	let team2ExpVal = (
		team2WinAmt * matchup.team_2.win_probability -
		betAmount * (1 - matchup.team_2.win_probability)
	).toFixed(0);

	let team1WinPct = (matchup.team_1.win_probability * 100).toFixed(0);
	let team2WinPct = (matchup.team_2.win_probability * 100).toFixed(0);

	if (["boxing", "ufc", "ncaaf", "ncaab"].includes(matchup.sport)) {
		matchup.team_1.logo = `../../../img/${matchup.sport}.png`;
		matchup.team_2.logo = `../../../img/${matchup.sport}.png`;
	}
	return (
		<div className="matchup-card mb-4">
			<div className="matchup-card-header">
				<p>
					{matchup.date} @ {matchup.time}
				</p>
			</div>
			<div className="bets d-flex flex-column justify-content-between">
				{[matchup.team_1, matchup.team_2].map((team, idx) => (
					<TeamBet
						key={idx}
						sport={matchup.sport}
						team={team}
						betAmount={betAmount}
					></TeamBet>
				))}
			</div>

			<div className="bet-details d-flex flex-row justify-content-between align-items-center">
				<p className="mb-0">Great Bet!</p>
				<button className="btn btn-primary btn-sm">
					Bet ${betAmount} on {matchup.team_1.short_name}
				</button>
			</div>
		</div>
	);
};

export default MatchupCard;
