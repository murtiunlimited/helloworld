# Helloworld Project (Readme Written By Gemini 3)

## Project Folder Structure
```text
project_name/
│
├── backend/
│   └── app.py
│
├── data/
│   └── iris.csv
│
├── frontend/
│   └── app.py
│
├── models/
│   └── iris_nb.pkl
│
├── src/
│   ├── data/
│   │   ├── __init__.py
│   │   └── load_data.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── predict.py    
│   │   └── train.py       
│   │
│   └── utils/
│       ├── __init__.py      
│       ├── save_model.py    
│       └── __init__.py     
│
├── Dockerfile              
├── README.md                
├── requirements.txt        
└── start.sh              

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
