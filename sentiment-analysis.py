import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('stopwords')

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Load your data
# Make sure to replace 'your_data.csv' with the path to your data file
data = pd.read_csv('your_data.csv')

# Assuming 'review_text' is the column containing the text to analyze
# Replace 'review_text' with the actual name of your text column
def preprocess_text(text):
    # Tokenize the text
    tokens = word_tokenize(text)
    # Convert to lower case
    tokens = [word.lower() for word in tokens]
    # Remove punctuation and non-alphabetic characters
    words = [word for word in tokens if word.isalpha()]
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if not w in stop_words]
    return " ".join(words)

# Preprocess the text data
data['processed_text'] = data['review_text'].apply(preprocess_text)

# Apply sentiment analysis
data['sentiment'] = data['processed_text'].apply(lambda x: sia.polarity_scores(x))

# Extract compound score as a measure of sentiment
data['compound'] = data['sentiment'].apply(lambda x: x['compound'])

# Determine positive, neutral, or negative based on the compound score
data['sentiment_type'] = data['compound'].apply(lambda x: 'positive' if x > 0 else ('neutral' if x == 0 else 'negative'))

# Print or save the results
print(data[['review_text', 'sentiment_type', 'compound']].head())

# Optional: Save to a new CSV file
# data.to_csv('sentiment_analysis_results.csv', index=False)
()