import React from "react";

const Showcase = () => {
	return (
		<section className="bg-primary text-light p-5 p-lg-0 pt-lg-5 text-center text-sm-start">
			<div className="container">
				<div className="d-sm-flex align-items-center justify-content-between">
					<div>
						<h1>Bet with confidence.</h1>
						<p className="lead my-4">
							We crunch the numbers. ALL of them. So you don't have to.
						</p>
						{/* <p className="my-4">
							Maybe you are feeling lucky and want to bet the biggest underdogs.
							Or maybe you want to make quick money on the huge favorites. Or
							maybe you want to take the mathematical approach and bet based on
							expected value. Whatever your desire, we make it quick and easy to
							navigate the market.
						</p>
						<button
							className="btn btn-primary btn-lg"
							data-bs-toggle="modal"
							data-bs-target="#enroll"
						>
							See the work!
						</button> */}
					</div>
					<img
						className="img-fluid d-none d-sm-block"
						id="showcase-img"
						src="../../../img/showcase.png"
						alt="Showcase Image"
					/>
				</div>
			</div>
		</section>
		//

		// <section id="showcase">
		// 	<div classNameName="container">
		// 		<div classNameName="row justify-content-between align-items-center">
		// 			<div classNameName="col-6">
		// 				<h2>Bet with confidence.</h2>
		// 				<p classNameName="lead">
		// 					We crunch the numbers. ALL of them. So you don't have to.
		// 				</p>
		// 				<p>
		// 					Maybe you are feeling lucky and want to bet the biggest underdogs.
		// 					Or maybe you want to make quick money on the huge favorites. Or
		// 					maybe you want to take the mathematical approach and bet based on
		// 					expected value. Whatever your desire, we make it quick and easy to
		// 					navigate the market.
		// 				</p>
		// 			</div>
		// 			<div classNameName="col-6">
		// 				<img
		// 					classNameName="img-fluid"
		// 					src="../../../img/showcase.png"
		// 					alt="Logo"
		// 				></img>
		// 			</div>
		// 		</div>
		// 		<div classNameName="row justify-content-between align-items-center">
		// 			<div classNameName="col-6">
		// 				<img
		// 					classNameName="img-fluid"
		// 					src="../../../img/odds.png"
		// 					alt="Logo"
		// 				></img>
		// 			</div>
		// 			<div classNameName="col-6">
		// 				<h2>Beat the odds.</h2>
		// 				<p classNameName="lead">
		// 					Ever wish you could game the system? Well now you can.
		// 				</p>
		// 				<p>
		// 					With so many sportsbooks all setting their own odds, there are
		// 					HUGE opportunities to make completely risk-free money. Yup.
		// 					Risk-free. We calculate the combinations of bets you would have to
		// 					place to walk away with a profit regardless of which teams win.
		// 					The concept is called 'arbitrage' and never before has it been so
		// 					easy to capitalize on these market inefficiencies.
		// 				</p>
		// 			</div>
		// 		</div>
		// 	</div>
		// </section>
	);
};

export default Showcase;
