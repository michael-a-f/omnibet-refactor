import React from "react";

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
	let team1ImagePath =
		"../../../img/nba-logos/" + matchup.team_1.full_name + ".png";
	let team2ImagePath =
		"../../../img/nba-logos/" + matchup.team_2.full_name + ".png";

	return (
		<div class="game-card">
			<div class="game-card-header">
				<p>
					{matchup.date} @ {matchup.time}
				</p>
			</div>

			<div class="teams">
				<div class="team">
					<img src={team1ImagePath} alt={matchup.team_1.short_name} />
					<p>{matchup.team_1.full_name}</p>
				</div>
				<div class="divider">
					<p>@</p>
				</div>
				<div class="team">
					<img src={team2ImagePath} alt={matchup.team_2.short_name} />
					<p>{matchup.team_2.full_name}</p>
				</div>
			</div>
			<div class="bets">
				<div class="bet" id="better-bet">
					<div class="title">
						<p>{matchup.team_1.short_name} Win:</p>
					</div>
					<div class="pct">
						<p>{team1WinPct}% Chance</p>
					</div>
					<div class="winning">
						<p>Win: ${team1WinAmt}</p>
					</div>
					<div class="place-bet">
						<button>Add to Cart</button>
					</div>
				</div>
				<div class="bet-divider"></div>

				<div class="bet">
					<div class="title">
						<p>{matchup.team_2.short_name} Win:</p>
					</div>
					<div class="pct">
						<p>{team2WinPct}% Chance</p>
					</div>
					<div class="winning">
						<p>Win: ${team2WinAmt}</p>
					</div>
					<div class="place-bet">
						<button>Add to Cart</button>
					</div>
				</div>
			</div>
		</div>
	);
};

export default MatchupCard;
