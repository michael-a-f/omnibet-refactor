import React from "react";

const Email = () => {
	return (
		<section id="email" className="bg-dark p-5 mb-4">
			<div className="container">
				<div className="d-flex flex-row justify-content-evenly align-items-center">
					<p className="mb-3 mb-md-0">Email me the best bets every day.</p>
					<div className="input-group">
						<input
							type="text"
							className="form-control"
							placeholder="Enter Email"
						/>
						<button className="btn btn-dark btn-lg" type="button">
							Submit
						</button>
					</div>
				</div>
			</div>
		</section>
	);
};

export default Email;
