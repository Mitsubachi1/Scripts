import os

def append_text_to_files(directory, text_to_append):
    # Get all file names in the directory
    file_names = os.listdir(directory)

    # Filter for text files
    text_files = [file_name for file_name in file_names if file_name.lower().endswith('.txt')]

    # Process each text file
    for text_file in text_files:
        file_path = os.path.join(directory, text_file)

        # Read the contents of the text file
        with open(file_path, 'a') as file:
            # Append the specified text to the file
            file.write(text_to_append)

# Get the current directory
current_directory = os.getcwd()

# Specify the text to append to the files
text_to_append = "Any text you wish to append"

# Append text to all text files in the current directory
append_text_to_files(current_directory, text_to_append)
