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


## ▶️ How to Run

1. Clone the repository:

```
git clone https://github.com/YOUR_USERNAME/code-with-python.git
```

2. Navigate to the project folder:

```
cd "File Organizer"
```

3. Run the script:

```
python file_organizer.py
```

4. Enter the folder path you want to organize (without quotes).

Example:
```
C:\Users\lenovo\Downloads
```

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
