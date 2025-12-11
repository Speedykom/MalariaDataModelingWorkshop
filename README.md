# IGAD Malaria & Disease Dashboard Project

[Click here to view the presentation.](https://Speedykom.github.io/MalariaDataModelingWorkshop/)

## 🚀 Overview: Modern Python Development Workflow

This project outlines a fast, reliable, and AI-assisted workflow for building data dashboards, leveraging powerful tools like **uv**, **Aider**, and **Streamlit**, powered by **OpenRouter** for unified LLM access.

## Key Tools

| Tool | Role | Description |
|------|------|-------------|
| ⚡ **uv** | Package Manager | Extremely fast Python package installer and project manager, written in Rust. |
| 🤖 **Aider** | AI Pair Programmer | Terminal-based AI tool that edits files, integrates with Git, and works with the entire codebase context. |
| 🎯 **OpenRouter** | LLM Gateway | Provides unified API access to various high-quality LLMs (like Deepseek and Gemini) via a single API key. |
| 📊 **Streamlit** | Dashboard Framework | Simplifies the creation of interactive data applications and dashboards in pure Python. |

## 1. Installation & Setup

### 1.1 Install uv

`uv` is essential for managing virtual environments and dependencies quickly.

**Windows (using winget):**
```bash
winget install --id astral-sh.uv
```

**macOS & Linux (Ubuntu):**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Verify Installation:**
```bash
uv --version
```

### 1.2 Install Aider Globally

We install Aider as a global tool using `uv` to ensure it is always available.

```bash
uv tool install aider-chat --python 3.12 --force
```

## 2. Project Initialization

If you are following along with the workshop, clone or download the repository files:

```bash
git clone https://github.com/Speedykom/MalariaDataModelingWorkshop
cd MalariaDataModelingWorkshop
```

## 3. Configuration

### 3.1 Configure OpenRouter API Key

We use OpenRouter for its unified access to multiple high-performance models and its privacy features.

1. Navigate to https://openrouter.ai/ to get your API Key.
2. Set up your key in the Aider configuration file.

### 3.2 Create Aider Config File

Rename the example configuration file and insert your API key.

1. Rename `example.aider.conf.yml` to `.aider.conf.yml`.
2. Edit the file to include your OpenRouter API Key and set your preferred model.

**`.aider.conf.yml` template:**
```yaml
# ~/.aider.conf.yml

# 1. Add your openRouter API key
api-key:
 - openrouter=sk-...
 
# 2. Set your default model (e.g., Deepseek or Mistral)
model: openrouter/mistralai/devstral-2512:free

# 3. Optional: Enable caching to save on costs
cache-prompts: true
```

### 3.3 Security

Protect your configuration file by adding it to `.gitignore`:

```gitignore
# Add to .gitignore
.aider.conf.yml
.env
*.env
```

## 4. Installing Dependencies

Use `uv sync` to install all project dependencies defined in `pyproject.toml` into a dedicated virtual environment.

```bash
uv sync
```

## 5. The Development Workflow with Aider

The recommended workflow follows a four-step process for AI-assisted development:

### 5.1 Launch Aider

Start the AI pair programmer in your project directory:

```bash
aider --no-auto-commits
```

(Use `--no-auto-commits` initially if you want to review changes before they are committed.)

**You'll see:**

```
Aider v0.x.x
Model: gemini/gemini-1.5-pro-latest
Git repo: .git
>
```

#### Troubleshooting: If the Launch Fails

If the basic `aider` command doesn't work (particularly on some Windows systems), try this alternative:

```bash
uv run --with aider-chat python -m aider --model openrouter/<Model-Name> --api-key openrouter=YOUR_OPENROUTER_API_KEY
```

Replace `<Model-Name>` with your desired model (e.g., `Deepseek/deepseek-v3.2` or `mistralai/devstral-2512:free`) and `YOUR_OPENROUTER_API_KEY` with your actual OpenRouter API key.

### 5.2 The Four-Step Aider Process

1. **Context & Requirements:** Set up the "Expert" persona and paste the detailed requirements from your `PROMPT.md` file.
2. **Freeze the Spec:** Lock the PRD to prevent the AI from changing core requirements.
   ```
   /read-only context/PRD.md
   ```
3. **Planning & TDD:** Break the work into small, testable tasks (often done automatically based on the prompt).
4. **The Loop:** Iterate through tasks by simply asking Aider to proceed.
   ```
   Please proceed to the next task.
   ```

### 5.3 Essential Aider Commands

| Command | Description |
|---------|-------------|
| `/add file.py` | Add a file to the current context for editing/reference. |
| `/read-only file.py` | Add a file to the context but prevent AI modifications. |
| `/drop file.py` | Remove a file from the context. |
| `/ls` | List files currently in the context. |
| `/undo` | Undo the last change made by Aider. |
| `/exit` | Exit the Aider session. |

## 6. Running the Application

Once your `app.py` is developed, run the Streamlit dashboard using `uv run`. This automatically activates the virtual environment and launches the application.

```bash
uv run streamlit run app.py
```

## 7. Resources

- **uv Documentation:** https://docs.astral.sh/uv/
- **OpenRouter:** https://openrouter.ai/
- **Aider Documentation:** https://aider.chat/docs
- **Streamlit Documentation:** https://docs.streamlit.io

---

**Happy coding! 🎉**