import os
import subprocess

def get_files_in_directory(directory):
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return []

    files = os.listdir(directory)
    files = [f for f in files if os.path.isfile(os.path.join(directory, f))]

    return files

if __name__ == "__main__":
    directory = input("Enter the directory path: ")

    file_list = get_files_in_directory(directory)
    os.chdir(directory)
    print("Files in the directory:")
    for file_name in file_list:
        # Split the file name into base name and extension
        base_name, extension = os.path.splitext(file_name)
        output_file = base_name + ".flac"
        
        # Construct the ffmpeg command as a list of strings
        command = ["ffmpeg", "-i", file_name, output_file]

        # Execute the command using subprocess.run
        subprocess.run(command, shell=True, capture_output=False)

        print(file_name)

    for file_name in file_list:
        if file_name.endswith('.webm'):
            os.remove(file_name)
