# 📂 File Organizer Script (Python)

A Python automation tool that organizes files into categorized folders such as Images, Documents, Videos, Music and Archives based on their file extensions.

---

## 🚀 Features

- Automatically detects file extensions  
- Creates category folders if they do not exist  
- Moves files into appropriate folders  
- Handles unmatched files using an "Others" folder  
- Simple and beginner-friendly implementation  

---

## 🛠️ Technologies Used

- Python 3
- os module (for file system navigation)
- shutil module (for file movement operations)

---


## ▶️ How to Run (Using VS Code Terminal)

1. Open the project folder in VS Code  
   - Click **File → Open Folder**  
   - Select the **File Organizer** folder  

2. Open Terminal in VS Code  
   - Click **Terminal → New Terminal**  

3. Run the script:

```
python file_organizer.py
```

OR (if python command doesn't work):

```
py file_organizer.py
```

4. Enter the folder path you want to organize (without quotes).

---

## 📌 Example

Before organizing:
```
Downloads/
│── photo.jpg
│── document.pdf
│── video.mp4
```

After organizing:
```
Downloads/
│── Images/
│    └── photo.jpg
│── Documents/
│    └── document.pdf
│── Videos/
│    └── video.mp4
```
