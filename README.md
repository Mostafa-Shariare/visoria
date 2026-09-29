# Visoria: An Attention-Aware Intervention System for Online Classrooms

Welcome to the **Visoria** project repository. This document provides a comprehensive overview of the full system architecture, components, and machine learning pipeline, designed specifically to help you prepare for your thesis defense.

---

## 1. System Overview

Visoria is a real-time, privacy-preserving, edge-computed student attention monitoring system designed to bridge the gap between online distance learning and physical classrooms. Rather than acting as a surveillance tool, Visoria functions as a **Teacher Decision-Support System**, utilizing an automated behavioral telemetry pipeline to notify educators when students lose focus, allowing teachers to launch real-time Socratic interventions to re-engage the classroom.

The system is built on a 3-tier architecture:
1. **Student Edge Client (Computer Vision & ML)**
2. **Centralized Backend Server (FastAPI + WebSockets)**
3. **Teacher & Student Web Portals (React 19)**

---

## 2. Core Components & Technology Stack

### A. The Backend (Python + FastAPI)
The backend acts as the central nervous system, handling authentication, database storage, and real-time telemetry routing.
- **Framework**: `FastAPI` (Chosen for high-performance async processing and native WebSocket support).
- **Real-Time Communication**: `WebSockets` (Used to broadcast live student attention scores from the desktop client to the teacher dashboard with near-zero latency).
- **Database**: `MongoDB` (NoSQL database used to store user profiles, class rosters, and longitudinal session analytics).
- **Authentication**: `PyJWT` & `passlib` (For secure JWT token-based authentication and BCrypt password hashing).

### B. The Frontend Web Portals (React + Vite)
The web application provides two distinct interfaces: a Teacher Dashboard for live monitoring and a Student Portal for self-reflection.
- **Framework**: `React 19` built with `Vite` (For fast hot-module reloading and optimized production builds).
- **Styling**: Standard CSS with a custom "Calm Focus" design system.
- **Data Visualization**: `Recharts` / `Chart.js` (Used to render real-time attention trend lines, student sparklines, and historical analytics).
- **State Management**: React Hooks (`useState`, `useEffect`) and native Context API.

### C. The Student Edge Client (Computer Vision + ML)
The client runs locally on the student's machine to process webcam feeds without sending raw video over the internet.
- **UI Framework**: `Tkinter` / `Electron` (For a lightweight, cross-platform desktop window).
- **Computer Vision Libraries**:
  - `OpenCV` (For webcam capture and frame manipulation).
  - `MediaPipe` (Google's framework used to extract 478 3D facial landmarks, track iris gaze vectors, and detect hand presence).
  - `YOLOv8n` (Ultralytics nano-model used for extremely fast mobile phone detection).
- **Machine Learning**: `scikit-learn`, `pandas`, `numpy`.

---

## 3. The Machine Learning & Computer Vision Pipeline

The attention detection system does not rely on a black-box neural network processing raw images. Instead, it mathematically extracts **23 behavioral features** and classifies them using a traditional Machine Learning model. 

### Step 1: Feature Extraction
The CV pipeline calculates 23 distinct signals:
1. **Raw Posture & Gaze**: Head pitch, yaw, roll, eye aspect ratio (EAR), blink frequency, and gaze direction.
2. **Object Detection**: Phone presence, phone bounding box confidence, and active hand count.
3. **Engineered Relational Features (The Innovation)**: Instead of relying on raw bounding boxes which change based on camera resolution, Visoria engineers spatial context:
   - `face_area` & `phone_area` (Proxies for depth).
   - `face_phone_dist` (Euclidean distance between the face and phone).
   - `phone_near_face` (A binary threshold trigger if the phone is held up to read/text).
4. **Dynamic Auto-Calibration**: The system tracks when the user's gaze is centered and automatically zeroes out the baseline head pitch and yaw. This makes the system incredibly robust to different webcam heights and slouching postures!

### Step 2: The Classifier
- **Model Used**: `RandomForestClassifier` (Selected via GridSearchCV for its perfect balance of high accuracy and extremely fast inference time on low-end CPUs).
- **Performance**: Achieves **99.87% accuracy** on the V2 dataset.
- **Probability Calibration**: Uses Isotonic Regression (`CalibratedClassifierCV`) to ensure the output percentage is a true reflection of confidence.

### Step 3: Temporal Smoothing
Because humans naturally twitch and cameras glitch, a raw frame-by-frame prediction causes "flickering." Visoria applies a **15-frame Temporal Smoother** (Moving Average) with hysteresis bounds (45% / 55%) to lock the student into a stable Attentive or Distracted state.

### Step 4: Explainability (SHAP)
- **Library**: `SHAP` (SHapley Additive exPlanations).
- **Defense Note**: If asked *why* the model made a decision, SHAP proves that the model heavily relies on our engineered `phone_near_face` feature and forward head pose, proving the model learned actual human behavior rather than memorizing background pixels.

---

## 4. The Pedagogical Intervention System

Visoria is not just a tracker; it is an intervention platform. When the backend detects that the class average attention drops below 50% for more than 30 seconds, it alerts the teacher. 

The teacher can then trigger a **Socratic Intervention**. This immediately pushes an interactive pop-quiz to all student dashboards, forcing them through a 4-stage active learning loop:
1. **Think**: Answer the question and state confidence.
2. **Compare**: View anonymous class results.
3. **Reflect**: Type a short justification for their reasoning.
4. **Reassess**: Submit a final answer.

---

## 5. Privacy & Security Architecture (Crucial for Defense)

If asked about privacy concerns (FERPA/GDPR), emphasize these three pillars:
1. **100% Edge Processing**: The webcam feed NEVER leaves the student's laptop. All YOLOv8 and MediaPipe processing happens locally in RAM.
2. **Lightweight Telemetry**: Only a tiny JSON payload containing numbers (e.g., `attention: 85`, `pitch: 12.4`) is sent via WebSockets to the server.
3. **Student Agency**: Students have a visible "Pause Monitoring" button. When clicked, tracking stops, and the teacher sees a neutral "Paused" badge, ensuring students are not falsely penalized for taking a break.

---

## 6. Installation & Setup Guide

Follow the steps below to install dependencies and configure the complete Visoria stack locally.

### Prerequisites
Make sure you have the following installed on your machine:
- **Python**: `3.10` or `3.11` recommended ([Download Python](https://www.python.org/downloads/))
- **Node.js**: `v18+` or `v20+` with `npm` ([Download Node.js](https://nodejs.org/))
- **MongoDB**: Local MongoDB Community Server running on port `27017` or Docker ([Download MongoDB](https://www.mongodb.com/try/download/community))
- **Git**: For version control
- **Webcam**: Required for real-time edge facial landmark and attention tracking

---

### Step 1: Clone the Repository
```bash
git clone https://github.com/Mostafa-Shariare/visoria.git
cd visoria
```

---

### Step 2: Configure Environment Variables
Copy the provided `.env.example` file to create your local `.env`:

- **Windows (PowerShell / CMD):**
  ```powershell
  Copy-Item .env.example .env
  ```
- **macOS / Linux:**
  ```bash
  cp .env.example .env
  ```

> [!NOTE]
> Review `.env` and configure values as needed. By default, it connects to local MongoDB at `mongodb://localhost:27017` with database `attention_tracker`. Ensure `JWT_SECRET` is set to a secure string in production environments.

---

### Step 3: Python Environment & Dependencies (Backend & ML)
Create and activate a Python virtual environment, then install the required dependencies:

**1. Create a virtual environment:**
```bash
python -m venv venv
```

**2. Activate the virtual environment:**
- **Windows (PowerShell):**
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```
  *(If script execution is disabled, run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned` first)*
- **Windows (CMD):**
  ```cmd
  venv\Scripts\activate.bat
  ```
- **macOS / Linux:**
  ```bash
  source venv/bin/activate
  ```

**3. Install Python dependencies:**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```
> This installs packages for the FastAPI backend (`fastapi`, `uvicorn`, `pymongo`, `pyjwt`, `pydantic`), the ML/CV edge pipeline (`opencv-python`, `mediapipe`, `ultralytics`, `scikit-learn`), and test/dev tools.

---

### Step 4: Web Portals Setup (Frontend)
Install the Node.js packages for the React + Vite web dashboards:

```bash
cd frontend
npm install
cd ..
```

---

### Step 5: (Optional) Electron Desktop Tracker Setup
If you want to use the Electron wrapper for the student edge client:

```bash
cd electron-tracker
npm install
cd ..
```

---

## 7. Running the Application

### 1. Start the Database (MongoDB)
Ensure MongoDB is running locally on port `27017`.

If using Docker:
```bash
docker compose up mongo -d
```

### 2. Start the Backend Server
From the project root with your virtual environment activated:
```bash
python -m uvicorn backend.app.main:app --reload --host 127.0.0.1 --port 8000
```
- **Backend API**: `http://127.0.0.1:8000`
- **Interactive OpenAPI/Swagger Docs**: `http://127.0.0.1:8000/docs`

### 3. Start the Web Dashboards (Teacher & Student)
In a new terminal window:
```bash
cd frontend
npm run dev
```
- Access the web portals at: `http://localhost:5173`

### 4. Start the Student Edge Tracker
In a new terminal window (with virtual environment activated):

- **Option A — Python Native Tracker (Tkinter Focus Companion):**
  ```bash
  python -m client
  ```
- **Option B — Electron Desktop Tracker:**
  ```bash
  cd electron-tracker
  npm start
  ```

---

## 8. Docker Deployment (Alternative)
You can build and run both the MongoDB instance and FastAPI backend in Docker containers:

```bash
docker compose up --build
```
This spins up MongoDB on port `27017` and FastAPI on port `8000`.
