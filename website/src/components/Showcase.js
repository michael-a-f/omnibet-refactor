import React from "react";

const Showcase = () => {
	return (
		<section id="showcase">
			<div className="container">
				<div className="row justify-content-between align-items-center">
					<div className="col-6">
						<h2>Bet with confidence.</h2>
						<p className="lead">
							We crunch the numbers. ALL of them. So you don't have to.
						</p>
						<p>
							Maybe you are feeling lucky and want to bet the biggest underdogs.
							Or maybe you want to make quick money on the huge favorites. Or
							maybe you want to take the mathematical approach and bet based on
							expected value. Whatever your desire, we make it quick and easy to
							navigate the market.
						</p>
					</div>
					<div className="col-6">
						<img
							className="img-fluid"
							src="../../../img/showcase.png"
							alt="Logo"
						></img>
					</div>
				</div>
				<div className="row justify-content-between align-items-center">
					<div className="col-6">
						<img
							className="img-fluid"
							src="../../../img/odds.png"
							alt="Logo"
						></img>
					</div>
					<div className="col-6">
						<h2>Beat the odds.</h2>
						<p className="lead">
							Ever wish you could game the system? Well now you can.
						</p>
						<p>
							With so many sportsbooks all setting their own odds, there are
							HUGE opportunities to make completely risk-free money. Yup.
							Risk-free. We calculate the combinations of bets you would have to
							place to walk away with a profit regardless of which teams win.
							The concept is called 'arbitrage' and never before has it been so
							easy to capitalize on these market inefficiencies.
						</p>
					</div>
				</div>
			</div>
		</section>
	);
};

export default Showcase;
