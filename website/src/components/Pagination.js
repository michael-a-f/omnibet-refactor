import React from "react";

const Pagination = ({
	matchupsPerPage,
	totalMatchups,
	setCurrentPage,
	indexOfFirstMatchup,
	indexOfLastMatchup,
}) => {
	const pageNumbers = [];

	for (let i = 1; i <= Math.ceil(totalMatchups / matchupsPerPage); i++) {
		pageNumbers.push(i);
	}

	return (
		<div className="d-flex flex-row justify-content-center align-items-center">
			<p className="mx-3 mb-0">
				Showing {indexOfFirstMatchup + 1} -{" "}
				{Math.min(indexOfLastMatchup, totalMatchups)} out of {totalMatchups}{" "}
				matchups
			</p>
			<nav>
				<ul className="pagination mb-0">
					{pageNumbers.map((number) => (
						<li key={number} className="page-item">
							<button
								onClick={(e) => setCurrentPage(number)}
								className="page-link"
							>
								{number}
							</button>
						</li>
					))}
				</ul>
			</nav>
		</div>
	);
};

export default Pagination;
