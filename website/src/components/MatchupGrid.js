import React from "react";
import MatchupCard from "./MatchupCard";

const MatchupGrid = ({ matchups, betAmount }) => {
	return (
		<div className="d-flex flex-row flex-wrap justify-content-between align-items-center">
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
