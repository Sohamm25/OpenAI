

import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class SimpleEmailWriter:
    def __init__(self):
        # Get API key from environment variable
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("Please set your OPENAI_API_KEY in the .env file")
        
        # Initialize OpenAI client
        self.client = OpenAI(api_key=api_key)
    
    def write_email(self, purpose, recipient, key_points, tone="professional"):
        """
        Write an email using OpenAI
        
        Args:
            purpose: What the email is for (e.g., "meeting request", "follow up")
            recipient: Who you're sending to
            key_points: What you want to say
            tone: How formal the email should be
        """
        try:
            # Create the prompt
            prompt = f"""
            Write a {tone} email for the following:
            
            Purpose: {purpose}
            Recipient: {recipient}
            Key points to include: {key_points}
            
            Please write a complete email with subject line and body.
            Keep it clear and concise.
            """
            
            # Get response from OpenAI
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that writes professional emails."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=500,
                temperature=0.7
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"Error writing email: {str(e)}"
    
    def improve_email(self, email_text):
        """
        Improve an existing email
        """
        try:
            prompt = f"""
            Please improve this email to make it more professional and clear:
            
            {email_text}
            
            Provide the improved version.
            """
            
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that improves email writing."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=500,
                temperature=0.5
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"Error improving email: {str(e)}"

def main():
    """Main function to run the email writer"""
    print("📧 Simple Email Writer using OpenAI")
    print("=" * 40)
    
    try:
        # Initialize the email writer
        writer = SimpleEmailWriter()
        
        while True:
            print("\nWhat would you like to do?")
            print("1. Write a new email")
            print("2. Improve an existing email")
            print("3. Exit")
            
            choice = input("\nEnter your choice (1-3): ").strip()
            
            if choice == "1":
                print("\n--- Write New Email ---")
                purpose = input("What is the email for? (e.g., meeting request, follow up): ")
                recipient = input("Who are you sending to? (e.g., John, my manager): ")
                key_points = input("What do you want to say? (main points): ")
                tone = input("Tone (professional/friendly/formal) [default: professional]: ") or "professional"
                
                print("\n⏳ Writing your email...")
                email = writer.write_email(purpose, recipient, key_points, tone)
                
                print("\n✅ Here's your email:")
                print("-" * 40)
                print(email)
                print("-" * 40)
            
            elif choice == "2":
                print("\n--- Improve Email ---")
                email_text = input("Paste your email text here: ")
                
                print("\n⏳ Improving your email...")
                improved = writer.improve_email(email_text)
                
                print("\n✅ Here's the improved version:")
                print("-" * 40)
                print(improved)
                print("-" * 40)
            
            elif choice == "3":
                print("\nGoodbye! 👋")
                break
            
            else:
                print("❌ Invalid choice. Please try again.")
    
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Make sure you have set your OPENAI_API_KEY in the .env file")

if __name__ == "__main__":
    main()
