#!/usr/bin/env python3
"""
CleanDrop: Instant directory organizer and file triage assistant.
Zero-dependency, cross-platform.
"""

import os
import shutil

CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".webp", ".raw", ".arw", ".cr2", ".gif"],
    "Videos": [".mp4", ".mov", ".mkv", ".flv", ".avi"],
    "Audio": [".mp3", ".wav", ".flac", ".aac", ".m4a"],
    "Documents": [".pdf", ".docx", ".doc", ".xlsx", ".csv", ".pptx", ".txt", ".md"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "3D_Models": [".stl", ".obj", ".step", ".scad"],
}

def organize_directory(target_path="."):
    target_path = os.path.abspath(target_path)
    print(f"[+] Organizing directory: {target_path}")

    files = [f for f in os.listdir(target_path) if os.path.isfile(os.path.join(target_path, f))]

    for f in files:
        if f.startswith(".") or f == "cleandrop.py":
            continue

        ext = os.path.splitext(f)[1].lower()
        destination_folder = "Others"

        for category, extensions in CATEGORIES.items():
            if ext in extensions:
                destination_folder = category
                break

        dest_dir = os.path.join(target_path, destination_folder)
        os.makedirs(dest_dir, exist_ok=True)
        shutil.move(os.path.join(target_path, f), os.path.join(dest_dir, f))
        print(f"  Moved: {f} -> {destination_folder}/")

    print("[✓] Directory sorted cleanly.")

if __name__ == "__main__":
    path = input("Enter directory to clean (Press Enter for current directory): ").strip()
    organize_directory(path if path else ".") 
