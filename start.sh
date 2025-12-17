#!/bin/bash

# Start backend Flask app in background
python -m backend.app &

# Start frontend Streamlit app
streamlit run frontend/app.py --server.port=8501 --server.address=0.0.0.0
