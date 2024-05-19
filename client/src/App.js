import "./app.css";
import AnimeButton from "./buttons/anime_button";
import { React } from "react";
import axios from "axios";

function App() {
  const handleButtonClick = (field, name) => {
    axios
      .post("http://localhost:5005/api/adjust-strategy", { field, name })
      .then((response) => console.log("Success:", response.data))
      .catch((error) => console.error("Error:", error));
  };

  return (
    <div className="App">
      <div className="sidebar">
        {/* Place sidebar content or navigation here */}
        <img src={"/tempLogo.png"} class="logo" alt="logo" />
      </div>
      <div className="videoContainer">
        <img
          src="http://localhost:5005/video_feed"
          alt="Live Stream"
          style={{ maxWidth: "100%", maxHeight: "100%" }}
        />
      </div>
      <div className="sidebar">
        {/* Right sidebar content */}
        <h2>Settings</h2>
        <div className="btnContainer">
          <AnimeButton
            name="Person 1"
            field="personality"
            onClick={handleButtonClick}
          />
          <AnimeButton
            name="Person 2"
            field="personality"
            onClick={handleButtonClick}
          />
          <AnimeButton name="Curl" field="curl" onClick={handleButtonClick} />
          <AnimeButton name="Squat" field="squat" onClick={handleButtonClick} />
          <AnimeButton
            name="PushUp"
            field="pushup"
            onClick={handleButtonClick}
          />
        </div>
      </div>
    </div>
  );
}

export default App;
