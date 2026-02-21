#!/usr/bin/bash


apt install python3 python3-pip python3-venv -y
python3 -m venv venv-guessing-game
source venv-guessing-game/bin/activate
pip install streamlit
streamlit run app.py
