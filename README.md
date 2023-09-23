# HarmonyVerse: The Song-Inspired Twitter Bot 🎵🤖

**HarmonyVerse** is a Twitter bot creating personalized, daily song-inspired tweets for its followers, blending Python, ChatGPT (OpenAI GPT-3 model), the Twitter API (Tweepy), and the Genius API to bring a unique twist to daily content generation. This bot can also serve as a great starting template for any AI inspired content! 

## Table of Contents
- [Overview](#overview)
- [Dependencies](#dependencies)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview

With its API integrations, HarmonyVerse ensures a continuous flow of captivating content. Although this template uses OpenAI for poemn creation,
the creator class could be transformed to do many content-related tasks, such as
select the most unique lyrics in a song (act as a lyric bot) or even provide educational content regarding favorite songs. The possiblities are endless. Share the joy of HarmonyVerse with your followers and music enthusiasts!

## Dependencies

To run HarmonyVerse, you'll need the following dependencies:

- [OpenAI Python](https://github.com/openai/openai-python)
- [Tweepy](https://github.com/tweepy/tweepy)
- [LyricsGenius](https://github.com/johnwmillr/LyricsGenius)

**API Keys**: HarmonyVerse relies on APIs from Twitter, Genius, and ChatGPT. To use the bot, you must obtain API keys from these services and add them to the `key_secrets.py` file.

## Setup Instructions

Follow these steps to set up and run HarmonyVerse:

1. **Clone the Repository:**

```bash
git clone https://github.com/your-username/harmonyverse.git
cd harmonyverse
```

2. **Install Dependencies:**

```bash
pip install -r requirements.txt
```

3. **Configure API Keys:**

- Open the `key_secrets.py` file in the project directory.
- Add your API keys for Twitter, Genius, and ChatGPT to this file.

```python
# key_secrets.py

# Twitter API Keys
TWITTER_CONSUMER_KEY = 'your_twitter_consumer_key'
TWITTER_CONSUMER_SECRET = 'your_twitter_consumer_secret'
TWITTER_ACCESS_TOKEN = 'your_twitter_access_token'
TWITTER_ACCESS_TOKEN_SECRET = 'your_twitter_access_token_secret'

# Genius API Key
GENIUS_API_KEY = 'your_genius_api_key'

# ChatGPT API Key
GPT_API_KEY = 'your_chatgpt_api_key'
```

**Note:** Keep the `key_secrets.py` file private and never expose it in your repository.

4. **Running the Bot:**

Execute the bot script to start generating tweets:

```bash
python main.py
```

HarmonyVerse will fetch song-inspired lyrics using the Genius API and create tweets using ChatGPT. The bot will then post these tweets to your Twitter account using the Twitter API.

## Usage

Once HarmonyVerse is up and running, it will generate and post song-inspired tweets to your Twitter account. Feel free to modify the content creation as you see fit, 
or use this repository to get started on your own AI bot! 

## Contributing

We welcome contributions to HarmonyVerse! If you have ideas for improvements, bug fixes, or new features, please message us. 

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.