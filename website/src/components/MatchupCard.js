import React from "react";
import BetGrade from "./BetGrade";
import TeamBet from "./TeamBet";
import { useState } from "react";

const MatchupCard = ({ matchup, betAmount }) => {
  const teams = [matchup.team_1, matchup.team_2];

  // Calculate the expected return from the best bet.
  const getExpectedReturn = (team) => {
    // None check for sake of using in calculations.
    let moneyMultiplier = team.money_multiplier;
    if (moneyMultiplier == null) {
      moneyMultiplier = 0;
    }

    const winAmount = betAmount * moneyMultiplier - betAmount;

    const expectedValue =
      winAmount * team.win_probability - betAmount * (1 - team.win_probability);
    const expectedReturn = 100 * ((betAmount + expectedValue) / betAmount - 1);

    return expectedReturn;
  };

  const getExpectedWinnings = (team) => {
    // None check for sake of using in calculations.
    let moneyMultiplier = team.money_multiplier;
    if (moneyMultiplier == null) {
      moneyMultiplier = 0;
    }

    const winAmount = betAmount * moneyMultiplier - betAmount;

    const expectedValue =
      winAmount * team.win_probability - betAmount * (1 - team.win_probability);

    return expectedValue;
  };

  teams[0]["expected_return"] = getExpectedReturn(teams[0]);
  teams[1]["expected_return"] = getExpectedReturn(teams[1]);

  // State variables
  const [selectedTeam, setSelectedTeam] = useState(matchup.team_1);

  return (
    <div className="matchup-card">
      <p className="matchup-card-header m-0">
        {matchup.sport.toUpperCase()}: {matchup.team_1.full_name} @{" "}
        {matchup.team_2.full_name}
      </p>
      {/* <p className="matchup-card-header m-0">
        {matchup.date} {matchup.time}
      </p> */}

      <div className="card-body d-flex flex-column justify-content-between">
        {teams.map((team, idx) => (
          <TeamBet
            key={idx}
            sport={matchup.sport}
            team={team}
            betAmount={betAmount}
          ></TeamBet>
        ))}
      </div>

      <BetGrade
        expectedWinnings={getExpectedWinnings(selectedTeam)}
        betAmount={betAmount}
        teamName={selectedTeam.short_name}
      ></BetGrade>
    </div>
  );
};

export default MatchupCard;
