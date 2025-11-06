<div align="center">

# ✨ Textify

### A powerful yet simple text processing toolkit built with Django

[![Live Demo](https://img.shields.io/badge/demo-live-success?style=for-the-badge)](https://37rohan.pythonanywhere.com/)
[![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-Framework-green?style=for-the-badge&logo=django)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

[Live Demo](https://37rohan.pythonanywhere.com/)

</div>

---

## 📋 Table of Contents

- [About The Project](#about-the-project)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)

---

## 🎯 About The Project

**Textify** is a Django-based web application designed to simplify text processing tasks. Whether you're a writer, developer, or content creator, Textify provides essential utilities to clean, format, and analyze your text efficiently.

### Why Textify?

- **Fast & Efficient** — Process text instantly without complex software
- **User-Friendly** — Clean interface with minimal learning curve
- **Mobile Responsive** — Works seamlessly on all devices
- **No Installation Required** — Access via web browser
- **Privacy Focused** — Text processing happens in real-time, nothing is stored

---

## ✨ Features

<table>
<tr>
<td>

### 🧹 Text Cleaning
- Remove unnecessary punctuation
- Strip extra whitespace
- Eliminate new lines for cleaner formatting

</td>
<td>

### 🔄 Text Transformation
- Convert to UPPERCASE instantly
- Normalize text spacing
- Prepare text for various use cases

</td>
</tr>
<tr>
<td>

### 📊 Text Analysis
- Character counter
- Real-time text statistics
- Clean, readable output

</td>
<td>

### 🎨 User Experience
- Intuitive interface
- Instant results
- Mobile-friendly design

</td>
</tr>
</table>

---

## 🛠️ Tech Stack

**Backend:**
- ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) Python 3.11
- ![Django](https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white) Django Framework

**Frontend:**
- ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white) HTML5
- ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white) CSS3
- ![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=flat&logo=bootstrap&logoColor=white) Bootstrap

**Hosting:**
- ![PythonAnywhere](https://img.shields.io/badge/PythonAnywhere-1D9FD7?style=flat&logo=python&logoColor=white) PythonAnywhere

---

## 🚀 Getting Started

Follow these steps to set up Textify locally on your machine.

### Prerequisites

- Python 3.11 installed on your system
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/RohanGoyal37/Textify.git
   cd Textify
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations** (if applicable)
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

6. **Open your browser** and navigate to:
   ```
   http://127.0.0.1:8000/
   ```

---

## 💡 Usage

1. **Enter your text** in the input area
2. **Select operations** you want to perform (remove punctuation, uppercase, etc.)
3. **Click "Analyze Text"** to process
4. **View results** instantly with character count and formatted output

### Example Use Cases

- Clean up copied text from PDFs
- Format text for social media posts
- Remove formatting before pasting into documents
- Quick character counting for content writing
- Prepare text for data processing

---

## 📁 Project Structure

```
Textify/
│
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
├── LICENSE                   # MIT License file
│
├── textify/               # Project configuration
│   ├── __init__.py
│   ├── settings.py          # Django settings
│   ├── urls.py              # URL routing
│   ├── wsgi.py              # WSGI configuration
│   └── asgi.py              # ASGI configuration
│
└── app/                     # Main application
    ├── __init__.py
    ├── views.py             # Application logic
    ├── urls.py              # App-specific URLs
    ├── templates/           # HTML templates
    │   └── index.html
    └── static/              # CSS, JS, images
        ├── css/
        └── js/
```

---

## 📜 License

Distributed under the **MIT License**. See `LICENSE` file for more information.

The MIT License is a permissive license that allows:
- ✅ Commercial use
- ✅ Modification
- ✅ Distribution
- ✅ Private use

---

## 📧 Contact

**Rohan Goyal**

- GitHub: [@RohanGoyal37](https://github.com/RohanGoyal37)
- Project Link: [https://github.com/RohanGoyal37/Textify](https://github.com/RohanGoyal37/Textify)
- Live Demo: [https://37rohan.pythonanywhere.com/](https://37rohan.pythonanywhere.com/)

---

## 🙏 Acknowledgments

- [Django Documentation](https://docs.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [PythonAnywhere](https://www.pythonanywhere.com/)
- [Shields.io](https://shields.io/) for badges

---

<div align="center">

### ⭐ Star this repository if you find it helpful!

**Made with ❤️ by [Rohan Goyal](https://github.com/RohanGoyal37)**

</div>
