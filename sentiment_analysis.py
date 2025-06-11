# sentiment_analysis.py
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download required NLTK data
nltk.download('vader_lexicon', quiet=True)

def analyze_sentiment(text):
    """Analyze sentiment of input text and return classification"""
    sia = SentimentIntensityAnalyzer()
    scores = sia.polarity_scores(text)
    
    # Classify based on compound score
    compound_score = scores['compound']
    if compound_score >= 0.05:
        return "positive", compound_score
    elif compound_score <= -0.05:
        return "negative", compound_score
    else:
        return "neutral", compound_score

if __name__ == "__main__":
    # Example text from your document
    sample_text = """
    Sentiment analysis, a key NLP technique, determines whether text is positive, negative, or neutral. 
    It can also detect specific emotions using a predefined lexicon. This method is widely used on social media 
    and review platforms to analyze public opinions.
    
    Popular data sources include:
    - Amazon (product reviews)
    - Facebook, Twitter, Reddit (social opinions)
    - News sites (public sentiment on events)
    
    This analysis helps in understanding audience perception and trends.
    """
    
    # Analyze the sample text
    sentiment, score = analyze_sentiment(sample_text)
    
    # Print results
    print("Sentiment Analysis Results:")
    print("=" * 50)
    print(sample_text)
    print("=" * 50)
    print(f"Sentiment: {sentiment.upper()} (Confidence: {score:.4f})")
    print("=" * 50)
    
    # Additional test cases
    test_texts = [
        "This product is absolutely amazing! Loved the features.",
        "The service was terrible and the staff was rude.",
        "The conference happened in Paris yesterday.",
        "I'm feeling excited about the new opportunities!"
    ]
    
    print("\nTest Cases:")
    for i, text in enumerate(test_texts, 1):
        sentiment, score = analyze_sentiment(text)
        print(f"\nTest {i}:")
        print(f"Text: {text}")
        print(f"Result: {sentiment.upper()} (Score: {score:.4f})")