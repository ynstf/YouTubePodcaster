import os

def delete_files(file_list):
    """
    Deletes a list of files.

    Args:
        file_list (list): A list of file paths to delete.
    """
    for file_path in file_list:
        try:
            # Check if the file exists
            if os.path.exists(file_path):
                # Delete the file
                os.unlink(file_path)
                print(f"Deleted file: {file_path}")
            else:
                print(f"File does not exist: {file_path}")
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")