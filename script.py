import json
import os

json_file_path = 'permissions.json'

permission_scores = {
    'r': 1,
    'i': 2,
    'w': 3,
    'x': 5
}

def calculate_score(perm_string):
    total_score = 0
    for perm in perm_string:
        total_score += permission_scores.get(perm, 0)
    return total_score

def get_common_folder(all_paths):
    common_folder = os.path.commonprefix(all_paths)
    return os.path.dirname(common_folder)

def main():
    try:
        with open(json_file_path, 'r') as file:
            permissions_data = json.load(file)

      
        all_file_paths = list(permissions_data.keys())
        common_folder = get_common_folder(all_file_paths)
        
        total_score = 0
        
        for file_path, file_permissions in permissions_data.items():

            file_score = sum(calculate_score(perm_string) for perm_string in file_permissions.values())

            total_score += file_score
        

        print(f"The total permissions score for files in folder '{common_folder}' is: {total_score}")
    
    except FileNotFoundError:
        print(f"Error: The file '{json_file_path}' does not exist.")
    except json.JSONDecodeError:
        print("Error: The file is not a valid JSON file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
