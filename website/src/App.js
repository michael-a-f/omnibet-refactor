import "./App.css";
import Navbar from "./components/Navbar";
import Showcase from "./components/Showcase";
import MatchupGrid from "./components/MatchupGrid";
import Sidebar from "./components/Sidebar";

const App = () => {
	const temp_data = [
		{
			date: "Thursday November 4",
			time: "7:00p",
			team_1: {
				full_name: "Philadelphia",
				short_name: "PHI",
				odds: {
					opening: -333,
					bovada: -195,
					betonline: -195,
					intertops: -190,
					sportsbetting: -195,
					betnow: -190,
					mybookie: -185,
					gtbets: -140,
				},
				win_probability: 0.6618631166472025,
				money_multiplier: 1.7142857142857142,
			},
			team_2: {
				full_name: "Detroit",
				short_name: "DET",
				odds: {
					opening: 255,
					bovada: 165,
					betonline: 170,
					intertops: 165,
					sportsbetting: 170,
					betnow: 165,
					mybookie: 155,
					gtbets: 110,
				},
				win_probability: 0.3778567115274373,
				money_multiplier: 3.55,
			},
		},
		{
			date: "Thursday November 4",
			time: "7:30p",
			team_1: {
				full_name: "Utah",
				short_name: "UTA",
				odds: {
					opening: -105,
					bovada: -120,
					betonline: -125,
					intertops: -125,
					sportsbetting: -125,
					betnow: -125,
					mybookie: -125,
					gtbets: -135,
				},
				win_probability: 0.5512369412862407,
				money_multiplier: 1.9523809523809523,
			},
			team_2: {
				full_name: "Atlanta",
				short_name: "ATL",
				odds: {
					opening: -111,
					bovada: 100,
					betonline: 105,
					intertops: 105,
					sportsbetting: 105,
					betnow: 105,
					mybookie: 105,
					gtbets: 105,
				},
				win_probability: 0.4941119523754479,
				money_multiplier: 2.05,
			},
		},
		{
			date: "Thursday November 4",
			time: "7:30p",
			team_1: {
				full_name: "Boston",
				short_name: "BOS",
				odds: {
					opening: 265,
					bovada: 220,
					betonline: 215,
					intertops: 220,
					sportsbetting: 215,
					betnow: 220,
					mybookie: 220,
					gtbets: -115,
				},
				win_probability: 0.33672211982382416,
				money_multiplier: 3.65,
			},
			team_2: {
				full_name: "Miami",
				short_name: "MIA",
				odds: {
					opening: -310,
					bovada: -270,
					betonline: -255,
					intertops: -260,
					sportsbetting: -255,
					betnow: -260,
					mybookie: -270,
					gtbets: -115,
				},
				win_probability: 0.7039381130149507,
				money_multiplier: 1.8695652173913044,
			},
		},
		{
			date: "Thursday November 4",
			time: "10:00p",
			team_1: {
				full_name: "Houston",
				short_name: "HOU",
				odds: {
					opening: 500,
					bovada: 450,
					betonline: 520,
					intertops: 470,
					sportsbetting: 520,
					betnow: 465,
					mybookie: 450,
					gtbets: -115,
				},
				win_probability: 0.2175246429160324,
				money_multiplier: 6.2,
			},
			team_2: {
				full_name: "Phoenix",
				short_name: "PHO",
				odds: {
					opening: -700,
					bovada: -665,
					betonline: -700,
					intertops: -650,
					sportsbetting: -700,
					betnow: -630,
					mybookie: -600,
					gtbets: -115,
				},
				win_probability: 0.8269984986401909,
				money_multiplier: 1.8695652173913044,
			},
		},
		{
			date: "Thursday November 4",
			time: "10:30p",
			team_1: {
				full_name: "Oklahoma City",
				short_name: "OKC",
				odds: {
					opening: 700,
					bovada: 450,
					betonline: 460,
					intertops: 450,
					sportsbetting: 460,
					betnow: 490,
					mybookie: 500,
					gtbets: 130,
				},
				win_probability: 0.20209000269565855,
				money_multiplier: 8.0,
			},
			team_2: {
				full_name: "LA Lakers",
				short_name: "LAL",
				odds: {
					opening: -1100,
					bovada: -665,
					betonline: -600,
					intertops: -620,
					sportsbetting: -600,
					betnow: -680,
					mybookie: -700,
					gtbets: -160,
				},
				win_probability: 0.8404405031243265,
				money_multiplier: 1.625,
			},
		},
		{
			date: "Friday November 5",
			time: "7:00p",
			team_1: {
				full_name: "Brooklyn",
				short_name: "BKN",
				odds: {
					opening: -650,
					bovada: null,
					betonline: -470,
					intertops: null,
					sportsbetting: -470,
					betnow: null,
					mybookie: null,
					gtbets: null,
				},
				win_probability: 0.8385964912280701,
				money_multiplier: 1.2127659574468086,
			},
			team_2: {
				full_name: "Detroit",
				short_name: "DET",
				odds: {
					opening: 450,
					bovada: null,
					betonline: 380,
					intertops: null,
					sportsbetting: 380,
					betnow: null,
					mybookie: null,
					gtbets: null,
				},
				win_probability: 0.1994949494949495,
				money_multiplier: 5.5,
			},
		},
		{
			date: "Friday November 5",
			time: "7:00p",
			team_1: {
				full_name: "Memphis",
				short_name: "MEM",
				odds: {
					opening: null,
					bovada: null,
					betonline: null,
					intertops: null,
					sportsbetting: null,
					betnow: null,
					mybookie: null,
					gtbets: null,
				},
				win_probability: null,
				money_multiplier: null,
			},
			team_2: {
				full_name: "Washington",
				short_name: "WAS",
				odds: {
					opening: null,
					bovada: null,
					betonline: null,
					intertops: null,
					sportsbetting: null,
					betnow: null,
					mybookie: null,
					gtbets: null,
				},
				win_probability: null,
				money_multiplier: null,
			},
		},
		{
			date: "Friday November 5",
			time: "7:00p",
			team_1: {
				full_name: "San Antonio",
				short_name: "SAN",
				odds: {
					opening: -162,
					bovada: -165,
					betonline: -160,
					intertops: null,
					sportsbetting: -160,
					betnow: null,
					mybookie: -165,
					gtbets: -165,
				},
				win_probability: 0.6195023949596902,
				money_multiplier: 1.625,
			},
			team_2: {
				full_name: "Orlando",
				short_name: "ORL",
				odds: {
					opening: 135,
					bovada: 140,
					betonline: 140,
					intertops: null,
					sportsbetting: 140,
					betnow: null,
					mybookie: 140,
					gtbets: 145,
				},
				win_probability: 0.4167269744777344,
				money_multiplier: 2.45,
			},
		},
		{
			date: "Friday November 5",
			time: "7:30p",
			team_1: {
				full_name: "New York",
				short_name: "NY",
				odds: {
					opening: null,
					bovada: null,
					betonline: null,
					intertops: null,
					sportsbetting: null,
					betnow: null,
					mybookie: null,
					gtbets: null,
				},
				win_probability: null,
				money_multiplier: null,
			},
			team_2: {
				full_name: "Milwaukee",
				short_name: "MIL",
				odds: {
					opening: null,
					bovada: null,
					betonline: null,
					intertops: null,
					sportsbetting: null,
					betnow: null,
					mybookie: null,
					gtbets: null,
				},
				win_probability: null,
				money_multiplier: null,
			},
		},
		{
			date: "Friday November 5",
			time: "7:30p",
			team_1: {
				full_name: "Cleveland",
				short_name: "CLE",
				odds: {
					opening: 200,
					bovada: 200,
					betonline: null,
					intertops: null,
					sportsbetting: null,
					betnow: null,
					mybookie: null,
					gtbets: null,
				},
				win_probability: 0.3333333333333333,
				money_multiplier: 3.0,
			},
			team_2: {
				full_name: "Toronto",
				short_name: "TOR",
				odds: {
					opening: -250,
					bovada: -240,
					betonline: null,
					intertops: null,
					sportsbetting: null,
					betnow: null,
					mybookie: null,
					gtbets: null,
				},
				win_probability: 0.7100840336134454,
				money_multiplier: 1.4166666666666667,
			},
		},
		{
			date: "Friday November 5",
			time: "8:00p",
			team_1: {
				full_name: "LA Clippers",
				short_name: "LAC",
				odds: {
					opening: null,
					bovada: null,
					betonline: null,
					intertops: null,
					sportsbetting: null,
					betnow: null,
					mybookie: null,
					gtbets: null,
				},
				win_probability: null,
				money_multiplier: null,
			},
			team_2: {
				full_name: "Minnesota",
				short_name: "MIN",
				odds: {
					opening: null,
					bovada: null,
					betonline: null,
					intertops: null,
					sportsbetting: null,
					betnow: null,
					mybookie: null,
					gtbets: null,
				},
				win_probability: null,
				money_multiplier: null,
			},
		},
		{
			date: "Friday November 5",
			time: "10:00p",
			team_1: {
				full_name: "New Orleans",
				short_name: "NOP",
				odds: {
					opening: null,
					bovada: null,
					betonline: null,
					intertops: null,
					sportsbetting: null,
					betnow: null,
					mybookie: null,
					gtbets: null,
				},
				win_probability: null,
				money_multiplier: null,
			},
			team_2: {
				full_name: "Golden State",
				short_name: "GS",
				odds: {
					opening: null,
					bovada: null,
					betonline: null,
					intertops: null,
					sportsbetting: null,
					betnow: null,
					mybookie: null,
					gtbets: null,
				},
				win_probability: null,
				money_multiplier: null,
			},
		},
		{
			date: "Friday November 5",
			time: "10:00p",
			team_1: {
				full_name: "Charlotte",
				short_name: "CHR",
				odds: {
					opening: 103,
					bovada: 100,
					betonline: 100,
					intertops: null,
					sportsbetting: 100,
					betnow: null,
					mybookie: null,
					gtbets: 100,
				},
				win_probability: 0.4985221674876847,
				money_multiplier: 2.03,
			},
			team_2: {
				full_name: "Sacramento",
				short_name: "SAC",
				odds: {
					opening: -114,
					bovada: -120,
					betonline: -120,
					intertops: null,
					sportsbetting: -120,
					betnow: null,
					mybookie: null,
					gtbets: -120,
				},
				win_probability: 0.5429056924384027,
				money_multiplier: 1.8771929824561404,
			},
		},
		{
			date: "Friday November 5",
			time: "10:00p",
			team_1: {
				full_name: "Indiana",
				short_name: "IND",
				odds: {
					opening: 130,
					bovada: 135,
					betonline: 135,
					intertops: null,
					sportsbetting: 135,
					betnow: null,
					mybookie: 140,
					gtbets: 145,
				},
				win_probability: 0.42270138089154874,
				money_multiplier: 2.45,
			},
			team_2: {
				full_name: "Portland",
				short_name: "POR",
				odds: {
					opening: -154,
					bovada: -160,
					betonline: -155,
					intertops: null,
					sportsbetting: -155,
					betnow: null,
					mybookie: -165,
					gtbets: -165,
				},
				win_probability: 0.6137755202267948,
				money_multiplier: 1.6493506493506493,
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
