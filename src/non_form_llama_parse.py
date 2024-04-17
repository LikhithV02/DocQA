from llama_parse import LlamaParse
from dotenv import load_dotenv
import os

load_dotenv()
LLAMA_PARSE = os.getenv('LLAMA_PARSE')

parser = LlamaParse(
    api_key = LLAMA_PARSE,
    result_type="text",  # "markdown" and "text" are available
    num_workers=4, # if multiple files passed, split in `num_workers` API calls
    verbose=True,
    language="en" # Optionaly you can define a language, default=en
)

def extract_text(pdf_path):
    documents = parser.load_data(pdf_path)
    all_text = ""
    for document in documents:
        all_text += document.text + '\n'
    return all_text.strip()  # Remove the trailing newline character

# combined_text = extract_text("/app/Non_form_pdfs/chapter-17-web-designing2.pdf")
# print(combined_text)