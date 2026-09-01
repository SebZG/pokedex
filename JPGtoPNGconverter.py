import os
import sys

from PIL import Image

path = sys.argv[1]
directory = sys.argv[2]

if not os.path.exists(path):
    print(f"Error: Source directory '{path}' does not exist.")
    sys.exit(1)

if not os.path.isdir(path):
    print(f"Error: '{path}' is not a directory.")
    sys.exit(1)

if not os.path.exists(directory):
    os.makedirs(directory)

for filename in os.listdir(path):
    clean_name = os.path.splitext(filename)[0]
    try:
        img = Image.open(f"{path}{filename}")
        img.save(f"{directory}{clean_name}.png", "png")
    except Exception as e:
        print(f"Error processing {filename}: {e}")

print("All done!")
