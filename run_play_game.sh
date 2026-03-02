#!/usr/bin/bash


apt install python3-pip python3-venv -y
python3 -m venv venv1
source venv1/bin/activate
pip install streamlit
streamlit run play_game2.py
