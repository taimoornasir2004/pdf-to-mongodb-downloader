import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import urllib.request
from datetime import datetime
import os
import threading
import PyPDF2
from pymongo import MongoClient

# --- MongoDB Setup ---
client = MongoClient("mongodb://localhost:27017/")
db = client["proj"]
collection = db["proj"]

def download_and_store_pdfs():
    url = url_entry.get()
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        pdf_links = []

        for link in soup.find_all('a', href=True):
            href = link['href']
            if href.endswith('.pdf'):
                full_url = href if href.startswith('http') else requests.compat.urljoin(url, href)
                pdf_links.append(full_url)

        if not pdf_links:
            messagebox.showinfo("No PDFs", "No PDF found on this page.")
            return

        if not os.path.exists("downloads"):
            os.makedirs("downloads")

        for pdf_url in pdf_links:
            pdf_name = pdf_url.split("/")[-1]
            pdf_path = os.path.join("downloads", pdf_name)
            urllib.request.urlretrieve(pdf_url, pdf_path)

            try:
                with open(pdf_path, "rb") as f:
                    reader = PyPDF2.PdfReader(f)
                    text = ""
                    for page in reader.pages:
                        text += page.extract_text() or ""
            except Exception as e:
                text = f"[Error reading PDF content: {e}]"

            document = {
                "name": pdf_name,
                "url": pdf_url,
                "download_time": str(datetime.now()),
                "content": text.strip()
            }
            collection.insert_one(document)

        messagebox.showinfo("Success", f"{len(pdf_links)} PDF(s) downloaded and stored in MongoDB.")

    except Exception as e:
        messagebox.showerror("Error", str(e))

def start_thread():
    threading.Thread(target=download_and_store_pdfs).start()

# --- GUI Setup ---
root = tk.Tk()
root.title("📥 PDF to MongoDB Downloader")
root.geometry("500x250")
root.configure(bg="#f0f0f0")

title_label = tk.Label(root, text="PDF to MongoDB Downloader", font=("Helvetica", 16, "bold"), bg="#f0f0f0", fg="#333")
title_label.pack(pady=15)

url_label = tk.Label(root, text="Enter Website URL:", font=("Helvetica", 11), bg="#f0f0f0")
url_label.pack()

url_entry = tk.Entry(root, width=60, font=("Helvetica", 10))
url_entry.pack(pady=8)

download_button = tk.Button(root, text="🔍 Check & Download PDFs", font=("Helvetica", 11, "bold"), bg="#4CAF50", fg="white", padx=10, pady=5, command=start_thread)
download_button.pack(pady=15)

root.mainloop()
