import './app.css';
import Anime_Button from './buttons/anime_button';
import {React, useState, useEffect} from 'react'

function App() {

  

  return (
    <div className="App">

        <div className='btnContainer'>
          <Anime_Button name="Person 1" field="personality"/>
          <Anime_Button name="Person 2" field="personality"/>
          <Anime_Button name="Exercise 1" field="exercise"/>
          <Anime_Button name="Exercise 2" field="exercise"/>
        </div>

        <img src="http://localhost:5005/video_feed" alt="Live Stream" />
    </div>
  );
}

export default App;
