
# Real-Time Sentiment Analysis on Social Media


[![Python](https://img.shields.io/badge/Python-3.8-blue.svg)]()

[![Flask](https://img.shields.io/badge/Flask-2.x-green.svg)]()

[![Twitter API](https://img.shields.io/badge/Twitter_Api-v2-white.svg)]()

This project is a Real-Time Sentiment Analysis system that analyzes tweets from Twitter (now X) to determine the sentiment (positive, negative, or neutral) of the text. It uses the Twitter API v2 to fetch recent tweets and TextBlob for sentiment analysis. The system is built with Flask for the backend and a simple HTML/CSS frontend.



## Table of Contents

- [Features]()
- [Installation]()
- [Usage]()
- [Project Structure]()
- [Limitations]()
- [Contributing]()
- [Acknowledgements]()

## Features
- Real-Time Tweet Fetching: Fetches recent tweets using the Twitter API v2.
- Sentiment Analysis: Analyzes tweet sentiment using TextBlob.
- Simple Web Interface: Displays results in a clean and user-friendly format.
- Customizable: Easily extendable for advanced use cases.


## Installation

Prerequisites

- Python 3.8 or higher
- Twitter Developer Account (for API access)

Steps

  - Clone the repository:
    ```bash
    git clone https://github.com/your-username/ real-time-sentiment-analysis.git

    cd real-time-sentiment-analysis
    ```
- Install the required dependencies:
    ```bash
    pip install flask tweepy textblob nltk
    ```
- Download NLTK data:

    ```bash
    python -c "import nltk; nltk.download('punkt'); nltk.download   ('averaged_perceptron_tagger')"
    ```

- Get your Twitter API Bearer Token:

    - Go to the [Twitter Developer Portal.](https://developer.x.com/en)
    - Navigate to your project → Keys & Tokens.
    - Generate a Bearer Token (if not already available).

- Replace the placeholder in app.py with your Bearer Token:

    ```bash
    BEARER_TOKEN = "your_bearer_token"  # Replace with your Bearer  Token
    ```


Usage
-
- Run the Flask app:

    ```bash
    python app.py
  ```

- Open your browser and go to [IP ADDRESS]().
- Enter a keyword (e.g., #Python) and click Analyze.
- The app will fetch 10 recent tweets related to the keyword and display their sentiment (Positive, Neutral, or Negative).

Project Structure
-
        
    real-time-sentiment-analysis/
    ├── app.py                  # Flask backend and sentiment analysis logic
    ├── templates/
    │   └── index.html          # Frontend HTML template
    ├── static/
    │   └── style.css           # CSS for styling the frontend
    ├── requirements.txt        # Python dependencies
    └── README.md               # Project documentation
    


\
Limitations
-

- Free Tier Restrictions:

    - Limited to fetching 10 tweets per request.
    - Only recent tweets (last 7 days) are available.
    -  Rate limits apply (e.g., 450 requests per 15 minutes).

- Sentiment Analysis:
    - TextBlob provides basic sentiment analysis. For more accurate results, consider using advanced models like BERT or VADER.
\
Contributing
-
Contributions are welcome! If you'd like to contribute, please follow these steps:

- Fork the repository.

- Create a new branch `(git checkout -b feature/YourFeatureName)`.

- Commit your changes `(git commit -m 'Add some feature')`.

- Push to the branch `(git push origin feature/YourFeatureName)`.

- Open a pull request.

\
Acknowledgements
-
- Twitter API: For providing access to tweet data.
- TextBlob: For sentiment analysis.
- Flask: For the backend framework.
- NLTK: For natural language processing tools.
