import React from "react";
import MatchupGrid from "./MatchupGrid";
import Sidebar from "./Sidebar";

const MainContent = () => {
	return (
		<div className="main-content">
			<Sidebar></Sidebar>

			<MatchupGrid></MatchupGrid>
		</div>
	);
};

export default MainContent;
