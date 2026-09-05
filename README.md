# Rule-Based Student Performance Analysis and Improvement Agent

## 📌 Project Overview

The **Rule-Based Student Performance Analysis and Improvement Agent** is a simple AI-based Python project that analyzes a student's performance using:

* Attendance Percentage
* Internal Marks
* Assignment Marks

The agent uses predefined rules to predict the student's performance and identifies areas where the student needs improvement.

### Performance Categories

The agent provides one of the following results:

* **Excellent Performance**
* **Good Performance**
* **Needs Improvement**

It also provides specific suggestions for improving attendance, internal marks, and assignment marks.

---

# 🛠️ Technologies Used

* **Python**
* **Visual Studio Code**
* **Git**
* **GitHub**

No external Python libraries are required for this project.

---

# 📂 Project Structure

```text
IAI-SLE1-YourPRN/
│
├── studentPerformenceAgent.py
├── AI_Contribution_Log.md
└── README.md
```

### File Description

| File                           | Description                                              |
| ------------------------------ | -------------------------------------------------------- |
| `studentPerformenceAgent.py` | Main Python program                                      |
| `AI_Contribution_Log.md`       | Documentation of AI assistance and personal contribution |
| `README.md`                    | Project information and execution steps                  |

---

# 💻 Requirements

Before running the project, make sure Python is installed on your computer.

You can check whether Python is installed by opening **Command Prompt** or the **VS Code Terminal** and entering:

```bash
python --version
```

Example:

```text
Python 3.12.5
```

If Python is not installed, download it from:

https://www.python.org/downloads/

During Python installation, make sure to select:

```text
Add Python to PATH
```

---

# 🚀 Steps to Run the Project

## Step 1: Download or Clone the Repository

Open the GitHub repository and click:

**Code → HTTPS → Copy**

Then open the VS Code terminal and run:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Example:

```bash
git clone https://github.com/YourUsername/IAI-SLE1-YourPRN.git
```

Move into the project folder:

```bash
cd IAI-SLE1-YourPRN
```

---

## Step 2: Open the Project in VS Code

Open Visual Studio Code.

Select:

```text
File → Open Folder
```

Choose the downloaded project folder.

The project should contain:

```text
studentPerformenceAgent.py
AI_Contribution_Log.md
README.md
```

---

## Step 3: Open the Python File

Open:

```text
studentPerformenceAgent.py
```

This is the main program file.

---

## Step 4: Run the Program

Open the VS Code terminal:

```text
Terminal → New Terminal
```

Run:

```bash
python studentPerformenceAgent.py
```

---

# ⌨️ Step 5: Enter Student Details

The program will ask for three inputs.

### 1. Attendance Percentage

Example:

```text
Enter attendance percentage: 65
```

### 2. Internal Marks

Example:

```text
Enter internal marks: 55
```

### 3. Assignment Marks

Example:

```text
Enter assignment marks: 50
```

---

# 📊 Step 6: View the Result

After entering the details, the agent analyzes the values using predefined rules.

Example output:

```text
--- Student Performance Report ---

Attendance: 65.0 %
Internal Marks: 55.0
Assignment Marks: 50.0

Performance Prediction: Good Performance

What You Need to Improve:
- Improve attendance to at least 75%.
- Improve internal marks by studying regularly.
- Complete assignments properly and improve assignment marks.
```

---

# 🧠 How the AI Agent Works

The project uses a **rule-based approach**.

The agent checks the student's values against predefined conditions.

```text
Student Data
     ↓
Attendance
Internal Marks
Assignment Marks
     ↓
Apply Predefined Rules
     ↓
Performance Prediction
     ↓
Identify Weak Areas
     ↓
Improvement Suggestions
```

---

# 📋 Performance Rules

| Condition                                             | Prediction            |
| ----------------------------------------------------- | --------------------- |
| Attendance ≥ 75 AND Internal ≥ 75 AND Assignment ≥ 75 | Excellent Performance |
| Attendance ≥ 60 AND Internal ≥ 50 AND Assignment ≥ 50 | Good Performance      |
| Otherwise                                             | Needs Improvement     |

---

# 💡 Improvement Rules

The agent checks each performance area separately.

### Attendance

If:

```text
Attendance < 75%
```

The agent suggests:

```text
Improve attendance to at least 75%.
```

### Internal Marks

If:

```text
Internal Marks < 75
```

The agent suggests:

```text
Improve internal marks by studying regularly.
```

### Assignment Marks

If:

```text
Assignment Marks < 75
```

The agent suggests:

```text
Complete assignments properly and improve assignment marks.
```

---

# 🧪 Sample Test Cases

## Test Case 1 – Excellent Performance

### Input

```text
Attendance: 90
Internal Marks: 85
Assignment Marks: 90
```

### Output

```text
Performance Prediction: Excellent Performance

What You Need to Improve:
- Excellent! Maintain your current performance.
```

---

## Test Case 2 – Good Performance

### Input

```text
Attendance: 65
Internal Marks: 85
Assignment Marks: 90
```

### Output

```text
Performance Prediction: Good Performance

What You Need to Improve:
- Improve attendance to at least 75%.
```

---

## Test Case 3 – Multiple Improvements Required

### Input

```text
Attendance: 60
Internal Marks: 55
Assignment Marks: 50
```

### Output

```text
Performance Prediction: Good Performance

What You Need to Improve:
- Improve attendance to at least 75%.
- Improve internal marks by studying regularly.
- Complete assignments properly and improve assignment marks.
```

---

# ⚠️ Troubleshooting

## Problem: Python is not recognized

If you see:

```text
'python' is not recognized as an internal or external command
```

Install Python and make sure **Add Python to PATH** is selected during installation.

You can also try:

```bash
py studentPerformenceAgent.py
```

---

## Problem: File not found

Make sure the terminal is inside the project folder.

Check the files using:

```bash
dir
```

You should see:

```text
studentPerformenceAgent.py
README.md
AI_Contribution_Log.md
```

Then run:

```bash
python studentPerformenceAgent.py
```

---

# 📌 Project Limitations

* The agent uses predefined rules.
* It does not use machine learning.
* It does not learn from previous student data.
* The prediction is based only on attendance, internal marks, and assignment marks.
* Improvement suggestions are based on fixed conditions.

---

# 👩‍💻 Author

**Name:** YOUR NAME
**PRN:** YOUR PRN
**Course:** 02AML204 – Introduction to Artificial Intelligence
**Semester:** VI

---

# 📄 SLE-1 Documentation

This project is prepared as part of **SLE-1: Tooling & AI Contribution Log Setup**.

The repository contains:

* Working AI-related Python code
* AI Contribution Log
* Project README
* GitHub repository history

The `AI_Contribution_Log.md` file documents the AI tools used, AI-assisted portions, personal contribution, and issues/fixes.

---

# ✅ Quick Run Command

After cloning the repository, simply run:

```bash
cd IAI-SLE1-YourPRN
python studentPerformenceAgent.py
```

Then enter:

```text
Attendance Percentage
Internal Marks
Assignment Marks
```

The agent will display the **performance prediction and improvement suggestions**.