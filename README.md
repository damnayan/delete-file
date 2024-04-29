# delete-file
This Python script checks if a specified file exists at a given path and deletes it if present, confirming the deletion or warning if the file doesn't exist. Useful for intentional and verified file management.

Key Features:

File Existence Verification: Before attempting deletion, the script checks if the file exists at the specified path.
Secure Deletion: Safely removes the file only after confirming its existence, preventing accidental deletions.
User Feedback: Provides clear messages to inform the user whether the file was successfully deleted or if the specified file was not found.

Technologies Used:

Python 3.
Standard Library: os for file management operations

Usage:

Place the script in a directory of your choice.
Modify the file_path variable in the script to reflect the absolute path of the file you wish to delete.
Run the script using a Python interpreter.
Receive feedback on whether the file was successfully deleted or if it did not exist.
