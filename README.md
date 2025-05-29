# OpenAI-Python Examples

This repository contains various Python scripts and examples using the OpenAI library. Each script demonstrates different ways to interact with OpenAI's API, including chatbots, text generation, image creation, and sentiment analysis.

## Getting Started 

To use the scripts in this repository, ensure you have the following prerequisites:

### Prerequisites
- **Python 3.x**
- **OpenAI Python Library**: Install via pip:
  ```bash
  pip install openai
  ```
- **Additional libraries** (depending on the script):
  ```bash
  pip install python-dotenv pillow requests
  ```
- **OpenAI API Key**: You'll need to set up an account on [OpenAI](https://openai.com/) and obtain an API key

## Environment Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/OpenAI.git
   cd OpenAI
   ```

2. Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 1 - OpenAI Chatbot

A simple chatbot built using the OpenAI library. The chatbot utilizes the GPT models to interact with users in a conversational manner.

### Features
- **Interactive Chat**: Users can input prompts, and the chatbot responds intelligently
- **Continuous Conversation**: The chatbot maintains context throughout a session until the user decides to exit

### Usage
```bash
python Chatbot_openai.py
```

Example interaction:
```
You: Hello, how are you?
Bot: I'm doing well, thank you for asking! How can I assist you today?

You: Can you explain quantum computing in simple terms?
Bot: [Response explaining quantum computing]

You: exit
```

## 2 - Text Summarizer

A script that leverages OpenAI's models to create concise summaries of longer text inputs.

### Features
- **Text Summarization**: Condenses lengthy text into shorter, coherent summaries
- **Adjustable Parameters**: Customize the length and style of summaries

### Usage
```python
from AI_Powered_Text_Summarizer import summarize_text

text = "Your long text here..."
summary = summarize_text(text)
print("Summary:", summary)
```

Example:
```python
text = "OpenAI is an artificial intelligence research laboratory consisting of the for-profit OpenAI LP and its parent company, the non-profit OpenAI Inc. OpenAI was founded in December 2015 by Elon Musk, Sam Altman, Greg Brockman, Ilya Sutskever, John Schulman, and Wojciech Zaremba. OpenAI's mission is to ensure that artificial general intelligence (AGI) benefits all of humanity."
summary = summarize_text(text)
print("Summary:", summary)
```

## 3 - DALL-E Image Generator

A Python wrapper for OpenAI's DALL-E API that allows you to generate, edit, and create variations of images using natural language prompts.

### Features
- **Generate Images**: Create images from text descriptions
- **Edit Images**: Modify existing images with masks and prompts
- **Create Variations**: Generate multiple versions of existing images
- **Download Images**: Save generated images locally

### Usage

```python
from dalle_image_generator import DALLEImageGenerator

# Initialize with API key (if not set in environment or .env)
generator = DALLEImageGenerator()

# Generate an image
prompt = "A futuristic city with flying cars and tall glass buildings at sunset"
image_urls = generator.generate_image(prompt)

# Download the generated image
if image_urls:
    generator.download_image(image_urls[0], "futuristic_city.png")
```

Run the example script:
```bash
python dalle_image_generator.py
```

## 4 - Sentiment Analyzer

A tool that leverages OpenAI's language models to perform advanced sentiment analysis and topic extraction from text.

### Features
- **Sentiment Analysis**: Determine positive, negative, neutral, or mixed sentiment
- **Emotion Detection**: Identify primary emotions in text
- **Confidence Scoring**: Get confidence levels for analysis results
- **Key Phrase Extraction**: Identify phrases that influence sentiment
- **Topic Analysis**: Extract main topics and themes from text
- **Batch Processing**: Analyze multiple texts simultaneously
- **File Support**: Process text from files

### Usage

Command-line interface:
```bash
# Analyze sentiment of text
python openai_sentiment_analyzer.py --text "I absolutely loved the movie! The plot was fantastic and the acting was superb."

# Analyze a file
python openai_sentiment_analyzer.py --file reviews.txt --output results.json

# Extract topics instead of sentiment
python openai_sentiment_analyzer.py --text "Climate change is affecting ecosystems worldwide." --type topics
```

Python API:
```python
from openai_sentiment_analyzer import OpenAISentimentAnalyzer

# Initialize the analyzer
analyzer = OpenAISentimentAnalyzer()

# Analyze sentiment
text = "The customer service was terrible. I waited for hours and no one responded to my request."
sentiment_result = analyzer.analyze_sentiment(text)
print(sentiment_result)
```

## API Usage and Costs

Please note that using the OpenAI API incurs costs based on token usage. Be mindful of:
- The number of requests you make
- The length of input text
- The models you use (GPT-4 is more expensive than GPT-3.5-turbo)
- Image generation costs for DALL-E

## License

MIT License

## Acknowledgements

- [OpenAI](https://openai.com/) for providing the APIs
- All contributors to this project
