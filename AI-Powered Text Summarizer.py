import openai
openai.api_key = 'api key paste' #and ofc billing is required for this code to run
def summarize_text(text):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Summarize the following text: {text}",
        max_tokens=100,
        temperature=0.5
    ) 
    return response.choices[0].text.strip()
text = "OpenAI is an artificial intelligence research laboratory consisting of the for-profit OpenAI LP and its parent company, the non-profit OpenAI Inc. OpenAI was founded in December 2015 by Elon Musk, Sam Altman, Greg Brockman, Ilya Sutskever, John Schulman, and Wojciech Zaremba. OpenAI's mission is to ensure that artificial general intelligence (AGI) benefits all of humanity."
summary = summarize_text(text)
print("Summary:", summary)
