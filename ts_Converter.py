import tkinter as tk
from tkinter import filedialog
import subprocess

def convert_ts_to_mp4(input_file, output_file):
    try:
        subprocess.run(["ffmpeg", "-i", input_file, output_file])
        print("Conversion successful!")
    except Exception as e:
        print("Conversion failed:", e)

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("TS files", "*.ts")])
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(0, file_path)

def convert():
    input_file = entry.get()
    output_file = "output_file.mp4"  # You can change the output file name here
    convert_ts_to_mp4(input_file, output_file)

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
