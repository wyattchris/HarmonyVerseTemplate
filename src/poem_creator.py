from openai import OpenAI

# Open API key

class PoemCreator:
    def __init__(self):
        self.client = OpenAI(api_key = "your_key_here")

    # To use OpenAI ChatGPT to generate valid haiku from processed lyrics
    def generate_haiku(self, your_lyrics):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo-16k",
            messages=[
                {"role": "system", "content": "You are a kind and sweet poet " \
                                            "who wants to make others laugh." \
                                            "Capture the meaning of the lyrics given to you by the user," \
                                            "and include words within the lyrics when you" \
                 "compose the poem. Do not exceed 10 lines of writing and do not use offensive slurs."},
                {"role": "user", "content": your_lyrics}
            ],
            n=1,
            max_tokens=256,
            temperature=0.8,
            frequency_penalty = 0.4,
            presence_penalty = 0.2
        )
        haiku = response.choices[0].message['content'].strip()
        return haiku
