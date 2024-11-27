import os

# Define the directory structure
directory_structure = {
    "data-processing-NSE ": {
        "config": ["__init__.py", "settings.py"],
        "data": {
            "raw": [],
            "processed": [],
            "eda": []
        },
        "import": ["__init__.py", "nse_importer.py", "api_connector.py", "file_importer.py"],
        "models": {
            "__init__.py": [],
            "time_series": ["__init__.py", "arima.py", "prophet.py"],
            "machine_learning.py": [],
            "deep_learning.py": []
        },
        "preprocessing": ["__init__.py", "data_preprocessor.py"],
        "strategies": ["__init__.py", "strategy_evaluator.py"],
        "utils": ["__init__.py", "backtest.py", "cross_validation.py", "metrics.py"],
        "deploy": ["__init__.py", "trading_bot.py"],
        "logs": ["eda.log", "model_training.log", "trading.log"],
        "docs": ["README.md"]
    }
}

# Function to create directories and files
def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            os.makedirs(base_path, exist_ok=True)
            for file in content:
                file_path = os.path.join(path, file)
                open(file_path, "w").close()  # Create empty file

# Create the directory structure
def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name.strip())  # Ensure no trailing spaces
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            print(f"Created directory: {path}")  # Debug log
            create_structure(path, content)
        else:
            os.makedirs(base_path, exist_ok=True)
            for file in content:
                file_path = os.path.join(path, file.strip())  # Ensure no trailing spaces
                print(f"Creating file: {file_path}")  # Debug log
                open(file_path, "w").close()  # Create empty file


print("Directory structure created successfully!")
