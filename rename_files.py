import os
import re

folder_path = os.path.dirname(os.path.abspath(__file__))

for filename in os.listdir(folder_path):
    match = re.match(r"(\d+)\.(.*)", filename)
    if match:
        number = int(match.group(1))
        rest = match.group(2).strip()

        # 4-digit zero padding
        new_filename = f"{number:04d}. {rest}"

        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_filename)

        if old_path != new_path:
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} → {new_filename}")

print("✅ Done! All numbers now 4-digit zero padded.")
