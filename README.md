# AI Software Engineering Project

## Project Overview
This project is a Security Log Analyzer web application built using Python Flask. 
The application allows users to paste or upload system log entries, automatically 
detects suspicious activity, assigns risk levels (Low, Medium, High), and provides 
explanations with suggested actions.

The goal of this project is to demonstrate how AI can be used as a collaborator 
throughout the Software Development Life Cycle (SDLC), including planning, 
implementation, debugging, and refinement.

---

## Features
- Paste log entries into a text input box
- Upload log files (.txt)
- Detect suspicious patterns such as:
  - Failed login attempts
  - Unauthorized access attempts
  - Repeated login failures (possible brute-force attack)
  - System errors
- Assign risk levels (Low, Medium, High)
- Provide explanations and suggested actions for each log entry

---

## Architecture
- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Python Flask  
- **Detection Logic:** Rule-based pattern matching (AI-assisted design)

---

## AI Tools Used
- **ChatGPT**
  - Project planning and scope definition
  - Code generation (Flask backend + frontend structure)
  - Debugging errors
  - Explaining logic and refining features

---

## AI Interaction Evidence
All screenshots of prompts, iterations, and results are included in the `/screenshots` folder in this repository.

---

## AI Engineering Analysis

### What Worked
- AI quickly generated a working Flask application structure
- Helped implement detection logic and UI layout
- Reduced development time significantly

### What Failed
- Some instructions were unclear or incorrect (especially GitHub file handling)
- Required manual troubleshooting and corrections
- Needed multiple iterations to get working outputs

### Tradeoffs
- Faster development speed vs occasional incorrect or confusing outputs  
- Less manual coding vs more time spent validating AI responses  

---

## Reflection

### What AI Improved
- Accelerated development process
- Helped generate ideas and structure quickly
- Reduced time needed to write boilerplate code

### What AI Made Worse
- Introduced errors that required debugging
- Occasionally gave misleading or incomplete instructions
- Required constant validation instead of blind trust

### What I Would Do Differently
- Use more structured and specific prompts earlier
- Validate AI outputs step-by-step instead of all at once
- Spend more time refining prompts to reduce errors
