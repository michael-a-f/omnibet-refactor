import "./App.css";
import Navbar from "./components/Navbar";
import Showcase from "./components/Showcase";
import MatchupGrid from "./components/MatchupGrid";
import Sidebar from "./components/Sidebar";
import { useState, useEffect } from "react";
import axios from "axios";

const App = () => {
	// This state variable controls which sports we scrape odds for, as well
	// as which sports are displayed in the dropdown to filter by.
	const [availableSports, setAvailableSports] = useState([
		"nba",
		"nhl",
		"ufc",
		"ncaab",
		"ncaaf",
		"nfl",
		// "boxing",
	]);
	const [matchups, setMatchups] = useState([]);
	const [isLoading, setIsLoading] = useState(true);
	const [betAmount, setbetAmount] = useState(25);
	const [matchupFilters, setmatchupFilters] = useState({
		sports: availableSports,
		dates: "all",
		sort_by: "smartest",
	});

	const fetchAllMatchups = async () => {
		// Create HTTP request for each sport-- each sport has own webpage.
		const httpRequests = [];
		availableSports.forEach((sport) => {
			httpRequests.push(axios(`http://127.0.0.1:5000/api/odds/${sport}`));
		});

		// Await response for all http requests.
		const response = await Promise.all(httpRequests);

		// Response is list of lists. Loop through and make 1D array of all.
		const allMatchups = [];
		response.forEach((sport) => {
			sport.data.forEach((match) => {
				allMatchups.push(match);
			});
		});

		// 1D array of ALL matchup objects.
		return allMatchups;
	};

	// On first render, fetch all odds, set as state, and add to session.
	useEffect(() => {
		fetchAllMatchups().then((resolvedMatchups) => {
			setMatchups(resolvedMatchups);
			sessionStorage.setItem("odds", JSON.stringify(resolvedMatchups));
		});
	}, []);

	// On change to matchupFilters, update matchups array in state.
	useEffect(() => {
		// Start with all the matchups held in session.
		var allMatchups = JSON.parse(sessionStorage.getItem("odds"));

		// Filter for matchups of selected sport with the desired date filter.
		var displayMatchups = allMatchups.filter((matchup) => {
			return matchupFilters.sports.includes(matchup.sport);
		});

		// Sort according to criteria.

		// Update state variable
		setMatchups(displayMatchups);
	}, [matchupFilters]);

	return (
		<div className="App">
			<Navbar></Navbar>
			<Showcase></Showcase>
			<section id="main-content">
				<div className="container">
					<div className="row">
						<div id="sidebar" className="col-3">
							<Sidebar availableSports={availableSports}></Sidebar>
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

							<MatchupGrid
								matchups={matchups}
								availableSports={availableSports}
							></MatchupGrid>
						</div>
					</div>
				</div>
			</section>
		</div>
	);
};

export default App;
