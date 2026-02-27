#!/usr/bin/bash

apt install python3 python3-pip python3-venv -y
python3 -m venv venv-game
source venv-game/bin/activate
pip install streamlit
streamlit run guessing_game/play_game2.py
