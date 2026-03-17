# 🤖 FAQ Chatbot — AI & Technology Concepts

[![Contributors](https://img.shields.io/github/contributors/khushi-Jag/ApexcifyTechnologys_Chatbot-for-FAQs-)](https://github.com/khushi-Jag/ApexcifyTechnologys_Chatbot-for-FAQs-/graphs/contributors)
[![Forks](https://img.shields.io/github/forks/khushi-Jag/ApexcifyTechnologys_Chatbot-for-FAQs-)](https://github.com/khushi-Jag/ApexcifyTechnologys_Chatbot-for-FAQs-/network/members)
[![Stars](https://img.shields.io/github/stars/khushi-Jag/ApexcifyTechnologys_Chatbot-for-FAQs-)](https://github.com/khushi-Jag/ApexcifyTechnologys_Chatbot-for-FAQs-/stargazers)
[![Issues](https://img.shields.io/github/issues/khushi-Jag/ApexcifyTechnologys_Chatbot-for-FAQs-)](https://github.com/khushi-Jag/ApexcifyTechnologys_Chatbot-for-FAQs-/issues)
[![License](https://img.shields.io/github/license/khushi-Jag/ApexcifyTechnologys_Chatbot-for-FAQs-)](https://github.com/khushi-Jag/ApexcifyTechnologys_Chatbot-for-FAQs-/blob/main/LICENSE)

> A **professional, interactive FAQ Chatbot** built with Flask that answers questions about Artificial Intelligence, Machine Learning, and Web Development using NLP techniques — Cosine Similarity and Keyword Overlap — with a modern Glassmorphism UI.

🌐 **[Explore the docs »](#)**
🚀 **[View Demo](#)** · 🐛 **[Report Bug](#)** · 🌟 **[Request Feature](#)**

---

## 📌 Table of Contents

* [About The Project](#-about-the-project)
* [Key Features](#-key-features)
* [Built With](#-built-with)
* [How It Works](#-how-it-works)
* [Project Structure](#-project-structure)
* [Getting Started](#-getting-started)
* [Usage](#-usage)
* [Contributing](#-contributing)
* [License](#-license)
* [Contact](#-contact)

---

## 💡 About The Project

The **FAQ Chatbot** is a full-stack intelligent question-answering system that provides accurate answers to common questions about AI, Machine Learning, and Web Development. It combines **Cosine Similarity** (65% weight) with **Keyword Overlap** (35% weight) to find the best matching answer from its FAQ database, and categorizes every response with a confidence level — High, Medium, or Low.

---

## ✨ Key Features

* **Intelligent Matching** – Combines Cosine Similarity and Keyword Overlap for accurate answer retrieval.
* **NLP Preprocessing** – Stopword removal, synonym expansion (e.g. `"ML"` → `"Machine Learning"`), and text normalization.
* **Confidence Scoring** – Categorizes every match as High, Medium, or Low confidence.
* **Dynamic Suggestions** – Offers helpful suggestions when no confident match is found.
* **Modern Glassmorphism UI** – Clean, responsive frontend built with HTML5, CSS3, and Vanilla JS.
* **Zero Heavy Dependencies** – Runs on standard Python libraries + Flask only.

---

## 🛠 Built With

| Technology | Purpose |
|---|---|
| Python | Core language |
| Flask | Web framework & backend server |
| HTML5 / CSS3 | Frontend UI |
| JavaScript (ES6+) | Frontend interactivity |
| `math` (Cosine Similarity) | NLP similarity calculation |
| `re` (Regex) | Text cleaning & normalization |

---

## 🧠 How It Works

User input is processed through a 5-stage NLP pipeline:

| Step | Description |
|---|---|
| **1. Normalization** | Converts text to lowercase, removes special characters |
| **2. Synonym Mapping** | Expands acronyms — `"AI"` → `"Artificial Intelligence"`, `"NLP"` → `"Natural Language Processing"` |
| **3. Vectorization** | Converts processed text into a numerical word-frequency vector |
| **4. Similarity Scoring** | Cosine Similarity (65%) + Keyword Overlap (35%) = combined score |
| **5. Confidence Classification** | High / Medium / Low based on final score threshold |

### Scoring Formula

```
Final Score = (Cosine Similarity × 0.65) + (Keyword Overlap × 0.35)
```

```
User Query
    │
    ▼
Normalize + Synonym Expand
    │
    ▼
Vectorize
    │
    ▼
Score against FAQ database
    │
    ▼
Score above threshold? ── Yes ──► Return best match + confidence level
    │
    No
    │
    ▼
Return suggestions
```

---

## 📁 Project Structure

```
ApexcifyTechnologys_Chatbot-for-FAQs-/
│
├── app.py              # Main Flask server + NLP logic
├── static/
│   └── style.css       # Glassmorphism UI styles
├── templates/
│   └── index.html      # Main frontend template
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

* Python 3.8+
* pip

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/khushi-Jag/ApexcifyTechnologys_Chatbot-for-FAQs-.git
cd ApexcifyTechnologys_Chatbot-for-FAQs-
```

**2. Create a virtual environment** *(recommended)*

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

**3. Install dependencies**

```bash
pip install flask
```

---

## 📝 Usage

**1. Run the application**

```bash
python app.py
```

**2. Open in browser**

```
http://127.0.0.1:5000
```

**3. Ask a question**

Type any question related to AI, ML, or Web Development:

```
What is deep learning?
What is the difference between AI and ML?
How does NLP work?
What is a REST API?
```

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a feature branch:

```bash
git checkout -b feature/AmazingFeature
```

3. Commit your changes:

```bash
git commit -m "Add AmazingFeature"
```

4. Push and open a Pull Request:

```bash
git push origin feature/AmazingFeature
```

---

## 📝 License

Distributed under the **MIT License**. See `LICENSE` for details.

---

## 📫 Contact

**Khushi Jagwani**
GitHub: [https://github.com/khushi-Jag](https://github.com/khushi-Jag)

---

## 🙏 Acknowledgments

* [Flask Documentation](https://flask.palletsprojects.com/)
* Open Source Community ❤️
