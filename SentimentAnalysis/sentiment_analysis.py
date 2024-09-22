import requests
import json

def sentiment_analyzer(text_to_analyze):
    # URL of the sentiment analysis service (check if this is correct)
    url = 'https://api.your-sentiment-service-endpoint.com/v1/analyze'  # Replace with the correct API URL

    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Custom header specifying the model ID for the sentiment analysis service
    headers = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}

    try:
        # Sending a POST request to the sentiment analysis API
        response = requests.post(url, json=myobj, headers=headers)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)

        # Parsing the JSON response from the API
        formatted_response = response.json()

        # Extracting sentiment label and score from the response if available
        if 'documentSentiment' in formatted_response:
            label = formatted_response['documentSentiment'].get('label')
            score = formatted_response['documentSentiment'].get('score')
        else:
            label = None
            score = None

    except requests.exceptions.RequestException as e:
        # Print the exception for debugging purposes
        print(f"An error occurred: {e}")
        label = None
        score = None

    # Returning a dictionary containing sentiment analysis results
    return {'label': label, 'score': score}
