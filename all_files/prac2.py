from pathlib import Path

file_path = Path("jinx.gft")
if file_path.exists:
    print("yea")
else:
    print("nah")