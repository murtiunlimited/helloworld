# Helloworld Project (Readme Written By Gemini 3)

## Setup & Run

## Project Folder Structure
```text
project_root/
│
├── backend/
│ └── app.py # Backend application code
│
├── data/
│ ├── iris.csv # Dataset file (CSV format)
│ └── Dockerfile # Docker configuration file
│
├── frontend/
│ └── app.py # Frontend application code
│
├── models/
│ └── iris_nb.pkl # Pickled machine learning model file
│
├── README.md # Project documentation file
├── requirements.txt # Python dependencies list
│
├── src/
│ ├── init.py # Marks this directory as a package
│ ├── data/ # Data-related helper modules
│ ├── models/ # Model-related helper modules
│ └── utils/ # Utility/helper functions
│
└── start.sh # Shell script to start the project
```
### 1. Clone the repository and run everything
```bash
git clone https://github.com/murtiunlimited/helloworld.git
cd helloworld

# Train the model
python -m src.models.train

# Start the backend API (in a new terminal)
python -m backend.app

# Run the frontend with Streamlit (main terminal)
streamlit run frontend/app.py
