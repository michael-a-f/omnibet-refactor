import React from "react";

const BetGrade = ({ betAmount, selectedTeam, expectedROI }) => {
	let grade;
	// Green buttons share the same base .png and we adjust brightness to get
	// different shades.
	if (expectedROI < 0.04) {
		grade = {
			text: "Bad Bet",
			textStyle: { color: "#e63632" },
			iconPath: `../../../img/Bad Bet.png`,
			imgStyle: { transform: "rotate(180deg)" },
		};
	} else if (expectedROI >= 0.04 && expectedROI < 0.07) {
		grade = {
			text: "Poor Bet",
			textStyle: { color: "#fb8d00" },
			iconPath: `../../../img/Poor Bet.png`,
			imgStyle: { transform: "rotate(135deg)" },
		};
	} else if (expectedROI >= 0.07 && expectedROI < 0.16) {
		grade = {
			text: "Fair Bet",
			textStyle: { color: "#54d15a" },
			iconPath: `../../../img/Great Bet.png`,
			imgStyle: { transform: "rotate(90deg)", filter: "brightness(130%)" },
		};
	} else if (expectedROI >= 0.16 && expectedROI < 0.25) {
		grade = {
			text: "Good Bet",
			textStyle: { color: "#44a948" },
			iconPath: `../../../img/Great Bet.png`,
			imgStyle: { transform: "rotate(45deg)", filter: "brightness(105%)" },
		};
	} else if (expectedROI >= 0.25) {
		grade = {
			text: "Great Bet",
			textStyle: { color: "#317934" },
			iconPath: `../../../img/Great Bet.png`,
			imgStyle: { transform: "rotate(0deg)", filter: "brightness(75%)" },
		};
	}

	// Handle cases of team objects not having a short name.
	// Mostly Boxing and UFC since people's names don't get abbreviations.
	let displayName;
	if (selectedTeam.short_name.length === 0) {
		displayName = selectedTeam.full_name.split(" ").pop();
	} else {
		displayName = selectedTeam.short_name;
	}

	return (
		<div className="bet-details d-flex flex-row justify-content-between align-items-end mt-1">
			<div className="d-flex flex-row justify-content-start align-items-center">
				<img
					className="bet-grade-icon"
					src={grade.iconPath}
					alt={grade.text}
					style={grade.imgStyle}
				></img>

				<div className="bet-grade-text">
					<p className="bet-grade-remark" style={grade.textStyle}>
						{grade.text}
					</p>
					{/* <p className="bet-grade-roi">${profitOnWin.toFixed(0)}</p> */}
					<p className="bet-grade-roi">{(100 * expectedROI).toFixed(2)}% ROI</p>
				</div>
			</div>
			<button className="btn btn-dark btn-sm">
				Bet ${betAmount} on {displayName}
			</button>
		</div>
	);
};

export default BetGrade;
