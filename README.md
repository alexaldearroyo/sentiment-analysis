# Sentiment Analysis Tool

This project is a Python-based sentiment analysis tool that utilizes Natural Language Processing (NLP) techniques to determine the sentiment of textual data. It's designed to process and interpret large datasets, categorizing each text snippet as positive, neutral, or negative based on its sentiment.

## Features

- Text data preprocessing including tokenization, case normalization, punctuation removal, and stopwords elimination.
- Sentiment analysis using NLTK's VADER (Valence Aware Dictionary and sEntiment Reasoner) tool.
- Output categorization into positive, neutral, or negative sentiments.

## Getting Started

### Prerequisites

Ensure you have Python installed on your system. This project is tested with Python 3.8+. You also need `pip` for installing Python packages.

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/sentiment-analysis-tool.git
cd sentiment-analysis-tool
```

2. Install the required Python packages:

```bash
pip install pandas nltk
```

3. Download NLTK data:

```python
import nltk
nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('stopwords')
```

### Usage

1. Prepare your data in a CSV format with a column named `review_text` containing the text to be analyzed.

2. Run the script:

```bash
python sentiment_analysis.py
```

3. The script will print the first few rows of the analyzed data including the sentiment type and compound score. Optionally, you can uncomment the last line in the script to save the results to a new CSV file.