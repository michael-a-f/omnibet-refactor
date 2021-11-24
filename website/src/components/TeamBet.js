import React from "react";

const TeamBet = ({ sport, team, betAmount }) => {
	// Modify logo filepath for sports without team-specific logos.
	if (["boxing", "ufc", "ncaaf", "ncaab"].includes(sport)) {
		team.logo = `../../../img/${sport}.png`;
	}

	// None check for sake of using in calculations.
	let moneyMultiplier = team.money_multiplier;
	if (moneyMultiplier == null) {
		moneyMultiplier = 0;
	}

	const winAmount = (betAmount * moneyMultiplier).toFixed(0) - betAmount;
	const winProbability = (100 * team.win_probability).toFixed(0);
	const expectedValue =
		winAmount * team.win_probability - betAmount * (1 - team.win_probability);
	const expectedReturn = 100 * ((betAmount + expectedValue) / betAmount - 1);
	return (
		<div className="bet row align-items-center">
			<div className="col text-center">
				<p className="m-0">{team.short_name}</p>
			</div>
			<div className="col text-center">
				<img
					className="img-fluid"
					src={team.logo}
					alt={team.full_name}
					style={{ width: "5rem" }}
				/>
			</div>
			<div className="col text-center">
				<p className="m-0">{winProbability}%</p>
				<p className="m-0">Chance:</p>
			</div>
			<div className="col text-center" id="middle">
				<p className="m-0">${winAmount}</p>
				<p className="m-0">To Win:</p>
			</div>
			<div className="col text-center">
				<p className="m-0">{expectedReturn.toFixed(2)}%</p>
				<p className="m-0">ROI:</p>
			</div>
		</div>
	);
};

export default TeamBet;
