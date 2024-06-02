<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br>
<div align="center">
  <a href="https://chezzle.onrender.com/">
    <img src="./client/public/logo.png" alt="Logo" width="80" height="80">
  </a>
  <h1 align="center">myCurlfriend</h1>
  <h3 align="center">
    Workout with a curlfriend
  </h3>
</div>


https://github.com/Jinnbo/StormHacks/assets/75389217/c792f232-742d-4cbd-ac86-7929f46af5fb


## Inspiration

We know that going to the gym is often hard to initially get into. We hope this project would help introverted individuals feel like they have someone to talk to at the gym and ask for advice

## What it does
The assistant watches you through your camera while you work out. It analyzes your positioning of your body while you do different exercises and gives you encouraging messages

## How we built it
We developed this project by integrating pose detection using opencv and MediaPipe, as well as voice feedback systems using Python and Flask for the backend. The frontend, built with React, interfaces with the backend to display real-time video feeds and user interactions, enabling dynamic and responsive exercise guidance.

## What's next for Curlfriend
- Adding ChatGPT messages rather than prerecorded messages
- Adding more exercises
- Give more specific tips


## Running backend 
1. In root:
2. `python -m venv .venv`
3. `source .venv/bin/activate` or `.venv/Scripts/activate`
4. `pip install -r requirements.txt`
5. `cd backend`
6. `python AiTrainer.py`

## Running frontend
1. `cd client`
2. `npm install`
3. `npm start`
