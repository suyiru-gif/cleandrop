#!/usr/bin/env python3
"""
MediaKit-Pro: A lightweight, automated CLI utility for batch video/audio processing.
Requires: ffmpeg (install via system package manager)
"""

import os
import subprocess
import sys

def check_ffmpeg():
    try:
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except FileNotFoundError:
        print("[-] FFmpeg not found! Please ensure FFmpeg is installed and added to PATH.")
        sys.exit(1)

def batch_extract_audio(folder="."):
    valid_exts = (".mp4", ".mov", ".mkv", ".avi")
    files = [f for f in os.listdir(folder) if f.lower().endswith(valid_exts)]
    os.makedirs("extracted_audio", exist_ok=True)
    
    print(f"[+] Found {len(files)} video files. Extracting MP3...")
    for idx, f in enumerate(files, 1):
        out_name = os.path.join("extracted_audio", os.path.splitext(f)[0] + ".mp3")
        cmd = ["ffmpeg", "-y", "-i", f, "-vn", "-c:a", "libmp3lame", "-q:a", "2", out_name]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"  [{idx}/{len(files)}] Extracted -> {out_name}")
    print("[✓] Audio extraction completed!")

def batch_compress_video(folder=".", crf=23):
    valid_exts = (".mp4", ".mov", ".mkv")
    files = [f for f in os.listdir(folder) if f.lower().endswith(valid_exts)]
    os.makedirs("compressed_videos", exist_ok=True)

    print(f"[+] Compressing {len(files)} videos with H.264 CRF={crf}...")
    for idx, f in enumerate(files, 1):
        out_name = os.path.join("compressed_videos", "cmp_" + f)
        cmd = ["ffmpeg", "-y", "-i", f, "-c:v", "libx264", "-crf", str(crf), "-c:a", "aac", "-b:a", "128k", out_name]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"  [{idx}/{len(files)}] Done -> {out_name}")
    print("[✓] Compression completed!")

if __name__ == "__main__":
    check_ffmpeg()
    print("=== MediaKit-Pro CLI ===")
    print("1. Batch Extract Audio (.mp3)")
    print("2. Batch Compress Video (H.264)")
    choice = input("Select mode (1 or 2): ").strip()
    if choice == "1":
        batch_extract_audio()
    elif choice == "2":
        batch_compress_video()
    else:
        print("Invalid choice.")
