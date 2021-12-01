import React from "react";

const BetGrade = ({ expectedWinnings, betAmount, teamName }) => {
  return (
    <div className="bet-details d-flex flex-row justify-content-between align-items-center mt-1">
      <p className="mb-0">Exp. Profit: ${expectedWinnings.toFixed(0)}</p>
      <button className="btn btn-primary btn-sm">
        Bet ${betAmount} on {teamName}
      </button>
    </div>
  );
};

export default BetGrade;
