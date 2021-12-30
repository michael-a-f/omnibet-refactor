import "./App.css";
import Navbar from "./components/Navbar";
import Showcase from "./components/Showcase";
import Boxes from "./components/Boxes";
import Footer from "./components/Footer";
import MainContent from "./components/MainContent";

const App = () => {
	const AVAILABLE_SPORTS = [
		"nba",
		// "nhl",
		// "ufc",
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
			<MainContent availableSports={AVAILABLE_SPORTS} />
			<Footer />
		</div>
	);
};

export default App;
