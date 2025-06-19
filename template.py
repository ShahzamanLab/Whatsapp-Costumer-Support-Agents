import os
from pathlib import Path

list_of_files = [
    "app/__init__.py",
    "app/main.py",
    "app/chatbot_logic.py",
    "app/twilio_handler.py",
    "app/utils.py",
    "app/config.py",

    "agents/__init__.py",
    "agents/support_agent.py",

    "prompts/support_prompt.txt",
    "data/faqs.txt",

    "tests/__init__.py",
    "tests/test_chatbot_logic.py",
    "tests/test_twilio_handler.py",

    ".env",
    ".gitignore",
    "Dockerfile",
    "docker-compose.yml",
    "requirements.txt",
    "setup.py",
    "README.md",
    "LICENSE",
    "langchain.yaml",
    "tunnel.py"
]

for file_path in list_of_files:
    file = Path(file_path)
    dir_name, file_name = os.path.split(file)

    if dir_name:
        os.makedirs(dir_name, exist_ok=True)

    if not os.path.exists(file) or os.path.getsize(file) == 0:
        with open(file, 'w') as f:
            f.write("")  
    else:
        print(f"File already exists: {file}")
