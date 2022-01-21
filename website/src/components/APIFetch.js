import React from "react";
import { useState, useEffect } from "react";
import OmniBet from "./OmniBet";
import axios from "axios";

const APIFetch = ({ availableSports }) => {
	const [unfilteredMatchups, setUnfilteredMatchups] = useState([]);
	const [isFetching, setIsFetching] = useState(true);

	const fetchAllMatchups = async () => {
		const httpRequests = [];
		availableSports.forEach((sport) => {
			httpRequests.push(axios(`http://127.0.0.1:5000/api/odds/${sport}`));
			console.log("sending request");
		});
		const response = await Promise.all(httpRequests);
		const allMatchups = [];
		response.forEach((sport) => {
			sport.data.forEach((match) => {
				allMatchups.push(match);
			});
		});
		return allMatchups;
	};

	useEffect(() => {
		setIsFetching(true);
		fetchAllMatchups().then((resolvedMatchups) => {
			setUnfilteredMatchups(resolvedMatchups);
			sessionStorage.setItem("odds", JSON.stringify(resolvedMatchups));
			setIsFetching(false);
		});
	}, []);

	return (
		<OmniBet
			availableSports={availableSports}
			unfilteredMatchups={unfilteredMatchups}
		/>
	);
};

export default APIFetch;
