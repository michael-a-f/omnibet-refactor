import React from "react";
import MatchupCard from "./MatchupCard";

const MatchupGrid = ({ matchups, betAmount, matchupFilters }) => {
  // Get the expected profit of a team's best bet.
  const getExpectedProfit = (team) => {
    let money_multiplier = team.money_multiplier;
    if (!money_multiplier) {
      money_multiplier = 0;
    }
    const prizeOnWin = betAmount * money_multiplier;
    const profitOnWin = prizeOnWin - betAmount;
    const expectedProfit =
      profitOnWin * team.win_probability -
      betAmount * (1 - team.win_probability);
    return expectedProfit;
  };

  // Get the expected ROI of a team's best bet.
  const getExpectedROI = (team) => {
    const expectedROI =
      100 * ((betAmount + getExpectedProfit(team)) / betAmount - 1);
    return expectedROI;
  };

  // Return the team object for the better team to bet on in a matchup.
  const getBetterTeamToBet = (matchup) => {
    if (getExpectedROI(matchup.team_1) >= getExpectedROI(matchup.team_2)) {
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
              getExpectedROI(matchB.team_1),
              getExpectedROI(matchB.team_2)
            ) -
            Math.max(
              getExpectedROI(matchA.team_1),
              getExpectedROI(matchA.team_2)
            )
          );
        })
        .map((matchup, idx) => (
          <MatchupCard
            key={idx}
            matchup={matchup}
            betAmount={betAmount}
            getExpectedProfit={getExpectedProfit}
            getExpectedROI={getExpectedROI}
            getBetterTeamToBet={getBetterTeamToBet}
          ></MatchupCard>
        ))}
    </div>
  );
};

export default MatchupGrid;
