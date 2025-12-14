# Helloworld Project (Readme Written By Gemini 3)

## Setup & Run

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
