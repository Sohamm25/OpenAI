import os
import openai
import argparse
import json
from dotenv import load_dotenv
load_dotenv()

class OpenAISentimentAnalyzer:
    """
    A class to analyze sentiment and extract insights from text using OpenAI's models.
    """
    
    def __init__(self, api_key=None):
        """
        Initialize the OpenAI client with the API key.
        
        Args:
            api_key (str, optional): OpenAI API key. If not provided, will try to get from environment variable.
        """
        # Use provided API key or try to get from environment
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        
        if not self.api_key:
            raise ValueError("OpenAI API key must be provided or set as OPENAI_API_KEY environment variable")
            
        # Initialize the OpenAI client
        self.client = openai.OpenAI(api_key=self.api_key)
    
    def analyze_sentiment(self, text):
        """
        Analyze the sentiment of the provided text.
        
        Args:
            text (str): The text to analyze
            
        Returns:
            dict: Dictionary containing sentiment analysis results
        """
        prompt = f"""
        Analyze the sentiment of the following text and provide a detailed response in JSON format with these fields:
        - sentiment: (positive, negative, neutral, or mixed)
        - sentiment_score: (number between -1 and 1, where -1 is very negative and 1 is very positive)
        - primary_emotion: (the main emotion expressed)
        - confidence: (low, medium, high)
        - key_phrases: (list of phrases that influenced the sentiment rating)
        
        Text to analyze:
        "{text}"
        
        Provide ONLY the JSON response without any additional text.
        """
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.2,
                response_format={"type": "json_object"}
            )
            
            # Parse the JSON response
            result = json.loads(response.choices[0].message.content.strip())
            return result
            
        except Exception as e:
            print(f"Error analyzing sentiment: {e}")
            return None
    
    def extract_topics(self, text, num_topics=5):
        """
        Extract main topics from the provided text.
        
        Args:
            text (str): The text to analyze
            num_topics (int): Number of topics to extract
            
        Returns:
            list: List of extracted topics
        """
        prompt = f"""
        Extract the {num_topics} most important topics or themes from the following text.
        For each topic, provide:
        - topic_name: short name of the topic
        - relevance_score: number between 0 and 1
        - related_terms: list of terms related to this topic mentioned in the text
        
        Format the response as a JSON array of topic objects.
        
        Text to analyze:
        "{text}"
        
        Provide ONLY the JSON response without any additional text.
        """
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.2,
                response_format={"type": "json_object"}
            )
            
            # Parse the JSON response
            result = json.loads(response.choices[0].message.content.strip())
            return result.get("topics", [])
            
        except Exception as e:
            print(f"Error extracting topics: {e}")
            return None
    
    def analyze_text_batch(self, texts, analysis_type="sentiment"):
        """
        Analyze a batch of texts.
        
        Args:
            texts (list): List of texts to analyze
            analysis_type (str): Type of analysis to perform (sentiment or topics)
            
        Returns:
            list: List of analysis results
        """
        results = []
        
        for i, text in enumerate(texts):
            print(f"Analyzing text {i+1}/{len(texts)}...")
            
            if analysis_type == "sentiment":
                result = self.analyze_sentiment(text)
            elif analysis_type == "topics":
                result = {"topics": self.extract_topics(text)}
            else:
                print(f"Unknown analysis type: {analysis_type}")
                continue
                
            results.append(result)
            
        return results
    
    def analyze_file(self, file_path, analysis_type="sentiment"):
        """
        Analyze text from a file.
        
        Args:
            file_path (str): Path to the file containing text to analyze
            analysis_type (str): Type of analysis to perform
            
        Returns:
            dict: Analysis results
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
                
            if analysis_type == "sentiment":
                return self.analyze_sentiment(text)
            elif analysis_type == "topics":
                return {"topics": self.extract_topics(text)}
            else:
                print(f"Unknown analysis type: {analysis_type}")
                return None
                
        except Exception as e:
            print(f"Error reading or analyzing file: {e}")
            return None


def main():
    """
    Command line interface for the OpenAI Sentiment Analyzer.
    """
    parser = argparse.ArgumentParser(description="Analyze sentiment and extract topics from text using OpenAI")
    
    # Add arguments
    parser.add_argument("--text", type=str, help="Text to analyze")
    parser.add_argument("--file", type=str, help="Path to file containing text to analyze")
    parser.add_argument("--type", type=str, choices=["sentiment", "topics"], default="sentiment",
                        help="Type of analysis to perform")
    parser.add_argument("--output", type=str, help="Path to save analysis results (JSON format)")
    
    args = parser.parse_args()
    
    # Ensure we have either text or file to analyze
    if not args.text and not args.file:
        parser.error("Either --text or --file must be provided")
    
    # Check if API key is available
    if not os.getenv("OPENAI_API_KEY"):
        print("Warning: OPENAI_API_KEY not found in environment variables.")
        print("Please provide your API key when creating an instance.")
        return
    
    # Create analyzer instance
    analyzer = OpenAISentimentAnalyzer()
    
    # Perform analysis
    if args.file:
        print(f"Analyzing file: {args.file}")
        result = analyzer.analyze_file(args.file, args.type)
    else:
        print("Analyzing provided text")
        if args.type == "sentiment":
            result = analyzer.analyze_sentiment(args.text)
        else:
            result = {"topics": analyzer.extract_topics(args.text)}
    
    # Display and save results
    if result:
        # Pretty print the result
        print("\nAnalysis Results:")
        print(json.dumps(result, indent=2))
        
        # Save to file if requested
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                json.dump(result, f, indent=2)
            print(f"\nResults saved to {args.output}")
    else:
        print("Analysis failed or returned no results")


if __name__ == "__main__":
    main()
