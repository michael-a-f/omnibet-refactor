import React from "react";

const Navbar = ({ availableSports }) => {
	return (
		<nav className="navbar navbar-expand-lg bg-light navbar-light py-3 fixed-top">
			<div className="container">
				<a href="#" className="navbar-brand">
					<img src="../../../img/icon.png" width="50" />
					OmniBet
					<p>Bet with confidence.</p>
				</a>

				<button
					className="navbar-toggler"
					type="button"
					data-bs-toggle="collapse"
					data-bs-target="#navmenu"
				>
					<span className="navbar-toggler-icon"></span>
				</button>

				<div className="collapse navbar-collapse" id="navmenu">
					<ul className="navbar-nav ms-auto">
						<li className="nav-item">
							<a target="_blank" href="#" className="nav-link">
								Motivations for Project
							</a>
						</li>
						<li className="nav-item">
							<a target="_blank" href="#" className="nav-link">
								How It Works
							</a>
						</li>
						<li className="nav-item">
							<a target="_blank" href="#" className="nav-link">
								Looking Ahead
							</a>
						</li>
						<li className="nav-item dropdown">
							<a
								className="nav-link dropdown-toggle"
								href="#"
								id="navbarDropdown"
								role="button"
								data-toggle="dropdown"
								aria-haspopup="true"
								aria-expanded="false"
							>
								See Our API
							</a>
							<div className="dropdown-menu" aria-labelledby="navbarDropdown">
								{availableSports.map((sport) => (
									<a
										className="dropdown-item"
										href={`http://127.0.0.1:5000/api/odds/${sport}`}
										target="_blank"
									>
										{sport.toUpperCase()}
									</a>
								))}
							</div>
						</li>
						<li className="nav-item">
							<a
								target="_blank"
								href="https://github.com/michael-a-f/omnibet-refactor"
								className="nav-link"
							>
								GitHub
							</a>
						</li>
					</ul>
				</div>
			</div>
		</nav>
	);
};

export default Navbar;
