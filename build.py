import PyInstaller.__main__
import os
import sys

def build_app():
    print("--- APP BUILDING ---")
    script_name = 'main.py'
    app_name = 'YoullNeverCatchMe'

    if not os.path.exists(script_name):
        print(f"Error: {script_name} not found!")
        sys.exit(1)

    print(f"Building {app_name}...")

    try:
        PyInstaller.__main__.run([
            script_name,
            '--onefile',
            '--windowed',
            f'--name={app_name}',
            '--clean',
            '--noconfirm' # Automatically overwrites previous builds
        ])
        print(f"\nSuccess! Executable created in the /dist folder.")
    except Exception as e:
        print(f"\nAn error occurred during the build: {e}")

if __name__ == "__main__":
    build_app()