import os
import shutil
import glob

def sort_files():
    print("\n📁 File Sorting Tool 📁\nSort a directory and the subdirectories by filetypes, and copy all to one bulk directory bucket.\nThis will be what you run the LDA tool on.\n")
    # Ask user for input
    source_dir = input("Please enter the directory to sort: ")
    file_types = input("Please enter a comma separated list of file types (e.g., txt,jpg,py): ")
    target_dir = input("Please enter the target directory: ")

    # Convert comma separated string to list
    file_types = [x.strip() for x in file_types.split(',')]

    try:
        # Check if source directory exists
        if not os.path.isdir(source_dir):
            print(f"❌ Source directory {source_dir} does not exist.")
            return

        # Check if target directory exists, if not, create it
        if not os.path.isdir(target_dir):
            os.makedirs(target_dir)
            print(f"✅ Target directory {target_dir} created.")

        # Iterate over each file type
        for file_type in file_types:

            # Use glob to find all files of this type in source directory and subdirectories
            files = glob.glob(source_dir + f'/**/*.{file_type}', recursive=True)

            for file_path in files:
                file_name = os.path.basename(file_path)

                # If the file doesn't already exist in the target directory, copy it
                if not os.path.exists(os.path.join(target_dir, file_name)):
                    shutil.copy(file_path, target_dir)
                    print(f"✅ File {file_name} copied to {target_dir}.")
                    print(f"Source path: {file_path}")
                else:
                    print(f"❌ File {file_name} already exists in {target_dir}, skipping.")

    except Exception as e:
        print(f"❌ An error occurred: {e}")
