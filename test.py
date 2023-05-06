# import openai
# import gradio as gr
# import re
# from bs4 import BeautifulSoup
# import requests

# openai.api_key = "OPEN_API_KEY"

# programming_languages = {
#     "python": {
#         "definition": "high-level, interpreted programming language",
#         "resources": ["https://www.codecademy.com/learn/learn-python", "https://docs.python.org/3/", "https://www.py4e.com/book.php"],
#     },
#     "java": {
#         "definition": "class-based, object-oriented programming language",
#         "resources": ["https://www.codecademy.com/learn/learn-java", "https://docs.oracle.com/en/java/", "https://www.headfirstlabs.com/books/hfjava/"],
#     },
#     "javascript": {
#         "definition": "high-level, dynamic scripting language",
#         "resources": ["https://www.codecademy.com/learn/introduction-to-javascript", "https://developer.mozilla.org/en-US/docs/Web/JavaScript", "https://eloquentjavascript.net/"],
#     },
# }

# messages = [
#     {"role": "system", "content": "Welcome to the programming language chatbot! What programming language do you want to learn?"},
# ]

# def chatbot(input):
#     if input:
#         messages.append({"role": "user", "content": input})
       
#         language = None
#         for word in input.split():
#             if word.lower() in programming_languages:
#                 language = word.lower()
#                 break
#         if language:
           
#             definition = programming_languages[language]["definition"]
#             resources = programming_languages[language]["resources"]
            
#             resources_html = ""
#             for resource in resources:
#                 response = requests.get(resource)
#                 soup = BeautifulSoup(response.content, "html.parser")
#                 content = soup.get_text().strip()
#                 resources_html += f"- <b><a href='{resource}' target='_blank'>{content}</a></b><br>"
#             reply = f"{language.title()} is a {definition}. Here are some resources to help you learn:<br><br>{resources_html}"
#         else:
           
#             reply = "Please enter the name of a programming language."
#         messages.append({"role": "assistant", "content": reply})
#         return reply

# inputs = gr.inputs.Textbox(lines=7, label="Chat with AI")
# outputs = gr.outputs.HTML(label="Reply")

# gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="Programming Language Chatbot",
#              description="Enter the name of a programming language and the chatbot will provide a definition and learning resources.",
#              theme="compact").launch(share=True)



# <------------------------------------------------------------->

# import openai
# import gradio as gr

# openai.api_key = "OPEN_API_KEY"

# messages = [
#     {"role": "system", "content": "Define the given programming language and give resources to learn"},
# ]

# def chatbot(input):
#     if input:
#         messages.append({"role": "user", "content": input})
#         chat = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo", messages=messages
#         )

#         reply = chat.choices[0].message.content
#         messages.append({"role": "assistant", "content": reply})
#         return reply

# inputs = gr.inputs.Textbox(lines=7, label="Chat with AI")
# outputs = gr.outputs.Textbox(label="Reply")

# gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="AI Chatbot",
#              description="Programing Language you want to learn",
#              theme="compact").launch(share=True)




# <--------------------------------------------->


import openai
import gradio as gr
import re

openai.api_key = "OPEN_API_KEY"

programming_languages = {
    "python": {
        "definition": "high-level, interpreted programming language",
        "resources": "- <a href='https://www.codecademy.com/learn/learn-python'>Codecademy Python course</a>\n- <a href='https://docs.python.org/3/'>Python documentation</a>\n- <a href='https://www.py4e.com/book.php'>Python for Everybody textbook</a>",
    },
    "java": {
        "definition": "class-based, object-oriented programming language",
        "resources": "- <a href='https://www.codecademy.com/learn/learn-java'>Codecademy Java course</a>\n- <a href='https://docs.oracle.com/en/java/'>Java documentation</a>\n- <a href='https://www.headfirstlabs.com/books/hfjava/'>Head First Java textbook</a>",
    },
    "javascript": {
        "definition": "high-level, dynamic scripting language",
        "resources": "- <a href='https://www.codecademy.com/learn/introduction-to-javascript'>Codecademy JavaScript course</a>\n- <a href='https://developer.mozilla.org/en-US/docs/Web/JavaScript'>Mozilla JavaScript documentation</a>\n- <a href='https://eloquentjavascript.net/'>Eloquent JavaScript textbook</a>",
    },
}

messages = [
    {"role": "system", "content": "Welcome to the programming language chatbot! What programming language do you want to learn?"},
]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        
        language = None
        for word in input.split():
            if word.lower() in programming_languages:
                language = word.lower()
                break
        if language:
        
            definition = programming_languages[language]["definition"]
            resources = programming_languages[language]["resources"]
           
            resources_html = re.sub(r"\n", "<br>", resources)
            reply = f"{language.title()} is a {definition}. Here are some resources to help you learn:<br><br>{resources_html}"
        else:
          
            reply = "Please enter the name of a programming language."
        messages.append({"role": "assistant", "content": reply})
        return reply

inputs = gr.inputs.Textbox(lines=7, label="Chat with AI")
outputs = gr.outputs.HTML(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="Programming Language Chatbot",
             description="Enter the name of a programming language.",
             theme="compact").launch(share=True)