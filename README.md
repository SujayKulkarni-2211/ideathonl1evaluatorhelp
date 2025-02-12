# 📊 Ideathon PPT Evaluation System

A **Flask-based web application** for **evaluating PPTs** in an Ideathon.  
This system enables **AI-based PPT scoring, user authentication, and admin panel** functionalities.

---

## 🚀 Features

### 👤 User Authentication
✅ **Admin & User roles**  
✅ **Admin can add users**  
✅ **Users can log in and upload PPTs**  

### 📊 AI-Based PPT Evaluation
✅ **Uses Google Gemini API to score presentations**  
✅ **Evaluates based on predefined weighted criteria**  
✅ **Categorizes teams into Red, Orange, and Green Panels**  

### 📂 Team Categorization
✅ **Red Panel** → Scores below **60% in any category** (Immediate Rejection)  
✅ **Orange Panel** → Needs manual review (image-heavy presentations)  
✅ **Green Panel** → **Auto-qualified teams**, sorted by highest score  

### 🔍 Admin Controls
✅ **Admin can add new users**  
✅ **Admins & Judges can review Orange-flagged teams**  
✅ **Move teams between categories** (Red → Orange, Orange → Green)  
✅ **Download uploaded PPTs** for manual review  

---

## 📜 Pre-requisites

1. **Python 3.8+** installed
2. **Google Gemini API Key** (See [Google Gemini API Docs](https://ai.google.dev/docs))

---

## 📂 Project File Structure

```
📁 ideathon-app/
├── app.py                 # Flask Backend
├── ai_evaluator.py        # AI Evaluation Logic
├── config.py             # Stores API keys & settings
├── schema.sql            # Database Schema
├── requirements.txt      # Dependencies
├── .gitignore           # Ignore sensitive files
├── README.md            # Project Documentation
├── 📁 templates/        # HTML Templates (Flask views)
│   ├── login.html
│   ├── admin.html
│   ├── upload.html
│   ├── view_category.html
│   └── dashboard.html
└── 📁 static/uploads/   # Uploaded PPTs (ignored in Git)
```

---

## ⚙️ Configuration (`config.py`)

Before running the app, **set the following values** in `config.py`:

```python
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
DATABASE = "database.db"
UPLOAD_FOLDER = "static/uploads"
ALLOWED_EXTENSIONS = {"ppt", "pptx"}
ADMIN_USERNAME = "YOUR_ADMIN_USERNAME"
ADMIN_PASSWORD = "YOUR_SECURE_PASSWORD"
SECRET_KEY = "YOUR_SECRET_KEY"
```

🔹 **Replace `YOUR_GEMINI_API_KEY`** with your **Google Gemini API Key**
   - Get your Gemini API Key from [Google Gemini API Docs](https://ai.google.dev/docs)

🔹 **Set a secure `ADMIN_USERNAME` and `ADMIN_PASSWORD`** (Do not use default values)
   - This is the **first admin login** to access the portal and add users

🔹 **Ensure `SECRET_KEY` is kept safe** (used for Flask session management)

---

## 🚫 Git Ignore Policy

To **protect sensitive files**, the following files are **ignored from Git commits**:

```
# Sensitive files
config.py
database.db

# Generated files
__pycache__/
*.pyc
*.pyo

# Upload directory
static/uploads/*
!static/uploads/.gitkeep

# Environment files
.env
venv/
```

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Ideathon-PPT-Evaluation.git
cd Ideathon-PPT-Evaluation
```

### 2. Install Dependencies

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

### 3. Initialize Database

```bash
python app.py
```

This will:
- Create the SQLite database
- Set up required tables
- Generate the admin user with credentials from `config.py`

### 4. Run the Application

```bash
python app.py
```

Access the application at: `http://127.0.0.1:5000`

---

## 🎯 How to Use

### 👑 Admin Role

1. **Login** using admin credentials from `config.py`
2. **Add Users:**
   - Navigate to "User Management"
   - Create accounts for judges and team members
   - Set appropriate role permissions
3. **Review Teams:**
   - Access "Orange Panel" for manual review
   - Move teams between categories based on review
4. **Download PPTs:**
   - Available in team details view
   - Use for offline evaluation

### 👤 User Role

1. **Login** with credentials provided by admin
2. **Upload PPT:**
   - Click "Upload Presentation"
   - Select PPT/PPTX file
   - Submit for evaluation
3. **View Results:**
   - Check evaluation status
   - See category assignment (Red/Orange/Green)
   - View detailed scoring breakdown

---

## 🌟 Contribution Guidelines

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Follow PEP 8 style guidelines
4. Write clear commit messages
5. Submit a Pull Request with detailed description

### Issue Reporting
- Use the GitHub Issues tab
- Include steps to reproduce
- Attach relevant screenshots/logs

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📌 Additional Notes

### Security Best Practices
- Change default admin credentials immediately
- Use strong passwords
- Keep `config.py` secure
- Regularly update dependencies
- Monitor API usage

### Deployment
For production deployment instructions, see our [Deployment Guide](docs/deployment.md)

### Support
For questions or support:
- Create a GitHub Issue
- Contact the maintainers
- Check documentation in `/docs`

---

*Made with ❤️ for Ideathons*