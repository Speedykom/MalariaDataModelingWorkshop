# IGAD Malaria & Disease Dashboard Project

Click [here](https://speedykom.github.io/Seans_presentation/#/title-slide) to view the presentation.


## Aider + uv Workflow Guide

This document outlines the step-by-step process used to build the IGAD Streamlit dashboard using uv (for package management) and Aider (AI pair programmer) with the Gemini 1.5 Pro model.

---

## 1. Installation & Setup

### Install Tools

First, we installed the necessary tools. `uv` is used for fast Python package management, and it is used to install Aider.

#### 1. Install uv

**Windows (using winget):**

```bash
winget install --id astral-sh.uv
```

**macOS & Linux (Ubuntu):**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### 2. Install Aider globally using uv

```bash
uv tool install aider-chat
```

### Project Initialization

We created a project directory and initialized a standard Python environment.

```bash
mkdir igad-dashboard
cd igad-dashboard
uv init
```

---

## 2. Configuration

We created a configuration file to manage the Gemini API key and Git behavior.

### Get Gemini API Key

Before configuring Aider, you need an API key from Google.

1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Click **Create API Key**
3. Copy the key string (it typically starts with `AIza...`)

### Create Config File

Create a file named `.aider.conf.yml` in your project root and paste your key below.

**File: `.aider.conf.yml`**

```yaml
# Model Selection
model: gemini/gemini-1.5-pro-latest

# Git Settings: Disable auto-commit to allow manual review
auto-commits: false

# API Key Configuration
api-key:
  - gemini=YOUR_ACTUAL_API_KEY_HERE
```

### Launch Command

We launch Aider ensuring it doesn't auto-commit (redundant with config, but good practice):

```bash
aider --no-auto-commits
```

---

## 3. The Development Workflow

### Step A: Context & Requirements (The "Expert" Persona)

We started by adding the raw data files and a target PRD file to the chat context. This allowed Aider to see the actual column headers in our CSVs.

**Aider Command:**

```bash
/add context/PRD.md data/dj_et_ke_so_ss_sd_ug_NationalUnit-data.csv data/flu_weather_dataset.csv
```

**The Prompt:**

```
You are an expert Data Scientist working for The Intergovernmental Authority on Development (IGAD) in Eastern Africa.

We need to prepare a high-level presentation for IGAD leadership regarding the current state of malaria and other diseases in the region.

Please fill out the `context/PRD.md` file to outline the requirements for a new Streamlit application.

The application must:
1. Allow users to upload new CSV files that match the schema/headings of the two files in the `data/` folder (which represent National Unit data and Flu/Weather data).
2. Automatically perform Exploratory Data Analysis (EDA) upon file upload.
3. Generate visualizations relevant to the IGAD region (Djibouti, Ethiopia, Kenya, Somalia, South Sudan, Sudan, Uganda) to highlight disease trends and weather correlations.

Analyze the columns in the provided data files to ensure the PRD technical specifications are accurate.
```

### Step B: Freezing the Spec

Once the PRD was generated, we locked it to prevent the AI from changing the requirements later.

**Aider Command:**

```bash
/read-only context/PRD.md
```

### Step C: Planning & TDD

We instructed Aider to break the work into small, testable tasks.

**The Prompt:**

```
Create a markdown file with the tasks to complete the PRD. Make each task concrete, use TDD as per PRD. Give each task a number. Also, put a checkmark ('[ ]') next to each task to track completion.
```

### Step D: The Loop

We entered a loop where we simply told Aider to move to the next item in the checklist it just created.

**The Prompt:**

```
Please proceed to the next task.
```

---

## 4. Running the Application

Once Aider finished writing the `app.py` code, we used `uv` to handle dependencies and execution.

### Install Dependencies

We added the libraries required by the generated code:

```bash
uv add streamlit pandas matplotlib seaborn
```

### Launch the App

We used `uv run` to execute Streamlit inside the isolated virtual environment:

```bash
uv run streamlit run app.py
```

---

## Summary

This workflow demonstrates how to leverage modern Python tooling (`uv`) and AI-assisted development (Aider with Gemini 1.5 Pro) to rapidly build a data-focused Streamlit application. The key principles are:

- **Context-aware AI**: Feed real data files to Aider for accurate schema understanding
- **Specification locking**: Use `/read-only` to prevent scope creep
- **Task decomposition**: Break complex projects into small, testable units
- **Iterative development**: Use a simple loop to progress through tasks
- **Isolated environments**: Use `uv` for reproducible dependency management
