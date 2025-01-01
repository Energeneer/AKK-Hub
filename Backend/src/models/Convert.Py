import os
from pathlib import Path

# Get all .py files in this folder

path = Path.cwd()

files = [file.name for file in path.glob("*.go")]

for idx, file in enumerate(files):
    with open(file, "r") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            if lines[i].find("gorm.Model") != -1:
                lines[i] = "	gorm.Model         // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields\n"
        
    with open(file, "w") as f:
        f.writelines(lines)

print("Done")
