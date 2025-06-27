from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from prompt import CUSTOM_QA_PROMPT, CONDENSE_QUESTION_PROMPT
from langchain.chains import ConversationalRetrievalChain

load_dotenv()

def load_vectorstore(load_path="vectorstore"):
    """Load FAISS vectorstore"""
    embeddings = OpenAIEmbeddings()
    return FAISS.load_local(load_path, embeddings, allow_dangerous_deserialization=True)

def create_qa_chain(vectorstore):
    """Return ConversationalRetrievalChain with memory"""
    llm = ChatOpenAI(model_name="gpt-3.5-turbo")
    retriever = vectorstore.as_retriever()
    return ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        return_source_documents=True,
        condense_question_prompt=CONDENSE_QUESTION_PROMPT,  
        combine_docs_chain_kwargs={"prompt": CUSTOM_QA_PROMPT}  
    )
