import csv
from tkinter import Tk, filedialog

Tk().withdraw()

file = filedialog.askopenfilename(
    title="Select a CSV file",
    filetypes=[("CSV Files", "*.csv")]
)

if file:
    with open(file, "r", newline="", encoding="utf-8-sig") as f:
        reader = csv.reader(f)

        for i, row in enumerate(reader):
            if i == 3:
                break
            print(row)
else:
    print("No file selected")