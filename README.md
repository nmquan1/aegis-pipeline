# 🛡️ AEGIS AI Pipeline

This repository contains the **AI Pipeline** powering the **SafeSpace** application, built with **Flask**. It provides natural language processing capabilities such as sentiment and friendliness analysis.

---

## 📋 Requirements

To run this project, ensure you have the following:

- 🐍 **Python 3.10 or higher**

---

## ⚙️ Setup Instructions

Follow these step-by-step instructions to get the pipeline up and running on your machine.

---

### 1️⃣ Clone the Repository

📥 Clone the repository to your local machine using `git`:
```bash
git clone https://github.com/nmquan1/aegis-pipeline.git
cd aegis-pipeline
```
This will download the project and navigate you into its directory.

---

### 2️⃣ Install Dependencies

📦 Install all required Python packages listed in the `requirements.txt` file:
```bash
pip install -r requirements.txt
```
This step ensures that all necessary libraries and tools are available for the app to run correctly.

---

### 3️⃣ Configure Environment Variables

🔐 Create a `.env` file in the root of the project and add your Gemini API key like this:
```env
API=your_gemini_api_key
The application uses this key to access Gemini services. Keep your key secure and do not share it publicly.
```
---

### 4️⃣ Run the Application

🚀 Start the Flask server with the following command:
bash
python app.py
By default, the application will start locally at:

http://localhost:5000
You can now interact with the AI pipeline through this local endpoint.

---

## 📂 Project Structure

Here's a quick overview of how the project is organized:
```bash
aegis-pipeline/
├── app.py              # Main Flask application entry point
├── pipeline/           # Core AI logic and model pipeline
├── utils/              # Utility functions and helpers
├── requirements.txt    # List of required Python packages
├── .env                # Environment variables file (not committed)
└── README.md           # Project documentation
```
---

## 🚧 Current Status

The pipeline is currently intended to be run locally for **development and testing purposes**.

---

## 🤝 Contributing

Interested in contributing?

1. 🍴 Fork the repository
2. 🛠️ Create a new feature branch
3. ✅ Commit your changes
4. 🚀 Open a pull request for review

All contributions and feedback are appreciated!

---

## 📝 License

This project is licensed under the **MIT License**.
