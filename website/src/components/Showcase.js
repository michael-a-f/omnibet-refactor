import React from "react";

const Showcase = () => {
  return (
    <section
      id="showcase"
      className="bg-light text-dark p-5 p-lg-0 pt-lg-5 text-center text-sm-start"
    >
      <div className="container">
        <div className="d-sm-flex align-items-center justify-content-between">
          <div>
            <h1>Bet with confidence.</h1>
            <p className="lead my-2">
              We crunch the numbers. ALL of them. So you don't have to.
            </p>
          </div>
          <img
            className="img-fluid d-none d-sm-block"
            id="showcase-img"
            src="../../../img/showcase.png"
            alt="Showcase Image"
          />
        </div>
      </div>
    </section>
  );
};

export default Showcase;
