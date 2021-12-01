import React from "react";

const Navbar = () => {
  return (
    <nav className="navbar navbar-expand-lg bg-light navbar-light py-3 fixed-top">
      <div className="container">
        <a href="#" className="navbar-brand">
          OmniBet
        </a>

        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navmenu"
        >
          <span className="navbar-toggler-icon"></span>
        </button>

        <div className="collapse navbar-collapse" id="navmenu">
          <ul className="navbar-nav ms-auto">
            <li className="nav-item">
              <a
                target="_blank"
                href="https://github.com/michael-a-f/omnibet-refactor"
                className="nav-link"
              >
                GitHub
              </a>
            </li>
            <li className="nav-item">
              <a
                target="_blank"
                href="http://127.0.0.1:5000/api/odds/nba"
                className="nav-link"
              >
                API
              </a>
            </li>
            <li className="nav-item">
              <a href="" className="nav-link">
                How it Works
              </a>
            </li>
            <li className="nav-item">
              <a href="" className="nav-link">
                Looking Ahead
              </a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
