from dotenv import load_dotenv
import os, cohere
import google.generativeai as genai  
from groq import Groq
from fpdf import FPDF


load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)
co = cohere.ClientV2(os.getenv("COHERE_API_KEY"))


model = genai.GenerativeModel("gemini-1.5-flash")      # valid public model id :contentReference[oaicite:1]{index=1}
resp  = model.generate_content(
                "Suggest some final year project ideas for a computer science student in the field of agentic AI.The ideas should be innovative, practical, and suitable for a final year project. Provide a brief description of each idea, including its potential applications and challenges.Also it should be technically challenging and not something that can be done easily using agentic ai tools like n8n or Zapier.",
)







chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Suggest some final year project ideas for a computer science student in the field of agentic AI.The ideas should be innovative, practical, and suitable for a final year project. Provide a brief description of each idea, including its potential applications and challenges.Also it should be technically challenging and not something that can be done easily using agentic ai tools like n8n or Zapier.",
        }
    ],
    model="llama-3.3-70b-versatile",
)



response = co.chat(
    model="command-r-plus",                    
    messages=[{
        "role": "user",
        "content": "Suggest some final year project ideas for a computer science student in the field of agentic AI.The ideas should be innovative, practical, and suitable for a final year project. Provide a brief description of each idea, including its potential applications and challenges.Also it should be technically challenging and not something that can be done easily using agentic ai tools like n8n or Zapier."
    }]
)


 

with open("project_ideas.txt", "w", encoding="utf‑8") as f:
       f.write(resp.text + "\n\n" + chat_completion.choices[0].message.content + "\n\n" + response.message.content[0].text)
       
with open("project_ideas.txt", "r", encoding="utf‑8") as f:
    result_text= f.read()
    
prompt = (
    "Re‑organize the text below into a clean, numbered list of project ideas,include all ideas. "
    "For each idea add a one‑line description, applications, and main challenges as provided.\n\n"
    + result_text
)

resp = model.generate_content(prompt)
with open("project_ideas_cleaned.txt", "w", encoding="utf‑8") as f:
    f.write(resp.text)
    
    
def text_to_pdf(text, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    for line in text.split('\n'):
        pdf.cell(200, 10, txt=line, ln=True)
    
    pdf.output(filename)    
    
text_to_pdf(resp.text, "project_ideas.pdf")    