// AnimeButton.js
import React from "react";
import "./style.css";

function AnimeButton({ name, field, onClick, isActive }) {
  const baseStyle = {
    backgroundColor: isActive ? "red" : "#f4f4f4", // Red when active, light gray otherwise
    color: isActive ? "white" : "black", // White text for active, black for inactive
    fontWeight: isActive ? "bold" : "normal", // Bold text when active
  };

  return (
    <button style={baseStyle} class="btn" onClick={() => onClick(field, name)}>
      {name}
    </button>
  );
}

export default AnimeButton;