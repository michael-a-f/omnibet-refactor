import React from "react";

const TeamBet = ({ sport, team, betAmount }) => {
	if (["boxing", "ufc", "ncaaf", "ncaab"].includes(sport)) {
		team.logo = `../../../img/${sport}.png`;
	}

	let moneyMultiplier = team.money_multiplier;
	if (moneyMultiplier == null) {
		moneyMultiplier = 0;
	}

	const winAmount = (betAmount * moneyMultiplier).toFixed(0) - betAmount;

	return (
		<div className="bet d-flex flex-row justify-content-around align-items-center text-center">
			<img
				className="img-fluid"
				src={team.logo}
				alt={team.full_name}
				style={{ width: "5rem" }}
			/>
			<p className="m-0">{(100 * team.win_probability).toFixed(0)}%</p>
			<p className="m-0">${winAmount}</p>
		</div>
	);
};

export default TeamBet;
