import React from "react";
import { useState } from "react";
import MatchupGrid from "./MatchupGrid";
import SortBar from "./SortBar";
import Pagination from "./Pagination";

const ContentArea = ({ filteredMatchups, betAmount }) => {
	const [sortMatchupsBy, setSortMatchupsBy] = useState("smartest");
	const [currentPage, setCurrentPage] = useState(1);
	const [matchupsPerPage] = useState(15);

	// Indices to slice matchups with for pagination.
	const indexOfLastMatchup = currentPage * matchupsPerPage;
	const indexOfFirstMatchup = indexOfLastMatchup - matchupsPerPage;

	return (
		<>
			<div className="d-flex flex-row justify-content-between align-content-center mb-4">
				<SortBar setSortMatchupsBy={setSortMatchupsBy} />
				<Pagination
					matchupsPerPage={matchupsPerPage}
					totalMatchups={filteredMatchups.length}
					setCurrentPage={setCurrentPage}
					indexOfFirstMatchup={indexOfFirstMatchup}
					indexOfLastMatchup={indexOfLastMatchup}
				/>
			</div>
			<MatchupGrid
				filteredMatchups={filteredMatchups}
				indexOfFirstMatchup={indexOfFirstMatchup}
				indexOfLastMatchup={indexOfLastMatchup}
				sortMatchupsBy={sortMatchupsBy}
				betAmount={betAmount}
			/>
		</>
	);
};

export default ContentArea;
