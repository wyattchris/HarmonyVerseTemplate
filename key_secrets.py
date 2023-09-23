# Twitter Consumer API keys
CONSUMER_KEY = "your_key_here"
CONSUMER_SECRET = "your_secret_here"

# Twitter Access token & access token secret
ACCESS_TOKEN = "your_token_here"

ACCESS_SECRET = "your_secret_here"

# Bearer token
BEARER_TOKEN = "your_token_here"

# Client id and secret
CLIENT_ID = "your_id_here"
CLIENT_SECRET = "your_secret_here"

# Access token for Genius API
GENIUS_TOKEN = "your_token_here"


# Contains all ids and secrets necessary for API usage
class TwitterSecrets:
    """Class that holds Twitter Secrets"""

    def __init__(self):
        self.CONSUMER_KEY = CONSUMER_KEY
        self.CONSUMER_SECRET = CONSUMER_SECRET
        self.ACCESS_TOKEN = ACCESS_TOKEN
        self.ACCESS_SECRET = ACCESS_SECRET
        self.BEARER_TOKEN = BEARER_TOKEN
        self.CLIENT_ID = CLIENT_ID
        self.CLIENT_SECRET = CLIENT_SECRET
        self.GENIUS_TOKEN = GENIUS_TOKEN

        # Tests if keys are present
        for key, secret in self.__dict__.items():
            assert secret != "", f"Please provide a valid secret for: {key}"


twitter_secrets = TwitterSecrets()
