import "./app.css";
import AnimeButton from "./buttons/anime_button";
import { useState } from "react";
import axios from "axios";

function App() {
  const [activeButton, setActiveButton] = useState("");

  const handleButtonClick = (field, name) => {
    setActiveButton(name);
    axios
      .post("http://localhost:5005/api/adjust-strategy", { field, name })
      .then((response) => console.log("Success:", response.data))
      .catch((error) => console.error("Error:", error));
  };

  return (
    <div className="App">
      <div className="navBar">
        <img src="./logo.png" className="logo" alt="Logo" />
        <div className="text">myCurlfriend</div>
      </div>
      <div className="mainContainer">
        <div className="videoContainer">
          <img
            src="http://localhost:5005/video_feed"
            alt="Live Stream"
            style={{ maxWidth: "100%", maxHeight: "100%" }}
          />
        </div>
        <div className="sidebar">
          <h2>Settings</h2>
          <div className="btnContainer">
            {/* <AnimeButton
              name="Person 1"
              field="personality"
              onClick={handleButtonClick}
              isActive={activeButton === "Person 1"}
            />
            <AnimeButton
              name="Person 2"
              field="personality"
              onClick={handleButtonClick}
              isActive={activeButton === "Person 2"}
            /> */}
            <AnimeButton
              name="Curl"
              field="curl"
              onClick={handleButtonClick}
              isActive={activeButton === "Curl"}
            />
            <AnimeButton
              name="Squat"
              field="squat"
              onClick={handleButtonClick}
              isActive={activeButton === "Squat"}
            />
            <AnimeButton
              name="PushUp"
              field="pushup"
              onClick={handleButtonClick}
              isActive={activeButton === "PushUp"}
            />
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;