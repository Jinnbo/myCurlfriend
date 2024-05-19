// ButtonComponent.js
import React from "react";
import "./style.css";

function AnimeButton({ field, name, onClick }) {
  return (
    <button
      className="anime-button"
      class="btn"
      onClick={() => onClick(field, name)}
    >
      {name}
    </button>
  );
}

export default AnimeButton;
