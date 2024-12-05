import os
import yaml
import sys

def get_folder_structure(path):
    folder_structure = {}
    for root, dirs, files in os.walk(path):
        folder = os.path.relpath(root, path)
        folder_structure[folder] = {'dirs': dirs, 'files': files}
    return folder_structure

def save_to_yaml(data, output_file):
    with open(output_file, 'w') as file:
        yaml.dump(data, file, default_flow_style=False)

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <path>")
        sys.exit(1)
    
    path = sys.argv[1]
    output_file = "folder_structure.yaml"
    folder_structure = get_folder_structure(path)
    save_to_yaml(folder_structure, output_file)
    print(f"Folder structure saved to {output_file}")

if __name__ == "__main__":
    main()
