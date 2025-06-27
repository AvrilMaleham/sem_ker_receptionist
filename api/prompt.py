from langchain import PromptTemplate
 
CUSTOM_QA_PROMPT = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are a helpful assistant. You have access to some retrieved document passages (below).  
Your job is twofold:
  1) If the answer can be found (verbatim or paraphrased) in the passages, respond with:
       "I used the provided documents to answer*: <your answer here>"
  2) If the passages do NOT contain any information that answers the question, respond with:
       "I did not find the answer in the provided documents. Answer from my own knowledge*: <your answer here>"
 
Passages:
{context}
 
Question: {question}
 
Answer exactly in one of the two formats above.
""".strip(),
)

CONDENSE_QUESTION_PROMPT = PromptTemplate.from_template("""
Given the following conversation and a follow-up question, rephrase the follow-up question to be a standalone question.
 
Chat History:
{chat_history}
 
Follow-up Question:
{question}
 
Standalone Question:
""".strip(),
)