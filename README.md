# AI Learning Intelligence Tool

## Overview
This project is an AI-powered Learning Intelligence Tool that analyzes student learning behavior
and provides predictions and actionable insights for mentors and administrators.

The system predicts course completion, identifies dropout risk, and detects difficult chapters.
Models are trained offline and used for inference through a CLI-based tool.

---

## Features
- Course completion prediction
- Dropout risk detection
- Chapter difficulty analysis
- Human-readable insights
- Command Line Interface (CLI)

---

## Project Structure
learning_intelligence_tool/
├── README.md
├── requirements.txt
├── data/
│   └── sample_input.csv
├── models/
│   ├── completion_model.pkl
│   └── dropout_model.pkl
├── src/
│   ├── ingestion.py
│   ├── preprocessing.py
│   ├── validation.py
│   ├── features.py
│   ├── train.py
│   ├── inference.py
│   ├── chapter_difficulty.py
│   ├── insights.py
│   └── cli.py
└── tests/
    └── test_core.py

---

## Setup Instructions

### 1. Create Virtual Environment (optional but recommended)
python3 -m venv venv  
source venv/bin/activate

### 2. Install Dependencies
pip install -r requirements.txt

---

## Input Format
Input must be a CSV file with the following columns:
- student_id
- course_id
- chapter_order
- time_spent
- score
- completion_status

Example input file is provided at:
data/sample_input.csv

---

## How to Run the Tool
From the project root directory, run:
python src/cli.py --input data/sample_input.csv

---

## Output
The tool prints an intelligence report in the console containing:
- High-risk students (dropout risk)
- Difficult chapters
- Average course completion prediction

---

## Model Design
- Logistic Regression is used for course completion prediction
- Random Forest is used for dropout risk detection
- Rule-based logic is used for chapter difficulty detection

---

## Reproducibility
- Models are trained offline and saved as .pkl files
- Fixed random seeds ensure consistent predictions
- Same input always produces the same output

---

## Testing
Unit tests are included to validate data checks and feature generation.

Run tests using:
python3 -m pytest tests/


---

## Limitations
- Small dataset used for demonstration
- No real-time streaming support
- CLI-based tool (no graphical UI)

---

## AI Usage Disclosure
AI tools such as ChatGPT were used for architectural guidance and code review.
All machine learning logic, feature engineering, model training, and validation
were implemented and verified independently.

