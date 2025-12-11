IGAD Malaria & Disease Dashboard ProjectClick here to view the presentation.🚀 Overview: Modern Python Development WorkflowThis project outlines a fast, reliable, and AI-assisted workflow for building data dashboards, leveraging powerful tools like uv, Aider, and Streamlit, powered by OpenRouter for unified LLM access.Key ToolsToolRoleDescription⚡ uvPackage ManagerExtremely fast Python package installer and project manager, written in Rust.🤖 AiderAI Pair ProgrammerTerminal-based AI tool that edits files, integrates with Git, and works with the entire codebase context.🎯 OpenRouterLLM GatewayProvides unified API access to various high-quality LLMs (like Deepseek and Gemini) via a single API key.📊 StreamlitDashboard FrameworkSimplifies the creation of interactive data applications and dashboards in pure Python.1. Installation & Setup1.1 Install uvuv is essential for managing virtual environments and dependencies quickly.Windows (using winget):winget install --id astral-sh.uv
macOS & Linux (Ubuntu):curl -LsSf [https://astral.sh/uv/install.sh](https://astral.sh/uv/install.sh) | sh
Verify Installation:uv --version
1.2 Install Aider GloballyWe install Aider as a global tool using uv to ensure it is always available.uv tool install aider-chat --python 3.12 --force
2. Project InitializationIf you are following along with the workshop, clone or download the repository files:git clone [https://github.com/Speedykom/MalariaDataModelingWorkshop](https://github.com/Speedykom/MalariaDataModelingWorkshop)
cd MalariaDataModelingWorkshop
3. Configuration3.1 Configure OpenRouter API KeyWe use OpenRouter for its unified access to multiple high-performance models and its privacy features.Navigate to https://openrouter.ai/ to get your API Key.Set up your key in the Aider configuration file.3.2 Create Aider Config FileRename the example configuration file and insert your API key.Rename example.aider.conf.yml to .aider.conf.yml.Edit the file to include your OpenRouter API Key and set your preferred model..aider.conf.yml template:# ~/.aider.conf.yml

# 1. Add your openRouter API key
api-key: # insert YOUR_OPENROUTER_API_KEY below
 - openrouter=sk-...
 
# 2. Set your default model (e.g., Deepseek or Mistral)
model: openrouter/mistralai/devstral-2512:free

# 3. Optional: Enable caching to save on costs
cache-prompts: true
3.3 SecurityProtect your configuration file by adding it to .gitignore:# Add to .gitignore
.aider.conf.yml
.env
*.env
4. Installing DependenciesUse uv sync to install all project dependencies defined in pyproject.toml into a dedicated virtual environment.uv sync
5. The Development Workflow with AiderThe recommended workflow follows a four-step process for AI-assisted development:5.1 Launch AiderStart the AI pair programmer in your project directory:aider --no-auto-commits
(Use --no-auto-commits initially if you want to review changes before they are committed.)5.2 The Four-Step Aider ProcessContext & Requirements: Set up the "Expert" persona and paste the detailed requirements from your PROMPT.md file.Freeze the Spec: Lock the PRD to prevent the AI from changing core requirements./read-only context/PRD.md
Planning & TDD: Break the work into small, testable tasks (often done automatically based on the prompt).The Loop: Iterate through tasks by simply asking Aider to proceed.Please proceed to the next task.
5.3 Essential Aider CommandsCommandDescription/add file.pyAdd a file to the current context for editing/reference./read-only file.pyAdd a file to the context but prevent AI modifications./drop file.pyRemove a file from the context./lsList files currently in the context./undoUndo the last change made by Aider./exitExit the Aider session.6. Running the ApplicationOnce your app.py is developed, run the Streamlit dashboard using uv run. This automatically activates the virtual environment and launches the application.uv run streamlit run app.py
7. Resourcesuv Documentation: https://docs.astral.sh/uv/OpenRouter: https://openrouter.ai/Aider Documentation: https://aider.chat/docsStreamlit Documentation: https://docs.streamlit.io
