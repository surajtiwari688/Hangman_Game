import os
import time
import fnmatch



directory = "Downloads"

file_pattern = "MEX PEARL ProductServices*"

current_time = time.time()

for filename in os.listdir(directory):
    if fnmatch.fnmatch(filename, file_pattern):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_mtime = os.path.getmtime(file_path)
            if current_time - file_mtime > 30 * 24 * 60 * 60:
                os.remove(file_path)
                print(f"Deleted: {file_path}")