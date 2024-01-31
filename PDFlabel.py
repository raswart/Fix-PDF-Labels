import os
import tkinter as tk
from tkinter import filedialog
import fitz  # PyMuPDF

def select_folder():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    folder_path = filedialog.askdirectory()  # Show dialog to select a folder
    return folder_path

def rename_pdf_page_labels(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(folder_path, filename)
            doc = fitz.open(pdf_path)

            # Set the page label to the PDF document name (without extension)
            page_label = os.path.splitext(filename)[0]

            # Define the page label dictionary for all pages
            label_dict = {"startpage": 0, "prefix": page_label, "style": "D", "firstpagenum": 1}

            # Update the page labels in the PDF
            doc.set_page_labels([label_dict])

            # Save the changes, overwriting the original file
            doc.save(pdf_path, incremental=True, encryption=fitz.PDF_ENCRYPT_KEEP)
            doc.close()
            print(f"Updated page labels for {filename}")

def main():
    folder_path = select_folder()
    if folder_path:
        rename_pdf_page_labels(folder_path)
        print("All PDFs have been processed with updated page labels.")
    else:
        print("No folder was selected.")

if __name__ == "__main__":
    main()