import React from "react";
import axios from "axios";
import Sidebar from "./Sidebar";
import Email from "./Email";
import SortBar from "./SortBar";
import MatchupGrid from "./MatchupGrid";
import { useState, useEffect } from "react";

const MainContent = ({ availableSports }) => {
  const [isFetching, setIsFetching] = useState(true);
  const [matchupFilters, setmatchupFilters] = useState({
    sports: [...availableSports],
    dates: ["today", "future"],
    sort_by: "smartest",
    page: 1,
  });
  const [betAmount, setbetAmount] = useState(200);
  const [matchups, setMatchups] = useState([]);

  // Fetch matchups from API for all available sports and return in array.
  const fetchAllMatchups = async () => {
    const httpRequests = [];
    availableSports.forEach((sport) => {
      httpRequests.push(axios(`http://127.0.0.1:5000/api/odds/${sport}`));
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

  // On first render, fetch all odds, add to session, and set in state.
  useEffect(() => {
    setIsFetching(true);
    fetchAllMatchups().then((resolvedMatchups) => {
      setMatchups(resolvedMatchups);
      sessionStorage.setItem("odds", JSON.stringify(resolvedMatchups));
      setIsFetching(false);
    });
  }, []);

  // Function to modify the sports attribute of matchupFilters.
  // When matchupFilters changes, it fires off useEffect which updates
  // the variable holding matchups in state.
  const filterMatchups = (eventTarget) => {
    console.log(eventTarget.value);
    switch (eventTarget.id) {
      case "sports-filter":
        if (eventTarget.value === "all") {
          setmatchupFilters({ ...matchupFilters, sports: availableSports });
        } else {
          setmatchupFilters({ ...matchupFilters, sports: [eventTarget.value] });
        }
        break;
      case "dates-filter":
        if (eventTarget.value === "all") {
          setmatchupFilters({ ...matchupFilters, dates: ["today", "future"] });
        } else {
          setmatchupFilters({ ...matchupFilters, dates: [eventTarget.value] });
        }
        break;
      case "sort-by":
        setmatchupFilters({ ...matchupFilters, sort_by: eventTarget.value });
        break;
      default:
        break;
    }
  };

  return (
    <section id="main-content">
      <div className="container py-5">
        <div className="row">
          <div className="col-xl-3 pb-4">
            <Sidebar
              availableSports={availableSports}
              matchupFilters={matchupFilters}
              onFilterMatchups={filterMatchups}
            />
          </div>
          <div className="col-xl-9">
            <Email />
            <SortBar
              matchupCount={matchups.length}
              onFilterMatchups={filterMatchups}
            />
            <MatchupGrid
              matchups={matchups}
              betAmount={betAmount}
              matchupFilters={matchupFilters}
            />
          </div>
        </div>
      </div>
    </section>
  );
};

export default MainContent;
