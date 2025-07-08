from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_core.documents import Document
from langchain_google_genai import ChatGoogleGenerativeAI
import tempfile
import os
from dotenv import load_dotenv

# Load environment variables from .env.txt file
load_dotenv(dotenv_path=".env.txt")

# Retrieve API key from environment variables
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# Load embeddings model
embedding_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# Text chunking function
def chunk_text(text, chunk_size=1000, chunk_overlap=200):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_documents([Document(page_content=text)])

# Initialize Chroma DB
VECTORDB_DIR = tempfile.mkdtemp()

def get_vectorstore(docs):
    vectorstore = Chroma.from_documents(docs, embedding=embedding_model, persist_directory=VECTORDB_DIR)
    return vectorstore

# Initialize Gemini LLM
def get_llm(temperature=0.7):
    return ChatGoogleGenerativeAI(
        model="gemini-1.5-flash-latest",
        convert_system_message_to_human=True,
        temperature=temperature # Default temperature, can be overridden in generate_notes
    )

# Main RAG pipeline function to generate notes
def generate_notes(transcript_text, prompt_template, chunk_size=1000, chunk_overlap=200, retriever_k=5, llm_temperature=0.7):
    chunks = chunk_text(transcript_text, chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    vectordb = get_vectorstore(chunks)
    retriever = vectordb.as_retriever(search_kwargs={"k": retriever_k})

    qa_chain = RetrievalQA.from_chain_type(
        llm=get_llm(temperature=llm_temperature),
        retriever=retriever,
        chain_type="stuff",
        return_source_documents=False,
        chain_type_kwargs={"prompt": prompt_template}
    )

    # Use prompt to ask for notes
    response = qa_chain.run("Generate lecture notes based on the above transcript.")
    return response, retriever

# Chat interface to ask questions based on the same transcript
def chat_with_transcript(user_query, retriever):
    llm = get_llm()
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        return_source_documents=False
    )
    response = qa_chain.run(user_query)

    # Check for specific keywords in the response
    keywords = ["does not consist", "doesn't contain information", "not found", "absent", "missing", "does not explain", "not present", "not mentioned", "not included", "not discussed", "not covered", "not addressed", "not specified", "not detailed", "not elaborated", "not described", "not explained", "not contain", "not provided", "not available", "no information on", "no details on", "does not, however, provide a direct answer", "don't know", "cannot answer", "unable to answer", "no information available", "no relevant information found", "no details provided", "no context available", "not applicable", "not relevant", "not related", "not pertinent", "not useful", "not helpful", "not informative", "not insightful", "not conclusive", "not definitive", "not satisfactory", "can't answer", "can't provide", "can't find", "can't locate", "can't retrieve", "can't access", "can't obtain", "can't discover", "can't identify", "can't determine", "can't clarify", "can't explain", "can't elaborate", "can't detail", "can't describe", "can't specify", "can't mention", "can't cover", "can't address", "not applicable to the question"]
    if any(keyword in response.lower() for keyword in keywords):
        # Use normal chatbot for the response
        from langchain.schema import HumanMessage
        general_chatbot_response = llm.invoke([HumanMessage(content=user_query)])  # Properly formatted input for llm.invoke
        # Extract content from the response
        content = general_chatbot_response[0] if isinstance(general_chatbot_response, list) else general_chatbot_response.content
        return f"\nNote: The requested information was not found in the provided document. Hence, the general chatbot was used.\n\n{content}\n"

    return response
