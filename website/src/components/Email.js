import React from "react";

const Email = () => {
	return (
		// <section className="email text-dark p-5 mb-4">
		// 	<div className="container">
		<div className="email p-5 mb-4 d-md-flex justify-content-evenly align-items-center">
			<p className="mb-3 mb-md-0">Email me the best bets every day.</p>

			<div className="input-group">
				<input type="text" className="form-control" placeholder="Enter Email" />
				<button className="btn btn-dark btn-lg" type="button">
					Submit
				</button>
			</div>
		</div>
		// 	</div>
		// </section>
	);
};

export default Email;
