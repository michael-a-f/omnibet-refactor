import "./App.css";
import { useState } from "react";
import Navbar from "./components/Navbar";
import Showcase from "./components/Showcase";
import Boxes from "./components/Boxes";
import Footer from "./components/Footer";
import MainContent from "./components/MainContent";

const App = () => {
  const [availableSports, setAvailableSports] = useState([
    "nba",
    "nhl",
    // "ufc",
    // "ncaab",
    // "ncaaf",
    "nfl",
    // "boxing",
  ]);

  return (
    <div className="App">
      <Navbar />
      <Showcase />
      <Boxes />
      <MainContent availableSports={availableSports} />
      <Footer />
    </div>
  );
};

export default App;
