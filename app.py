from flask import Flask, render_template, request
import tweepy
from textblob import TextBlob

# Flask app
app = Flask(__name__)

# Twitter API v2 credentials (replace with your own)
BEARER_TOKEN = "-----"  # Replace with your Bearer Token

# Authenticate with Twitter v2 API
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Function to analyze sentiment
def analyze_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity == 0:
        return "Neutral"
    else:
        return "Negative"

# Function to fetch tweets using v2 API
def fetch_tweets(keyword):
    try:
        tweets = client.search_recent_tweets(query=keyword, max_results=10)
        return [tweet.text for tweet in tweets.data]
    except Exception as e:
        print(f"Error fetching tweets: {e}")
        return []

# Home route
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        keyword = request.form["keyword"]
        tweets = fetch_tweets(keyword)  # Fetch 10 recent tweets
        results = []
        for tweet in tweets:
            sentiment = analyze_sentiment(tweet)
            results.append({"text": tweet, "sentiment": sentiment})
        return render_template("index.html", results=results, keyword=keyword)
    return render_template("index.html")

# Run the app
if __name__ == "__main__":
    app.run(debug=True)