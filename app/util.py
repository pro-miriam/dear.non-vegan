import json
import os
import shutil

script_directory = os.path.dirname(os.path.realpath(__file__))
folder_path = os.path.join(script_directory, 'assets', 'meta')
image_path = os.path.join(script_directory, 'assets', 'images')
board_path = os.path.join(folder_path, 'board_list.json')

def read_board_list():
    global file_path
    with open(board_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data

def write_to_board_list(data):
    global file_path
    with open(board_path, 'w') as file:
        json.dump(data, file, indent=2)

def copy_file(path, name) :
    shutil.copy(path, image_path)
    return 'images/' + name