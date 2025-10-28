#!/bin/bash
set -e

# --- Configuration ---
# You can change the default ports here if needed.
BACKEND_PORT=8000
FRONTEND_PORT=5170

# --- Environment Setup ---
# Set a dummy OpenAI API key for local development.
# The backend will fail to start if this is not set.
export OPENAI_API_KEY="dummy_key_for_dev"
echo "✅ Set dummy OPENAI_API_KEY for development."

# --- Node.js Version Check ---
echo "🔎 Checking Node.js version..."
NODE_MAJOR_VERSION=$(node -v | cut -d'.' -f1 | sed 's/v//')

if [[ "$NODE_MAJOR_VERSION" -ne 20 && "$NODE_MAJOR_VERSION" -ne 22 ]]; then
  echo "❌ Warning: You are using Node.js version $(node -v)."
  echo "   Vite requires a Long-Term Support (LTS) version like 20.x or 22.x."
  echo "   Please switch to a compatible version using a tool like 'nvm' (e.g., 'nvm use 20')."
  exit 1
fi
echo "✅ Node.js version $(node -v) is compatible."

# --- Backend Setup (using pip and venv) ---
echo "🛠️  Setting up backend..."
cd backend

# Create a virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
  echo "   - Creating Python virtual environment..."
  python3 -m venv .venv
fi

# Activate the virtual environment and install dependencies
echo "   - Installing Python dependencies with pip..."
source .venv/bin/activate
pip install -e . --quiet
deactivate # Deactivate after installation

cd ..
echo "✅ Backend setup complete."

# --- Frontend Setup ---
echo "🛠️  Setting up frontend..."
cd frontend
echo "   - Installing npm dependencies..."
npm install
cd ..
echo "✅ Frontend setup complete."

# --- Launch Servers ---
echo "🚀 Launching servers..."
echo "   - Backend will run on http://127.0.0.1:$BACKEND_PORT"
echo "   - Frontend will run on http://127.0.0.1:$FRONTEND_PORT"

# Use concurrently to run both servers.
# It's already in the devDependencies of the root package.json.
npx concurrently --kill-others-on-fail --names "BACKEND,FRONTEND" \
  "cd backend && source .venv/bin/activate && uvicorn app.main:app --reload --port $BACKEND_PORT" \
  "npm --prefix frontend run dev -- --port $FRONTEND_PORT"
