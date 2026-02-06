import os
import sys
import subprocess

# GTK3 Runtime path
gtk_path = r"C:\Program Files\GTK3-Runtime Win64\bin"

if os.path.exists(gtk_path):
    # Prepend GTK3 path to PATH environment variable
    os.environ['PATH'] = gtk_path + os.pathsep + os.environ['PATH']
    print(f"Added GTK3 to PATH: {gtk_path}")
else:
    print(f"Warning: GTK3 path not found at {gtk_path}")
    print("PDF generation might fail if GTK3 is not in PATH.")

# Run mkdocs build
print("Starting PDF build...")
try:
    # Use the same python executable to run module
    subprocess.run([sys.executable, "-m", "mkdocs", "build", "-f", "mkdocs_pdf.yml"], check=True, env=os.environ)
    print("Build completed successfully!")
except subprocess.CalledProcessError as e:
    print(f"Build failed with exit code {e.returncode}")
    sys.exit(e.returncode)
except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)
