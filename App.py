import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk  # For Progressbar
from PyPDF2 import PdfMerger # type: ignore

# ----------------------------------------
# SPLASH SCREEN
# ----------------------------------------
def show_main_app():
    splash.destroy()  # close splash

    # MAIN PDF Merger APP
    root = tk.Tk()
    root.title("MergeMate - PDF Merger")
    root.geometry("400x400")
    root.config(bg="#FED5F9")
    root.resizable(False, False)
    icon = tk.PhotoImage(file="icon.png")  # Make sure 'my_icon.png' exists
    root.iconphoto(True, icon)


    pdf_list = []

    def add_pdfs():
        files = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
        for file in files:
            if file not in pdf_list:
                pdf_list.append(file)
                listbox.insert(tk.END, file.split("/")[-1])

    def merge_pdfs():
        if not pdf_list:
            messagebox.showwarning("No PDFs", "Please add at least two PDF files.")
            return

        merger = PdfMerger()
        for pdf in pdf_list:
            merger.append(pdf)

        save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF File", "*.pdf")])
        if save_path:
            merger.write(save_path)
            merger.close()
            messagebox.showinfo("Success", f"Merged PDF saved at:\n{save_path}")

    tk.Label(root, text="MergeMate", font=("Century Gothic", 30, "bold"), bg="#0E0000", fg="white").pack(pady=10)
    listbox = tk.Listbox(root, width=30, height=5)
    listbox.pack(pady=10)

    tk.Button(root, text="Add PDFs", command=add_pdfs, bg="#0E0000", fg="white").pack(pady=5)
    tk.Button(root, text="Merge & Save", command=merge_pdfs, bg="#0E0000", fg="white").pack(pady=5)

    root.mainloop()
# ----------------------------------------
# CREATE SPLASH
# ----------------------------------------
splash = tk.Tk()
splash.overrideredirect(True)  # Removes title bar
splash.geometry("400x400+500+250")  # Width x Height + x_offset + y_offset
splash.configure(bg="white")

img = tk.PhotoImage(file="icon.png")  # must be .png
tk.Label(splash, image=img, bg="white").pack()


tk.Label(splash, text="MergeMate", font=("Century Gothic", 30, "bold"), bg="#0E0000", fg="white").pack(expand=True)

# Progress Bar
progress = ttk.Progressbar(splash, length=200, mode='indeterminate')
progress.pack(pady=20)
progress.start()

# Close splash after 3 seconds and open main app
splash.after(6000, show_main_app)

splash.mainloop()
