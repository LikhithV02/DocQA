import streamlit as st
import pandas as pd
from PIL import Image
import os
from dotenv import load_dotenv
from pdf2image import convert_from_path, convert_from_bytes
import tempfile
from langchain_groq import ChatGroq
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from donut_inference import inference
from classification import predict
from non_form_llama_parse import extract_text
from RAG import rag

load_dotenv()
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

llm = ChatGroq(temperature=0, groq_api_key=GROQ_API_KEY, model_name="mixtral-8x7b-32768")

if "current_page" not in st.session_state:
    st.session_state["current_page"] = "upload"
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hi, How can I help you today?"}]
if "csv_agent" not in st.session_state:
    st.session_state.csv_agent = None
if "rag" not in st.session_state:
    st.session_state.rag = None
    
USER_AVATAR = "👤"
BOT_AVATAR = "🤖"

def csv_chat_interface(agent):
    st.title("DocQA")
    for message in st.session_state.messages:
        image = USER_AVATAR if message["role"] == "user" else BOT_AVATAR
        with st.chat_message(message["role"], avatar=image):
            st.markdown(message["content"])
    if prompt := st.chat_input("User input"):
        st.chat_message("user", avatar=USER_AVATAR).markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})
        result = agent.run(str(prompt))
        
        with st.chat_message("assistant", avatar=BOT_AVATAR):
            st.markdown(str(result))
        st.session_state.messages.append({"role": "assistant", "content": str(result)})
        
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
                    # items_string = ""
                    # for key, value in data_dict['items'].items():
                    #     items_string += f"{key}: {value}\n"
                    # full_string += items_string
                    df = pd.DataFrame([data_dict['items']], columns=data_dict['items'].keys())
                    all_data.append(df)
                else:
                    text = extract_text(temp_file.name)
                    full_string += text
            os.remove(temp_file.name)
    
    if all_data:
        combined_df = pd.concat(all_data, ignore_index=True)
        st.dataframe(combined_df)
        with tempfile.NamedTemporaryFile(mode='w+', suffix='.csv', delete=False) as temp_csv:
            combined_df.to_csv(temp_csv.name, index=False)
            agent = create_csv_agent(
            llm,
            temp_csv.name,
            verbose=True,
            agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            )
            st.session_state.csv_agent = agent
        if st.button("Start Chatting"):
            st.session_state["current_page"] = "csv_chat_ui"
            st.rerun()
            
    elif full_string:
        qa = rag(full_string)
        st.session_state.rag = qa
        if st.button("Start Chatting"):
            st.session_state["current_page"] = "rag_ui"
            st.rerun()
        

def main():
    if st.session_state["current_page"] == "upload":
        upload()
    elif st.session_state["current_page"] == "csv_chat_ui":
        csv_chat_interface(st.session_state.get('csv_agent'))
    elif st.session_state["current_page"] == "rag_ui":
        rag_chat_interface(st.session_state.get('rag'))         
if __name__ == '__main__':
    main()