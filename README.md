# TweetScraper: Simple Sentiment Analysis Application

**TweetScraper** is a sample project demonstrating basic sentiment analysis using Python and machine learning.

## Features

* Scikit-Learn-based sentiment classification
* Dataset of 19,999 movie reviews

  * First 10,002 reviews: positive
  * Remaining 9,997 reviews: negative
* Turkish stop words list (`trstop`)

## Requirements

* Windows OS
* (Optional, for Python version) Python 3.7 or above
* Python packages:

  * scikit-learn
  * pandas
  * numpy

> **Note:** If you prefer not to install Python packages, you can use the provided executables.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/agahgok/TOPAS.git
   ```
2. Change directory:

   ```bash
   cd TOPAS/TweetScraper
   ```
3. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   venv/Scripts/activate  # Windows PowerShell
   ```
4. Install Python packages:

   ```bash
   pip install scikit-learn pandas numpy
   ```

## Usage

* **Executable without Python dependencies**

  * Run `ListeleSayfasi.exe` in the `TweetScraper` folder.

* **Executable with Python environment**

  * Run `Topas_UI_Tasarım.exe` after installing Python packages.

## Project Structure

```
TweetScraper/
├─ dene111me.csv           # Sample review data
├─ yorumlar.csv            # Full dataset
├─ sentimentAnalysist.py   # Analysis and classification script
├─ turkce-stop-words       # Turkish stop words list
├─ Topas_UI_Tasarım.exe    # GUI-based executable
└─ ListeleSayfasi.exe      # Executable without dependencies
```

## References

* Scikit-Learn for Text Analysis of Amazon Fine Food Reviews
* trstop: Turkish stop words list

---

*This project is intended for educational purposes.*
