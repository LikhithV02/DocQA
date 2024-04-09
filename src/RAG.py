from ragatouille import RAGPretrainedModel
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

llm = ChatGroq(temperature=0, groq_api_key=GROQ_API_KEY, model_name="mixtral-8x7b-32768")
RAG = RAGPretrainedModel.from_pretrained("colbert-ir/colbertv2.0")
system_prompt = """You are a helpful assistant, you will use the provided context to answer user questions.
Read the given context before answering questions and think step by step. If you can not answer a user question based on 
the provided context, inform the user. Do not use any other information for answering user. Provide a detailed answer to the question."""
prompt_template = (
                system_prompt
                + """
    
            Context: {history} \n {context}
            User: {question}
            Answer:"""
            )
prompt = PromptTemplate(input_variables=["history", "context", "question"], template=prompt_template)
memory = ConversationBufferMemory(input_key="question", memory_key="history")

def rag(full_string):
    RAG.index(
        collection=[full_string],
        index_name="vector_db",
        max_document_length=512,
        split_documents=True,
    )
    retriever = RAG.as_langchain_retriever(k=5)
    qa = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",  # try other chains types as well. refine, map_reduce, map_rerank
            retriever=retriever,
            return_source_documents=True,  # verbose=True,
            chain_type_kwargs={"prompt": prompt, "memory": memory},
        )
    return qa