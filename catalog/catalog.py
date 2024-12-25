import os
import ast
import json

def get_python_functions(file_path):
    functions = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            tree = ast.parse(file.read(), filename=file_path)
            functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
    except Exception as e:
        print(f"Error parsing {file_path}: {e}")
    return functions

def list_dir_structure(base_dir):
    result = {}
    for root, dirs, files in os.walk(base_dir):
        # Ignore .git directory or any git-related files
        dirs[:] = [d for d in dirs if d != ".git"]
        files = [f for f in files if not f.startswith(".git")]

        python_files = [f for f in files if f.endswith(".py")]
        result[root] = {
            "python_files": python_files,
            "functions": {f: get_python_functions(os.path.join(root, f)) for f in python_files}
        }
    return result

if __name__ == "__main__":
    base_directory = input("Enter the base directory path: ").strip()
    output_file = input("Enter the output JSON file path: ").strip()

    data = list_dir_structure(base_directory)
    with open(output_file, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4)

    print(f"Directory structure and Python functions written to {output_file}")
