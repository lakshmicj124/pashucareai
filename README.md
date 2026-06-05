# PashuCare AI 🐾

PashuCare AI is a comprehensive, full-stack application designed to help farmers and veterinarians accurately diagnose diseases in livestock (Cows, Goats, and Sheep) using cutting-edge Artificial Intelligence. 

## Features
- **AI Disease Diagnostics:** Upload images of livestock to detect potential diseases instantly.
- **Multilingual Support:** Supports English, Hindi, and Kannada for rural accessibility.
- **AI Veterinary Chatbot:** A Gemini-powered AI chatbot providing localized, real-time veterinary advice.
- **Nearby Vets:** Integration with OpenStreetMap to find veterinary clinics near you.
- **Authentication:** Secure user registration and login.
- **Full-Stack Architecture:** Built with a robust FastAPI (Python) backend and a dynamic React (Vite) frontend.

## Technology Stack
- **Frontend:** React, Vite, TailwindCSS (or vanilla CSS)
- **Backend:** FastAPI, Python, Uvicorn
- **Database:** MongoDB
- **AI Models:** Gemini API & Custom Computer Vision models

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/lakshmicj124/pashucareai.git
cd pashucareai
```

### 2. Set up the Environment
Ensure you have the required environment variables. You will need a `.env` file in the `backend/` directory with:
- `MONGODB_URI`
- `GEMINI_API_KEY`
- `JWT_SECRET`

### 3. Start the Application
You can start both the backend and frontend simultaneously by running the startup script from the root directory:
```bash
# On Windows
.\start.bat
```

Alternatively, you can run them manually:
**Backend:**
```bash
cd backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn app.main:app --port 8000 --reload
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

## License
MIT License