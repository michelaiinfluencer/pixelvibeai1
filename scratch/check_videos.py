import re
import subprocess
import os

def get_git_files():
    res = subprocess.run(['git', 'ls-files'], capture_output=True, text=True)
    return set(res.stdout.splitlines())

def check_html_videos(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    
    videos = re.findall(r'<video[^>]+src=["\']([^"\']+)["\']', content)
    git_files = get_git_files()
    
    print(f"Checking {file_path}...")
    for video in videos:
        # Check if file exists in git with exact case
        if video in git_files:
            # print(f"[OK] {video}")
            pass
        else:
            # Check if it exists with different case
            matches = [f for f in git_files if f.lower() == video.lower()]
            if matches:
                print(f"[CASE MISMATCH] HTML: {video} | Git: {matches[0]}")
            else:
                print(f"[MISSING] {video}")

check_html_videos('portfolio.html')
