import streamlit as st
import pandas as pd
from PIL import Image
import os, json
from dotenv import load_dotenv
from pdf2image import convert_from_path, convert_from_bytes
import tempfile
from langchain_groq import ChatGroq
from groq import Groq
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from donut_inference import inference
from classification import predict
from non_form_llama_parse import extract_text
from RAG import rag

load_dotenv()
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

# llm = ChatGroq(temperature=0, groq_api_key=GROQ_API_KEY, model_name="mixtral-8x7b-32768")
client = Groq(api_key=GROQ_API_KEY)

if "current_page" not in st.session_state:
    st.session_state["current_page"] = "upload"
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hi, How can I help you today?"}]
if "conversation_state" not in st.session_state:
        st.session_state["conversation_state"] = [{"role": "assistant", "content": "Hi, How can I help you today?"}]
if "json_data" not in st.session_state:
    st.session_state.json_data = None
if "rag" not in st.session_state:
    st.session_state.rag = None
    
USER_AVATAR = "👤"
BOT_AVATAR = "🤖"

def csv_chat_interface(data):
    st.title("DocQA")
    for message in st.session_state.messages:
        image = USER_AVATAR if message["role"] == "user" else BOT_AVATAR
        with st.chat_message(message["role"], avatar=image):
            st.markdown(message["content"])
    
    system_prompt = f'''You are a helpful assistant, you will use the provided context to answer user questions. You are great at reding json data.
Read the given context before answering questions and think step by step. If you can not answer a user question based on 
the provided context, inform the user. Do not use any other information for answering user. Provide a detailed answer to the question.\n
Context:\n
{data}
'''
    print("System Prompt: ", system_prompt)
    if prompt := st.chat_input("User input"):
        st.chat_message("user", avatar=USER_AVATAR).markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})
        conversation_context = st.session_state["conversation_state"]
        conversation_context.append({"role": "user", "content": prompt})
        # Define an empty context variable
        context = []
        # Add system prompt to context if desired
        context.append({"role": "system", "content": system_prompt})
        # Add conversation context to context
        context.extend(st.session_state["conversation_state"])
        response = client.chat.completions.create(
            messages=context,
            model="mixtral-8x7b-32768",
            temperature=0,
            max_tokens=1024,
            top_p=1,
            stop=None,
            stream=True,
        )
        
        with st.chat_message("assistant", avatar=BOT_AVATAR):
            # st.markdown(str(result))
            result = ""
            res_box = st.empty()
            for chunk in response:
                if chunk.choices[0].delta.content:
                    new_content = chunk.choices[0].delta.content
                    result += new_content   # Add a space to separate words
                    res_box.markdown(f'{result}')
        assistant_response = result
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})
        conversation_context.append({"role": "assistant", "content": assistant_response})
        
def rag_chat_interface(rag):
    st.title("DocQA")
    for message in st.session_state.messages:
        image = USER_AVATAR if message["role"] == "user" else BOT_AVATAR
        with st.chat_message(message["role"], avatar=image):
            st.markdown(message["content"])
    if prompt := st.chat_input("User input"):
        st.chat_message("user", avatar=USER_AVATAR).markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})
        res = rag(prompt)
        answer, docs = res["result"], res["source_documents"]
        with st.chat_message("assistant", avatar=BOT_AVATAR):
            st.markdown(str(answer))
        st.session_state.messages.append({"role": "assistant", "content": str(answer)})

def upload():
    st.title('DocQA')
    st.subheader("These are types of forms used to fine-tune DONUT model")

    # Define the paths to your images
    image_paths = [
        "/app/cropped_1099-Div.jpg",
        "/app/cropped_1099-Int.jpg",
        "/app/cropped_w2.jpg",
        "/app/cropped_w3.jpg"
    ]

    # Define the captions for your images
    captions = ["1099-Div", "1099-Int", "W2", "W3"]

    # Display the images side-by-side with captions
    cols = st.columns(len(image_paths))
    for col, image_path, caption in zip(cols, image_paths, captions):
        col.image(image_path, caption=caption)
        
    st.subheader("Try it out")
    uploaded_files = st.file_uploader("Choose PDF files", type="pdf", accept_multiple_files=True)
    full_string = ""
    all_data = []
    # combined_data_dict = {}
    for uploaded_file in uploaded_files:
        if uploaded_file is not None:
            with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_file:
                temp_file.write(uploaded_file.getvalue())
                temp_file.flush()
                pages = convert_from_path(temp_file.name, 300)
                # width, height = pages[0].size
                # print(type(pages[0]))
                img_classification = pages[0].resize((1024, 1024), Image.LANCZOS)
                pred = predict(img_classification)
                
                if pred != "Non_Form":
                    img = pages[0].resize((1864, 1440), Image.LANCZOS)
                    # st.write(width, height)
                    data_dict = inference(img)
                    data_dict['filename'] = uploaded_file.name
                    # items_string = ""
                    # for key, value in data_dict['items'].items():
                    #     items_string += f"{key}: {value}\n"
                    # full_string += items_string
                    # combined_data_dict.update(data_dict)
                    # df = pd.DataFrame([data_dict], columns=data_dict.keys())
                    print(data_dict)
                    all_data.append(data_dict)
                else:
                    text = extract_text(temp_file.name)
                    full_string += text
            os.remove(temp_file.name)
    
    if all_data:
        # combined_df = pd.concat(all_data, ignore_index=True)
        # st.dataframe(combined_df)
        # df = pd.DataFrame([combined_data_dict], columns=combined_data_dict.keys())
        # st.dataframe(df)
        all_data_string = "\n\n".join(json.dumps(data_dict) for data_dict in all_data)
        st.session_state.json_data = all_data_string
        # print(all_data)
        # st.write(all_data)
        if st.button("Start Chatting"):
            st.session_state["current_page"] = "csv_chat_ui"
            st.rerun()
            
    elif full_string:
        qa = rag(full_string)
        st.session_state.rag = qa
        if st.button("Start Chatting"):
            st.session_state["current_page"] = "rag_ui"
            st.rerun()
    st.markdown('''
# Instructions:

1. **Ensure all uploads are in PDF format**. This ensures compatibility and uniform processing across documents.

2. **Submit forms in portrait orientation only**. Landscape formats are not supported and may result in processing errors.

3. **Forms must have a minimum resolution of 1864x1440**. This is crucial for the clarity and legibility necessary for accurate parsing.

4. **Multiple documents can be uploaded simultaneously**; however, the combined size of these documents should not exceed 10MB.

5. **Donut model parses specific forms**: 1099-Div, 1099-Int, W2, and W3. Non-form documents are also processable.
            ''')    

def main():
    if st.session_state["current_page"] == "upload":
        upload()
    elif st.session_state["current_page"] == "csv_chat_ui":
        csv_chat_interface(st.session_state.get('json_data'))
    elif st.session_state["current_page"] == "rag_ui":
        rag_chat_interface(st.session_state.get('rag'))         
if __name__ == '__main__':
    main()
