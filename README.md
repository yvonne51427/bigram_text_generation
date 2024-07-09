# Text Processing and Bigram Model

This project consists of three scripts to collect text data, build a bigram model, and generate random text using the bigram model.

## Requirements

- Python 3.x
- `requests`
- `beautifulsoup4`
- `tqdm`

## Setup Instructions

Follow these steps to set up the project and run the scripts:

### 1. Clone the GitHub Repository

```bash
git clone https://github.com/yvonne51427/bigram_text_generation.git 
cd bigram_text_generation
```

### 2. Create a Virtual Environment

Create a virtual environment to manage dependencies.

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

Activate the virtual environment.

- **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- **macOS and Linux**:
  ```bash
  source venv/bin/activate
  ```

### 4. Install Dependencies

Install the required Python packages using `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 5. Run the Scripts

Execute the scripts in the following order:

#### 5.1 Collect Text Data

This script collects text data and stores it in `corpus.txt`.

```bash
python book_content_collector.py
```

#### 5.2 Build Bigram Model

This script reads the collected text data and builds a bigram model, storing it in `bigram_model.pkl`.

```bash
python corpus_bigram_model.py
```

#### 5.3 Generate Random Text

This script uses the bigram model to generate random text and prints it.

```bash
python bigram_text_generator.py
```

## File Descriptions

- `book_content_collector.py`: Collects text data from a website and stores it in `corpus.txt`.
- `corpus_bigram_model.py`: Reads `corpus.txt`, builds a bigram model, and stores it in `bigram_model.pkl`.
- `bigram_text_generator.py`: Reads `bigram_model.pkl` and generates random text based on the bigram model.

## .gitignore

The `.gitignore` file should include the following entries to ignore the virtual environment and other unnecessary files:

```plaintext
# Ignore virtual environment directory
venv/

# Ignore Python compiled files
__pycache__/
*.pyc
*.pyo
*.pyd

# Ignore system files
.DS_Store
Thumbs.db
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
