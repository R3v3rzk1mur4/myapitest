# This is a simple Flask REST API that takes a GET request with a given file path or directory
# and generates a JSON response. 

from flask import Flask, request, jsonify
import os

app = Flask(__name__)

def get_directory_path():
    # Get the absolute path of the current Python file
    current_file_path = os.path.abspath(__file__)

    # Extract the directory path and remove the file name
    directory_path = os.path.dirname(current_file_path)

    return directory_path

def get_file_info(file_path):    
    # Get file information (size, permissions, and owner) for a given file.
    file_info = os.stat(file_path)
    
    return {
        'size': file_info.st_size,
        'permissions': oct(file_info.st_mode & 0o777),  # Get octal representation of permissions
        'owner': file_info.st_uid,
    }

# Read the file and return its content
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return str(e)
    

@app.route("/", methods=["GET"])
@app.route("/<path:route_param>", methods=["GET"])
def list_directory_contents(route_param=""):
    # List directory content 
    full_path = os.path.join(get_directory_path(), route_param)
    
    if not os.path.exists(full_path):
        return jsonify({"error": "Path not found"}), 404
    
    if os.path.isdir(full_path):
        # List directory contents
        contents = []
        for item in os.listdir(full_path):
            item_path = os.path.join(full_path, item)
            file_info = get_file_info(item_path)
            contents.append({"name": item, **file_info})
        return jsonify(contents)
    else:
        # Return file info if it's a file
        file_info = get_file_info(full_path)
        file_content = read_file(full_path)   
        return jsonify({"name": route_param, **file_info, "content": file_content})

@app.route("/", methods=["POST", "PUT", "DELETE"])
@app.route("/<path:route_param>", methods=["POST", "PUT", "DELETE"])
def handle_other_methods(route_param=""):
    # Validate if POST, PUT, and DELETE requests by returning an error response.

    return jsonify({"error": "Not Authorized to such HTTP method. Please use GET HTTP method requests instead."}), 405

if __name__ == "__main__":
    app.run(debug=True)
