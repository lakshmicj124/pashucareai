@echo off
echo Starting PashuCare AI Full-Stack Application...

echo [1/2] Starting FastAPI Backend...
start cmd /k "cd backend && call venv\Scripts\activate.bat && python -m uvicorn app.main:app --port 8000 --host 127.0.0.1 --reload"

echo [2/2] Starting React Frontend...
start cmd /k "cd frontend && npm run dev"

echo Both servers have been launched in separate terminal windows!
echo Access the application at http://localhost:5173 / http://localhost:5174

