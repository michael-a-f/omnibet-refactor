import React from "react";

const Boxes = () => {
	return (
		<section id="info-boxes" className="bg-dark p-4">
			<div className="container">
				<div className="row text-center g-4">
					<div className="col-md">
						<div className="card bg-dark text-light pb-4">
							<div className="card-body text-center">
								<div className="h1 mb-3">
									<i className="bi bi-laptop"></i>
								</div>
								<h3 className="card-title mb-3">
									User Focused
								</h3>
								<p className="card-text">
									OmniBet makes it quick and easy to browse
									and filter through all kinds of bets.
								</p>
							</div>
						</div>
					</div>
					<div className="col-md">
						<div className="card bg-dark text-light pb-4">
							<div className="card-body text-center">
								<div className="h1 mb-3">
									<i className="bi bi-person-square"></i>
								</div>
								<h3 className="card-title mb-3">Math-Driven</h3>
								<p className="card-text">
									We 'rank' bets so that you can understand
									when a bet is better than another.
								</p>
							</div>
						</div>
					</div>
					<div className="col-md">
						<div className="card bg-dark text-light pb-4">
							<div className="card-body text-center">
								<div className="h1 mb-3">
									<i className="bi bi-people"></i>
								</div>
								<h3 className="card-title mb-3">
									Whole Market
								</h3>
								<p className="card-text">
									We scrape odds from 7 major sportsbooks so
									that you can be sure your bet is the best.
								</p>
							</div>
						</div>
					</div>
				</div>
			</div>
		</section>
	);
};

export default Boxes;
