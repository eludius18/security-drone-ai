# 🚀 Security Drone AI - Autonomous Surveillance with AI & RL

## 📌 Project Overview
**Security Drone AI** is an AI-powered autonomous surveillance system that detects intruders using **YOLOv8 (object detection)** and **Reinforcement Learning (RL) to optimize drone patrol routes**. The system integrates a **DJI Mini 3 drone and a Wansview 2K Solar Camera** for real-time monitoring, AI-based decision-making, and automatic threat response.

## 🎯 Features
✅ **Real-Time Intrusion Detection**  
   - Detects people and vehicles using **YOLOv8** (PyTorch)  
✅ **Autonomous Drone Patrol**  
   - Uses **Reinforcement Learning (DQN)** to optimize patrol routes  
✅ **Smart Decision Making**  
   - AI-based logic decides when the drone should investigate an alert  
✅ **Telegram Alerts**  
   - Sends real-time alerts with detected threats  
✅ **Modular & Scalable**  
   - Fully modular Python architecture with API, AI, and drone control  
✅ **Docker Support**  
   - Easy deployment with **Docker & Flask API**  

## 📂 Project Structure
```
security-drone/
│── src/
│   ├── camera/                 # 📸 Camera module (IP Camera integration)
│   │   ├── ip_camera.py
│   ├── detection/              # 🎯 AI-powered detection using YOLOv8
│   │   ├── detector.py
│   │   ├── model_loader.py
│   ├── drone/                  # 🚁 DJI Mini 3 autonomous control
│   │   ├── drone_controller.py
│   ├── alerts/                 # 📩 Telegram alerts module
│   │   ├── telegram_alert.py
│   ├── database/               # 🗄 Logs and event storage (MongoDB)
│   │   ├── database.py
│   ├── reinforcement_learning/ # 🧠 Reinforcement Learning (Deep Q-Learning)
│   │   ├── drone_env.py
│   │   ├── train_agent.py
│   │   ├── run_agent.py
│   ├── api/                    # 🌐 Flask API server
│   │   ├── server.py
│   ├── main.py                 # 🚀 Main execution script
│── tests/                      # 🧪 Unit tests
│── config/                     # ⚙️ Configuration files
│── docker/                     # 🐳 Docker setup
│── .env                        # 🌱 Environment variables
│── .env.example                # 📄 Example environment variables file
│── README.md                   # 📖 Documentation
│── requirements.txt             # 📦 Python dependencies
```

## 🔧 Technologies Used
- **Python 3.9+** for backend and AI logic
- **YOLOv8 (Ultralytics, PyTorch-based)** for real-time object detection
- **Flask** for API communication
- **MongoDB** for logging detections and drone activity
- **DJI Mobile SDK** for drone control
- **Stable-Baselines3 (DQN, Reinforcement Learning)** for AI-powered patrol optimization
- **OpenCV** for camera stream processing
- **Docker** for easy deployment
- **Telegram API** for real-time alerts

## 🚀 How the System Works
1. **Camera Stream & Detection**:
   - The **Wansview 2K Solar Camera** streams live video.
   - **YOLOv8** processes images in real-time to detect **intruders** (people, vehicles, etc.).
   - If an **intruder is detected**, the system logs the event in MongoDB and triggers an alert.

2. **Autonomous Drone Response**:
   - The **DJI Mini 3 drone** is automatically deployed if an intrusion is detected.
   - The drone follows a **pre-learned patrol route**, optimized via **Reinforcement Learning (DQN)**.
   - It records footage and sends it back to the system.
   - The system **evaluates the risk** and sends updates to the user.

3. **Alert System**:
   - When an intruder is detected, the system **sends a real-time alert to Telegram**.
   - The alert includes **a photo of the intruder**, detection confidence, and timestamp.

4. **Data Logging & AI Learning**:
   - Every event is stored in **MongoDB** for historical analysis.
   - The reinforcement learning model **continuously improves patrol efficiency** based on new data.

## 📄 Environment Variables
Before running the project, configure your `.env` file using the provided `.env.example`. This ensures that all necessary API keys and database connections are set up correctly.

### 📌 `.env.example`
```env
# MongoDB Database
MONGO_URI=mongodb://your_mongo_uri

# IP Camera Configuration
CAMERA_URL=rtsp://user:password@your_camera_ip:554/live/ch0

# Telegram Bot Credentials for Alerts
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
CHAT_ID=your_chat_id
```

## 🚀 Running the System
### **1. Start the System**
```bash
python src/main.py
```

## 📜 License
This project is **MIT Licensed** - feel free to modify and improve!

---
🚀 **Ready to deploy an AI-powered autonomous security system? Let's build the future together!**