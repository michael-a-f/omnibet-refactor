import React from "react";

const Navbar = () => {
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
							<a
								target="_blank"
								href="https://github.com/michael-a-f/omnibet-refactor"
								className="nav-link"
							>
								GitHub
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
								Dropdown
							</a>
							<div className="dropdown-menu" aria-labelledby="navbarDropdown">
								<a
									className="dropdown-item"
									href="http:127.0.0.1:5000/api/odds/nba"
									target="_blank"
								>
									NBA
								</a>
								<a
									className="dropdown-item"
									href="http:127.0.0.1:5000/api/odds/nhl"
									target="_blank"
								>
									NHL
								</a>
								<a
									className="dropdown-item"
									href="http:127.0.0.1:5000/api/odds/nfl"
									target="_blank"
								>
									NFL
								</a>
							</div>
						</li>
					</ul>
				</div>
			</div>
		</nav>
	);
};

export default Navbar;
