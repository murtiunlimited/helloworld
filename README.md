# Helloworld Project

## Setup & Run

### 1. Clone the repository and run everything
```bash
git clone <your-repo-url>
cd helloworld

# Train the model
python -m src.models.train

# Start the backend API (in a new terminal)
python -m backend.app

# Run the frontend with Streamlit (main terminal)
streamlit run frontend/app.py
