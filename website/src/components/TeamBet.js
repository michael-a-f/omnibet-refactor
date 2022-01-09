import React from "react";

const TeamBet = ({
	sport,
	team,
	selectedTeam,
	profitOnWin,
	setSelectedTeam,
}) => {
	// Modify logo filepath for sports without team-specific logos.
	if (["boxing", "ufc", "ncaaf", "ncaab"].includes(sport)) {
		team.logo = `../../../img/${sport}.png`;
	}

	const winProbability = (100 * team.win_probability).toFixed(0);

	return (
		<div
			className={
				team === selectedTeam
					? "selected bet row align-items-center"
					: "bet row align-items-center"
			}
			onClick={() => setSelectedTeam(team)}
		>
			<div className="col text-center">
				<img
					className="team-logo img-fluid"
					src={team.logo}
					alt={team.full_name}
					style={{ width: "4.5rem" }}
				/>
			</div>
			<div className="col text-center">
				<p className="m-0">{winProbability}%</p>
				<p className="m-0">Chance</p>
			</div>
			<div className="col text-center">
				<p className="m-0">${profitOnWin.toFixed(0)}</p>
				<p className="m-0">To Win</p>
			</div>
		</div>
	);
};

export default TeamBet;
