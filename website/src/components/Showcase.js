import React from "react";

const Showcase = () => {
	return (
		<section
			id="showcase"
			className="bg-light text-dark p-5 p-lg-0 pt-lg-5 text-center text-sm-start"
		>
			<div className="container mt-5 pt-5">
				<div className="row py-5">
					<div className="col-7">
						<h1>Online sports gambling is confusing.</h1>
						<h1>It doesn't have to be.</h1>
						<p className="lead my-4">
							With OmniBet, you don't have to worry about pluses or minuses. We
							crunch the numbers for you. Yes, all of them. The end result? You
							can bet with confidence knowing that you are getting the best
							possible payout.
						</p>
						<button className="cta mt-3 bg-dark" href="#">
							{" "}
							See it in action
						</button>
					</div>
					<div className="col-5">
						<img
							className="img-fluid d-none d-sm-block mx-auto"
							id="showcase-img"
							src="../../../img/showcase.png"
							alt="Showcase"
						/>
					</div>
				</div>
			</div>
		</section>
	);
};

export default Showcase;
