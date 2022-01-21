import "./App.css";
import Navbar from "./components/Navbar";
import Showcase from "./components/Showcase";
import Boxes from "./components/Boxes";
import Footer from "./components/Footer";
import OmniBet from "./components/OmniBet";
import Email from "./components/Email";
import APIFetch from "./components/APIFetch";

const App = () => {
	const AVAILABLE_SPORTS = [
		"nba",
		"nhl",
		"ufc",
		// "ncaab",
		// "ncaaf",
		// "nfl",
		// "boxing",
	];

	return (
		<div className="App">
			<Navbar />
			<Showcase />
			<Boxes />
			<Email />
			<APIFetch availableSports={AVAILABLE_SPORTS} />
			<Footer />
		</div>
	);
};

export default App;
