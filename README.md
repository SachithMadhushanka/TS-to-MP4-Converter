# TS to MP4 Converter

## Overview

The TS to MP4 Converter is a Python-based desktop application that allows users to convert video files from the `.ts` format to the `.mp4` format. The application uses `ffmpeg` for the conversion process and provides a simple graphical user interface (GUI) for selecting the input file and initiating the conversion.

## Features

- Select a `.ts` video file for conversion.
- Convert the selected `.ts` file to an `.mp4` file.
- User-friendly GUI for easy file selection and conversion.

## Requirements

- Python 3.x
- tkinter
- ffmpeg

## Installation

1. **Install `ffmpeg`:**
   - On Windows: Download from [ffmpeg.org](https://ffmpeg.org/download.html) and follow the installation instructions.
   - On macOS: Install via Homebrew:
     ```bash
     brew install ffmpeg
     ```
   - On Linux: Install via package manager, e.g.,
     ```bash
     sudo apt-get install ffmpeg
     ```

2. **Install the required Python packages:**
   ```bash
   pip install tkinter
   ```

## Usage

1. **Run the application:**
   ```bash
   python ts_to_mp4_converter.py
   ```

2. **Use the application:**
   - Click the "Browse" button to select a `.ts` file for conversion.
   - The selected file path will be displayed in the entry field.
   - Click the "Convert" button to start the conversion process.
   - The output `.mp4` file will be saved in the same directory as the script with the name `output_file.mp4`.

## Script Explanation

### Importing Libraries
```python
import tkinter as tk
from tkinter import filedialog
import subprocess
```
- **tkinter**: For creating the graphical user interface.
- **subprocess**: For running the `ffmpeg` command.

### Function to Convert TS to MP4
```python
def convert_ts_to_mp4(input_file, output_file):
    try:
        subprocess.run(["ffmpeg", "-i", input_file, output_file])
        print("Conversion successful!")
    except Exception as e:
        print("Conversion failed:", e)
```
- Runs the `ffmpeg` command to convert the `.ts` file to `.mp4`.

### Function to Select File
```python
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("TS files", "*.ts")])
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(0, file_path)
```
- Opens a file dialog to select a `.ts` file and displays the selected file path in the entry field.

### Function to Start Conversion
```python
def convert():
    input_file = entry.get()
    output_file = "output_file.mp4"  # You can change the output file name here
    convert_ts_to_mp4(input_file, output_file)
```
- Gets the input file path from the entry field and calls the `convert_ts_to_mp4` function to start the conversion.

### Creating the GUI
```python
# Create the main window
root = tk.Tk()
root.title("TS to MP4 Converter")

# Create a frame for the file selection
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Create a label and entry for displaying the selected file path
label = tk.Label(frame, text="Select .ts file:")
label.grid(row=0, column=0, padx=(0, 10))
entry = tk.Entry(frame, width=40)
entry.grid(row=0, column=1, padx=(0, 10))
button = tk.Button(frame, text="Browse", command=select_file)
button.grid(row=0, column=2)

# Create a button to start the conversion
convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.pack(pady=10)

# Run the main event loop
root.mainloop()
```
- Sets up the main window and GUI components for file selection and conversion.

## License

This project is licensed under the MIT License.
