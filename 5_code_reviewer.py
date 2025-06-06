import openai
import os
import json
from pathlib import Path

class AICodeReviewer:
    def __init__(self, api_key=None):
        """Initialize the AI Code Reviewer"""
        self.client = openai.OpenAI(api_key=api_key or os.getenv('OPENAI_API_KEY'))
        
    def analyze_code(self, code, language="python", filename=""):
        """Analyze code and provide suggestions"""
        
        prompt = f"""
        You are an expert code reviewer. Analyze the following {language} code and provide:
        
        1. **Code Quality Issues**: Identify bugs, logic errors, or potential runtime issues
        2. **Best Practices**: Suggest improvements following {language} best practices
        3. **Performance**: Point out performance bottlenecks or inefficiencies
        4. **Security**: Identify potential security vulnerabilities
        5. **Readability**: Suggest improvements for code clarity and maintainability
        6. **Overall Rating**: Rate the code from 1-10 and provide summary
        
        File: {filename}
        
        Code:
        ```{language}
        {code}
        ```
        
        Please provide specific, actionable feedback with line references where applicable.
        Format your response clearly with headers and bullet points.
        """
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an expert code reviewer with years of experience in software development."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=1500
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"Error analyzing code: {str(e)}"
    
    def review_file(self, file_path):
        """Review a code file"""
        try:
            file_path = Path(file_path)
            
            if not file_path.exists():
                return "File not found!"
            
            # Read the file
            with open(file_path, 'r', encoding='utf-8') as f:
                code = f.read()
            
            # Determine language from file extension
            language_map = {
                '.py': 'python',
                '.js': 'javascript',
                '.java': 'java',
                '.cpp': 'cpp',
                '.c': 'c',
                '.cs': 'csharp',
                '.php': 'php',
                '.rb': 'ruby',
                '.go': 'go',
                '.rs': 'rust',
                '.ts': 'typescript'
            }
            
            language = language_map.get(file_path.suffix.lower(), 'unknown')
            
            if language == 'unknown':
                return f"Unsupported file type: {file_path.suffix}"
            
            # Analyze the code
            return self.analyze_code(code, language, file_path.name)
            
        except Exception as e:
            return f"Error reading file: {str(e)}"
    
    def review_multiple_files(self, file_paths):
        """Review multiple files and generate a summary report"""
        results = {}
        
        for file_path in file_paths:
            print(f"Reviewing: {file_path}")
            results[file_path] = self.review_file(file_path)
        
        return results
    
    def generate_report(self, results, output_file="code_review_report.md"):
        """Generate a markdown report from review results"""
        report = "# Code Review Report\n\n"
        report += f"Generated on: {Path().cwd()}\n\n"
        
        for file_path, review in results.items():
            report += f"## {file_path}\n\n"
            report += f"{review}\n\n"
            report += "---\n\n"
        
        # Save report
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"Report saved to: {output_file}")
        return report

def main():
    """Main function to demonstrate the code reviewer"""
    
    # Initialize the reviewer
    reviewer = AICodeReviewer()
    
    print("🔍 AI Code Reviewer")
    print("=" * 50)
    
    while True:
        print("\nOptions:")
        print("1. Review a single file")
        print("2. Review multiple files")
        print("3. Review code snippet")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            file_path = input("Enter file path: ").strip()
            print("\n🔍 Analyzing...")
            result = reviewer.review_file(file_path)
            print("\n" + "="*50)
            print(result)
            
        elif choice == '2':
            files_input = input("Enter file paths (comma-separated): ").strip()
            file_paths = [f.strip() for f in files_input.split(',')]
            
            print("\n🔍 Analyzing multiple files...")
            results = reviewer.review_multiple_files(file_paths)
            
            # Generate report
            report = reviewer.generate_report(results)
            print("\n📊 Review completed! Check the generated report.")
            
        elif choice == '3':
            print("Enter your code (press Enter twice to finish):")
            code_lines = []
            while True:
                line = input()
                if line == "" and len(code_lines) > 0 and code_lines[-1] == "":
                    break
                code_lines.append(line)
            
            code = "\n".join(code_lines[:-1])  # Remove the last empty line
            language = input("Enter language (python/javascript/java/etc.): ").strip() or "python"
            
            print("\n🔍 Analyzing...")
            result = reviewer.analyze_code(code, language)
            print("\n" + "="*50)
            print(result)
            
        elif choice == '4':
            print("👋 Goodbye!")
            break
            
        else:
            print("❌ Invalid choice. Please try again.")

# Example usage
if __name__ == "__main__":
    # Example of reviewing a simple Python function
    sample_code = '''
def calculate_average(numbers):
    sum = 0
    for i in range(len(numbers)):
        sum += numbers[i]
    return sum / len(numbers)

def process_data(data):
    result = []
    for item in data:
        if item > 0:
            result.append(item * 2)
    return result
    '''
    reviewer = AICodeReviewer()
    
    # Analyze sample code
    print("Sample Code Review:")
    print("=" * 50)
    analysis = reviewer.analyze_code(sample_code, "python", "sample.py")
    print(analysis)
    
    print("\n" + "="*50)
    print("Starting interactive mode...")
    main()
