"""
This module provides a Flask web server for performing sentiment analysis.

The server has two routes:
- /sentimentAnalyzer: Takes text input from the user and returns the sentiment analysis result.
- /: Renders the index page for input submission.

The sentiment analysis is done using the sentiment_analyzer function from the 
SentimentAnalysis package.
"""
from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

# Flask web server for sentiment analysis
app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    """
    Analyze the sentiment of the text passed via request arguments.

    Retrieves the text to analyze from the request,
    calls the sentiment_analyzer function, and returns the result.

    Returns:
        A string message indicating the sentiment label and score, or an error message.
    """
    # Retrieve the text from request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Handle missing input
    if not text_to_analyze:
        return "No input provided! Please submit text for analysis."

    # Call sentiment analysis function and get the response
    response = sentiment_analyzer(text_to_analyze)
    label = response.get('label')
    score = response.get('score')

    # If no label is returned, return an error message
    if label is None:
        return "Error analyzing sentiment. Please try again with valid input."

    try:
        # Extract the sentiment (assumes the label has format like 'positive_something')
        sentiment = label.split('_')[1]
    except IndexError:
        # Use the label directly if splitting doesn't work
        sentiment = label

    # Return sentiment result
    return f"The given text has been identified as {sentiment} with a score of {score}."

@app.route("/")
def render_index_page():
    """
    Renders the index page.

    This function renders the main HTML page where users can submit their text 
    for sentiment analysis.

    Returns:
        HTML content from the 'index.html' template.
    """
    return render_template("index.html")

if __name__ == "__main__":
    # Run the Flask app
    app.run(host="0.0.0.0", port=5000, debug=True)
