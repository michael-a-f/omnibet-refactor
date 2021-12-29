import React from "react";

const BetGrade = ({ betAmount, team, expectedROI }) => {
  let grade;
  if (expectedROI < 4) {
    grade = "Poor";
  } else if (expectedROI >= 4 && expectedROI < 7) {
    grade = "OK";
  } else if (expectedROI >= 7 && expectedROI < 16) {
    grade = "Good";
  } else if (expectedROI >= 16 && expectedROI < 25) {
    grade = "Great";
  } else if (expectedROI >= 25) {
    grade = "Excellent";
  }
  grade = `${grade} bet`;

  return (
    <div className="bet-details d-flex flex-row justify-content-between align-items-center mt-1">
      <p className="mb-0">Exp. ROI: {expectedROI.toFixed(2)}%</p>
      <p className="mb-0">{grade}</p>
      <button className="btn btn-primary btn-sm">
        Bet ${betAmount} on {team.short_name}
      </button>
    </div>
  );
};

export default BetGrade;
