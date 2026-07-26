# PDF to MongoDB Downloader

A Python desktop tool with a Tkinter GUI that scrapes a webpage for PDF links, downloads them, extracts their text content, and stores everything in a MongoDB database.

## 🎮 Features

- **Simple GUI** — enter any website URL and scan it for PDF files
- **Automatic PDF Detection** — scrapes all `<a>` tags on the page and identifies links ending in `.pdf`
- **Bulk Download** — downloads all found PDFs into a local `downloads` folder
- **Text Extraction** — extracts readable text content from each PDF using PyPDF2
- **MongoDB Storage** — stores PDF metadata (name, source URL, download timestamp) and extracted text as documents in MongoDB
- **Threaded Execution** — download and processing runs in a background thread to keep the GUI responsive

## 🛠️ Tech Stack

- **Language:** Python
- **GUI:** Tkinter
- **Web Scraping:** Requests, BeautifulSoup4
- **PDF Processing:** PyPDF2
- **Database:** MongoDB (via PyMongo)

## ⚙️ How to Run

1. Clone the repository
2. Install dependencies:
```bash
   pip install requests beautifulsoup4 PyPDF2 pymongo
```
3. Make sure MongoDB is running locally (`mongodb://localhost:27017/`)
4. Run the script:
```bash
   python proj.py
```
5. Enter a website URL and click "Check & Download PDFs"

## 🎓 About

Developed as a Python project for Advanced DBMS coursework to practice web scraping, PDF text extraction, and NoSQL database integration, University of Engineering and Technology (UET), Lahore — Faisalabad Campus.
