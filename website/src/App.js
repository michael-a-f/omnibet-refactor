import "./App.css";
import Navbar from "./components/Navbar";
import Showcase from "./components/Showcase";
import MatchupGrid from "./components/MatchupGrid";
import Sidebar from "./components/Sidebar";
import { useState, useEffect } from "react";
import axios from "axios";

const App = () => {
	// Declare state variables
	const [availableSports, setAvailableSports] = useState([
		// "nba",
		"nhl",
		// "ufc",
		// "ncaab",
		// "ncaaf",
		// "nfl",
		// "boxing",
	]);
	const [matchups, setMatchups] = useState([]);
	const [isLoading, setIsLoading] = useState(true);

	// Fetch all odds on the first render of page.
	useEffect(() => {
		const fetchAllMatchups = async () => {
			// Each element of httpRequests array is a sport's HTTP request.
			const httpRequests = [];
			availableSports.forEach((sport) => {
				httpRequests.push(axios(`http://127.0.0.1:5000/api/odds/${sport}`));
			});

			// Await response for all http requests.
			const response = await Promise.all(httpRequests);

			// Create array to hold every JSON object and variable as counter.
			const allMatchups = [];
			let match_id = 0;

			// Add every match for every sport to array and session storage.
			response.forEach((sport) => {
				sport.data.forEach((match) => {
					allMatchups.push(match);
					sessionStorage.setItem(match_id, JSON.stringify(match));
					match_id++;
				});
			});

			// Set state to this new array of all the JSON objects.
			setMatchups(allMatchups);
			setIsLoading(false);
		};

		// Runs only on first page load due to empty dependency array.
		fetchAllMatchups();
	}, []);

	return (
		<div className="App">
			<Navbar></Navbar>
			<Showcase></Showcase>
			<section id="main-content">
				<div className="container">
					<div className="row">
						<div id="sidebar" className="col-3">
							<Sidebar></Sidebar>
						</div>
						<div id="games" className="col-9">
							<div className="email d-flex flex-row justify-content-center align-items-center">
								<form>
									<label for="email">
										Sign up for daily emails of the day's best bets.
									</label>
									<input type="email" id="email" value="Email"></input>

									<button type="submit" class="btn btn-primary mb-2">
										Email Me
									</button>
								</form>
							</div>
							<div className="row justify-content-between">
								<div className="col-3">
									<select
										class="form-select"
										aria-label="Default select example"
									>
										<option selected>Smartest bets first</option>
										<option value="1">Biggest underdogs first</option>
										<option value="2">Biggest favorites first</option>
									</select>
								</div>
								<div className="col-3">
									<p>Showing 1-20 out of {matchups.length} games</p>
								</div>
							</div>

							<MatchupGrid matchups={matchups}></MatchupGrid>
						</div>
					</div>
				</div>
			</section>
		</div>
	);
};

export default App;
