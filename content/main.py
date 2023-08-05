import os

# Folder name to read files from
folder_name = ""

# Output file name
output_file = "combined_file.txt"

# Get the absolute path of the current directory
current_directory = os.getcwd()

# Create the full path to the folder
folder_path = os.path.join(current_directory, folder_name)

# List all files in the folder
files = os.listdir(folder_path)

# Sort the files alphabetically
files.sort()

count = 0
# Open the output file in append mode
with open(output_file, "a") as combined_file:
    # Loop through each file in the folder
    for file_name in files:
        # Create the full path to the file
        file_path = os.path.join(folder_path, file_name)

        # Check if the current item is a file and contains the word "simple"
        if os.path.isfile(file_path) and "simply-cryptocurrency" in file_name.lower():
            count += 1
            # Open the file in read mode
            with open(file_path, "r") as file:
                # Read the content of the file
                content = file.read()

                # Write the content to the output file
                combined_file.write(content)
