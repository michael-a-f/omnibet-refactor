import "./App.css";
import Navbar from "./components/Navbar";
import Showcase from "./components/Showcase";
import MatchupGrid from "./components/MatchupGrid";
import Sidebar from "./components/Sidebar";

const App = () => {
	const temp_data = [
		{
			sport: "nba",
			date: "Monday November 8",
			time: "7:00p",
			team_1: {
				full_name: "New York",
				short_name: "NY",
				logo: "../../../img/nba-logos/New York.png",
				odds: {
					opening: 150,
					bovada: -135,
					betonline: -135,
					intertops: -130,
					sportsbetting: -135,
					betnow: -133,
					mybookie: -150,
					gtbets: -130,
				},
				win_probability: 0.5530818110714527,
				money_multiplier: 2.5,
			},
			team_2: {
				full_name: "Philadelphia",
				short_name: "PHI",
				logo: "../../../img/nba-logos/Philadelphia.png",
				odds: {
					opening: -182,
					bovada: 115,
					betonline: 115,
					intertops: 110,
					sportsbetting: 115,
					betnow: 113,
					mybookie: 125,
					gtbets: 110,
				},
				win_probability: 0.48838098412897535,
				money_multiplier: 2.25,
			},
		},
		{
			sport: "nba",
			date: "Monday November 8",
			time: "8:00p",
			team_1: {
				full_name: "Brooklyn",
				short_name: "BKN",
				logo: "../../../img/nba-logos/Brooklyn.png",
				odds: {
					opening: 100,
					bovada: -120,
					betonline: -110,
					intertops: -115,
					sportsbetting: -110,
					betnow: -110,
					mybookie: -120,
					gtbets: -110,
				},
				win_probability: 0.5276288633846773,
				money_multiplier: 2.0,
			},
			team_2: {
				full_name: "Chicago",
				short_name: "CHI",
				logo: "../../../img/nba-logos/Chicago.png",
				odds: {
					opening: -120,
					bovada: 100,
					betonline: -110,
					intertops: -105,
					sportsbetting: -110,
					betnow: -110,
					mybookie: 100,
					gtbets: -110,
				},
				win_probability: 0.5191109703304825,
				money_multiplier: 2.0,
			},
		},
		{
			sport: "nba",
			date: "Monday November 8",
			time: "8:00p",
			team_1: {
				full_name: "Minnesota",
				short_name: "MIN",
				logo: "../../../img/nba-logos/Minnesota.png",
				odds: {
					opening: 195,
					bovada: 160,
					betonline: 165,
					intertops: 160,
					sportsbetting: 165,
					betnow: 165,
					mybookie: 160,
					gtbets: 160,
				},
				win_probability: 0.3761900076258886,
				money_multiplier: 2.95,
			},
			team_2: {
				full_name: "Memphis",
				short_name: "MEM",
				logo: "../../../img/nba-logos/Memphis.png",
				odds: {
					opening: -233,
					bovada: -185,
					betonline: -190,
					intertops: -180,
					sportsbetting: -190,
					betnow: -190,
					mybookie: -190,
					gtbets: -190,
				},
				win_probability: 0.6584427148174878,
				money_multiplier: 1.5555555555555556,
			},
		},
		{
			sport: "nba",
			date: "Monday November 8",
			time: "8:30p",
			team_1: {
				full_name: "New Orleans",
				short_name: "NOP",
				logo: "../../../img/nba-logos/New Orleans.png",
				odds: {
					opening: 325,
					bovada: 345,
					betonline: 320,
					intertops: 330,
					sportsbetting: 320,
					betnow: 325,
					mybookie: 350,
					gtbets: 310,
				},
				win_probability: 0.23377257667371068,
				money_multiplier: 4.5,
			},
			team_2: {
				full_name: "Dallas",
				short_name: "DAL",
				logo: "../../../img/nba-logos/Dallas.png",
				odds: {
					opening: -400,
					bovada: -470,
					betonline: -400,
					intertops: -420,
					sportsbetting: -400,
					betnow: -400,
					mybookie: -450,
					gtbets: -420,
				},
				win_probability: 0.8072659796344006,
				money_multiplier: 1.25,
			},
		},
		{
			sport: "nba",
			date: "Monday November 8",
			time: "9:00p",
			team_1: {
				full_name: "Miami",
				short_name: "MIA",
				logo: "../../../img/nba-logos/Miami.png",
				odds: {
					opening: -111,
					bovada: -135,
					betonline: -128,
					intertops: -125,
					sportsbetting: -128,
					betnow: -123,
					mybookie: -135,
					gtbets: -125,
				},
				win_probability: 0.5575612695381368,
				money_multiplier: 1.9009009009009008,
			},
			team_2: {
				full_name: "Denver",
				short_name: "DEN",
				logo: "../../../img/nba-logos/Denver.png",
				odds: {
					opening: -105,
					bovada: 115,
					betonline: 108,
					intertops: 105,
					sportsbetting: 108,
					betnow: 103,
					mybookie: 110,
					gtbets: 105,
				},
				win_probability: 0.48540761653573866,
				money_multiplier: 2.15,
			},
		},
		{
			sport: "nba",
			date: "Monday November 8",
			time: "10:00p",
			team_1: {
				full_name: "Atlanta",
				short_name: "ATL",
				logo: "../../../img/nba-logos/Atlanta.png",
				odds: {
					opening: 115,
					bovada: 145,
					betonline: 140,
					intertops: 140,
					sportsbetting: 140,
					betnow: 145,
					mybookie: 140,
					gtbets: 145,
				},
				win_probability: 0.41953409270685016,
				money_multiplier: 2.45,
			},
			team_2: {
				full_name: "Golden State",
				short_name: "GS",
				logo: "../../../img/nba-logos/Golden State.png",
				odds: {
					opening: -138,
					bovada: -170,
					betonline: -160,
					intertops: -160,
					sportsbetting: -160,
					betnow: -165,
					mybookie: -165,
					gtbets: -165,
				},
				win_probability: 0.615442492107309,
				money_multiplier: 1.7246376811594204,
			},
		},
		{
			sport: "nba",
			date: "Monday November 8",
			time: "10:00p",
			team_1: {
				full_name: "Phoenix",
				short_name: "PHO",
				logo: "../../../img/nba-logos/Phoenix.png",
				odds: {
					opening: -141,
					bovada: -160,
					betonline: -158,
					intertops: -155,
					sportsbetting: -158,
					betnow: -158,
					mybookie: -165,
					gtbets: -160,
				},
				win_probability: 0.6104406775559472,
				money_multiplier: 1.7092198581560283,
			},
			team_2: {
				full_name: "Sacramento",
				short_name: "SAC",
				logo: "../../../img/nba-logos/Sacramento.png",
				odds: {
					opening: 125,
					bovada: 135,
					betonline: 138,
					intertops: 135,
					sportsbetting: 138,
					betnow: 138,
					mybookie: 140,
					gtbets: 140,
				},
				win_probability: 0.4236682261557104,
				money_multiplier: 2.4,
			},
		},
		{
			sport: "nba",
			date: "Monday November 8",
			time: "10:30p",
			team_1: {
				full_name: "Charlotte",
				short_name: "CHR",
				logo: "../../../img/nba-logos/Charlotte.png",
				odds: {
					opening: 125,
					bovada: 115,
					betonline: 118,
					intertops: 115,
					sportsbetting: 118,
					betnow: 118,
					mybookie: 120,
					gtbets: 120,
				},
				win_probability: 0.45748933758321425,
				money_multiplier: 2.25,
			},
			team_2: {
				full_name: "LA Lakers",
				short_name: "LAL",
				logo: "../../../img/nba-logos/LA Lakers.png",
				odds: {
					opening: -141,
					bovada: -135,
					betonline: -138,
					intertops: -135,
					sportsbetting: -138,
					betnow: -138,
					mybookie: -140,
					gtbets: -140,
				},
				win_probability: 0.5800201094828326,
				money_multiplier: 1.7407407407407407,
			},
		},
		{
			sport: "nba",
			date: "Tuesday November 9",
			time: "7:30p",
			team_1: {
				full_name: "Milwaukee",
				short_name: "MIL",
				logo: "../../../img/nba-logos/Milwaukee.png",
				odds: {
					opening: -263,
					bovada: null,
					betonline: null,
					intertops: null,
					sportsbetting: null,
					betnow: null,
					mybookie: null,
					gtbets: null,
				},
				win_probability: 0.7245179063360881,
				money_multiplier: 1.3802281368821292,
			},
			team_2: {
				full_name: "Philadelphia",
				short_name: "PHI",
				logo: "../../../img/nba-logos/Philadelphia.png",
				odds: {
					opening: 210,
					bovada: null,
					betonline: null,
					intertops: null,
					sportsbetting: null,
					betnow: null,
					mybookie: null,
					gtbets: null,
				},
				win_probability: 0.3225806451612903,
				money_multiplier: 3.1,
			},
		},
		{
			sport: "nba",
			date: "Tuesday November 9",
			time: "9:00p",
			team_1: {
				full_name: "Atlanta",
				short_name: "ATL",
				logo: "../../../img/nba-logos/Atlanta.png",
				odds: {
					opening: 275,
					bovada: -350,
					betonline: 280,
					intertops: null,
					sportsbetting: 280,
					betnow: null,
					mybookie: null,
					gtbets: null,
				},
				win_probability: 0.39269005847953214,
				money_multiplier: 3.8,
			},
			team_2: {
				full_name: "Utah",
				short_name: "UTA",
				logo: "../../../img/nba-logos/Utah.png",
				odds: {
					opening: -335,
					bovada: 275,
					betonline: -350,
					intertops: null,
					sportsbetting: -350,
					betnow: null,
					mybookie: null,
					gtbets: null,
				},
				win_probability: 0.6480842911877395,
				money_multiplier: 3.75,
			},
		},
		{
			sport: "nba",
			date: "Tuesday November 9",
			time: "10:00p",
			team_1: {
				full_name: "Portland",
				short_name: "POR",
				logo: "../../../img/nba-logos/Portland.png",
				odds: {
					opening: 135,
					bovada: 125,
					betonline: 125,
					intertops: null,
					sportsbetting: 125,
					betnow: null,
					mybookie: null,
					gtbets: 130,
				},
				win_probability: 0.4387295713845205,
				money_multiplier: 2.35,
			},
			team_2: {
				full_name: "LA Clippers",
				short_name: "LAC",
				logo: "../../../img/nba-logos/LA Clippers.png",
				odds: {
					opening: -162,
					bovada: -145,
					betonline: -145,
					intertops: null,
					sportsbetting: -145,
					betnow: null,
					mybookie: null,
					gtbets: -150,
				},
				win_probability: 0.5987661629537311,
				money_multiplier: 1.6896551724137931,
			},
		},
	];
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
								{/* <p>Email me can't miss opportunities of mispriced bets.</p> */}
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
									<p>Showing 1-20 out of 63 games</p>
								</div>
							</div>

							<MatchupGrid matchups={temp_data}></MatchupGrid>
						</div>
					</div>
				</div>
			</section>
		</div>
	);
};

export default App;
