# OpenAI-Python Examples

This repository contains various Python scripts and examples using the OpenAI library. Each script demonstrates different ways to interact with OpenAI's API, including chatbots, text generation, image creation, sentiment analysis, AI-powered code review, and email writing.
 
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
  pip install python-dotenv pillow requests pathlib
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

## 5 - AI Code Reviewer

An intelligent code review tool that leverages OpenAI's advanced language models to analyze code quality, identify bugs, suggest improvements, and enforce best practices across multiple programming languages.

### Features
- **Multi-Language Support**: Supports Python, JavaScript, Java, C++, C#, PHP, Ruby, Go, Rust, and TypeScript
- **Comprehensive Analysis**: 
  - Code quality issues and potential bugs
  - Best practices adherence
  - Performance bottlenecks identification
  - Security vulnerability detection
  - Code readability and maintainability suggestions
  - Overall code rating (1-10 scale)
- **Flexible Input Methods**:
  - Single file analysis
  - Multiple file batch processing
  - Direct code snippet review
- **Professional Reporting**: Generates detailed markdown reports for team reviews
- **Interactive CLI**: User-friendly command-line interface
- **Line-specific Feedback**: Provides actionable suggestions with line references

### Usage

**Interactive Mode:**
```bash
python ai_code_reviewer.py
```

**Programmatic Usage:**
```python
from ai_code_reviewer import AICodeReviewer

# Initialize the reviewer
reviewer = AICodeReviewer()

# Review a single file
review_result = reviewer.review_file("my_script.py")
print(review_result)

# Review multiple files and generate report
file_paths = ["script1.py", "script2.js", "utils.java"]
results = reviewer.review_multiple_files(file_paths)
report = reviewer.generate_report(results, "team_code_review.md")

# Analyze code snippet directly
code_snippet = '''
def calculate_factorial(n):
    if n == 0:
        return 1
    return n * calculate_factorial(n-1)
'''
analysis = reviewer.analyze_code(code_snippet, "python", "factorial.py")
print(analysis)
```

## 6 - Simple Email Writer

A straightforward tool that helps you write professional emails using OpenAI's language models.

### Features
- **Write New Emails**: Create emails from scratch based on purpose and key points
- **Improve Existing Emails**: Make your emails more professional and clear
- **Multiple Tones**: Choose from professional, friendly, or formal tones
- **Interactive Interface**: Easy-to-use command-line interface

### Usage

**Run the interactive email writer:**
```bash
python simple_email_writer.py
```

**Example workflow:**
```
📧 Simple Email Writer using OpenAI
========================================

What would you like to do?
1. Write a new email
2. Improve an existing email
3. Exit

Enter your choice (1-3): 1

--- Write New Email ---
What is the email for? (e.g., meeting request, follow up): meeting request
Who are you sending to? (e.g., John, my manager): Sarah from marketing
What do you want to say? (main points): discuss new product launch timeline
Tone (professional/friendly/formal) [default: professional]: 

⏳ Writing your email...

✅ Here's your email:
----------------------------------------
Subject: Meeting Request - Product Launch Timeline Discussion

Hi Sarah,

I hope this email finds you well. I would like to schedule a meeting to discuss the new product launch timeline.

Would you be available for a brief meeting this week to go over the details and coordinate our efforts? I'm flexible with timing and can work around your schedule.

Please let me know what works best for you.

Best regards,
[Your Name]
----------------------------------------
```

**Programmatic Usage:**
```python
from simple_email_writer import SimpleEmailWriter

# Initialize the writer
writer = SimpleEmailWriter()

# Write a new email
email = writer.write_email(
    purpose="follow up meeting",
    recipient="John",
    key_points="discuss project status and next steps",
    tone="professional"
)
print(email)

# Improve an existing email
improved = writer.improve_email("hey john, whats up with the project?")
print(improved)
```

## API Usage and Costs

Please note that using the OpenAI API incurs costs based on token usage. Be mindful of:
- The number of requests you make
- The length of input text
- The models you use (GPT-4 is more expensive than GPT-3.5-turbo)
- Image generation costs for DALL-E
- Code review analysis can be token-intensive for large files

### Cost Optimization Tips
- Use GPT-3.5-turbo for basic tasks to reduce costs
- Keep prompts concise and focused
- Cache results for frequently used content
- Monitor your usage through the OpenAI dashboard

## File Structure

```
OpenAI/
├── Chatbot_openai.py              # Interactive chatbot
├── AI_Powered_Text_Summarizer.py  # Text summarization tool
├── dalle_image_generator.py       # DALL-E image generation
├── sentiment_analyzer.py          # Sentiment analysis tool
├── ai_code_reviewer.py           # AI-powered code reviewer
├── simple_email_writer.py        # Simple email writing tool
├── requirements.txt              # Python dependencies
├── .env.example                  # Environment variables template
├── README.md                     # This file
└── examples/                     # Usage examples
    ├── sample_code/              # Sample code for testing reviewer
    ├── test_data/                # Test data for various tools
    └── reports/                  # Generated reports
```

## Contributing

We welcome contributions! Please feel free to submit pull requests or open issues for:
- Bug fixes
- New features
- Additional programming language support for code reviewer
- Performance improvements
- Documentation updates

### Guidelines
1. Follow PEP 8 style guidelines for Python code
2. Add docstrings to all functions and classes
3. Write unit tests for new features
4. Update README.md with new functionality

## Troubleshooting

### Common Issues

**API Key Issues:**
```bash
# Verify your API key is set correctly
echo $OPENAI_API_KEY

# Or check if .env file exists and is properly formatted
cat .env
```

**Rate Limiting:**
- Implement retry logic with exponential backoff
- Consider using multiple API keys for high-volume usage
- Monitor your API usage through OpenAI dashboard

**Large File Processing:**
- Break large files into smaller chunks
- Use streaming for real-time analysis
- Consider preprocessing to remove comments/whitespace

## License

MIT License

## Acknowledgements

- [OpenAI](https://openai.com/) for providing the APIs
- All contributors to this project
- The open-source community for inspiration and best practices

## Support

If you encounter any issues or have questions:
1. Check the troubleshooting section above
2. Open an issue on GitHub
3. Review the OpenAI API documentation
4. Check your API usage and billing status

---

*Last updated: July 2025*
*Version: 2.1.0*
