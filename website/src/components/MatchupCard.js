import React, { useEffect } from "react";
import BetGrade from "./BetGrade";
import TeamBet from "./TeamBet";
import { useState } from "react";

const MatchupCard = ({
  matchup,
  betAmount,
  getExpectedProfit,
  getExpectedROI,
  getBetterTeamToBet,
}) => {
  // Default selection is the team with highest expected ROI.
  const [selectedTeam, setSelectedTeam] = useState(() =>
    getBetterTeamToBet(matchup)
  );

  // When matchup changes, recalculate the better team to bet on.
  useEffect(() => {
    setSelectedTeam(getBetterTeamToBet(matchup));
  }, [matchup]);

  const title = `${matchup.sport.toUpperCase()}: ${matchup.team_1.full_name} @ 
  ${matchup.team_2.full_name}`;
  const datetime = `${matchup.date} ${matchup.time}`;

  const betGrade = (ROI) => {
    let grade;
    if (ROI < 4) {
      grade = "Poor";
    } else if (ROI >= 4 && ROI < 7) {
      grade = "OK";
    } else if (ROI >= 7 && ROI < 16) {
      grade = "Good";
    } else if (ROI >= 16 && ROI < 25) {
      grade = "Great";
    } else if (ROI >= 25) {
      grade = "Excellent";
    }
    grade = `${grade} Bet`;
    return grade;
  };
  return (
    <div className="matchup-card d-flex flex-column justify-content-between">
      <div className="matchup-card-header">
        <p className="m-0">{title}</p>
        <p className="matchup-date">{datetime}</p>
      </div>

      <div className="matchup-card-body">
        {[matchup.team_1, matchup.team_2].map((team, idx) => (
          <TeamBet
            key={idx}
            sport={matchup.sport}
            team={team}
            selectedTeam={selectedTeam}
            expectedProfit={getExpectedProfit(team)}
            expectedROI={getExpectedROI(team)}
          ></TeamBet>
        ))}
      </div>

      {/* <BetGrade
        betAmount={betAmount}
        team={selectedTeam}
        expectedProfit={getExpectedProfit(selectedTeam)}
        expectedROI={getExpectedROI(selectedTeam)}
      ></BetGrade> */}
      <div className="bet-details d-flex flex-row justify-content-between align-items-end">
        <div>
          <p className="bet-grade-remark mb-0">
            {betGrade(getExpectedROI(selectedTeam))}
          </p>
          <p className="bet-grade mb-0">
            {getExpectedROI(selectedTeam).toFixed(2)}% ROI
          </p>
        </div>

        <button className="btn btn-primary btn-sm">
          Bet ${betAmount} on {selectedTeam.short_name}
        </button>
      </div>
    </div>
  );
};

export default MatchupCard;
