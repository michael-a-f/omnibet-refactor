import React from "react";
import MatchupCard from "./MatchupCard";

const MatchupGrid = ({ matchups, betAmount }) => {
  return (
    <div className="matchup-grid">
      {matchups.map((matchup, idx) => (
        <MatchupCard
          key={idx}
          matchup={matchup}
          betAmount={betAmount}
        ></MatchupCard>
      ))}
    </div>
  );
};

export default MatchupGrid;
