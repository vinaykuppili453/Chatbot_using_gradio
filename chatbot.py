import openai
import gradio as gr

# Set your OpenAI API key
openai.api_key = 'enter your secret key here'

# Function to generate responses from ChatGPT
def generate_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use the appropriate model name
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.7,
        )
        message = response.choices[0].message['content'].strip()
        return message
    except Exception as e:
        return str(e)

# Gradio interface
def chat_interface(input_text):
    response = generate_response(input_text)
    return response

# Create Gradio interface
iface = gr.Interface(
    fn=chat_interface,
    inputs="text",
    outputs="text",
    title="ChatGPT-like Chatbot",
    description="Ask me anything!",
)

# Launch the interface
iface.launch(share=True)
