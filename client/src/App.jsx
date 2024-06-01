import "./app.css";
import Button from "./Button/Button";
import { useState } from "react";
import axios from "axios";

function App() {
  const [activeButton, setActiveButton] = useState("Curl");

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
            <Button
              name="Curl"
              field="curl"
              onClick={handleButtonClick}
              isActive={activeButton === "Curl"}
            />
            <Button
              name="Squat"
              field="squat"
              onClick={handleButtonClick}
              isActive={activeButton === "Squat"}
            />
            <Button
              name="Push Up"
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