from fastapi import APIRouter
from schemas import QueryRequest
import globals
import psycopg2
from psycopg2.extras import RealDictCursor

router = APIRouter()

def get_db_connection():
    return psycopg2.connect(
        dbname="chatbotdb",
        user="postgres",
        password="postgres",
        host="db",
        port="5432"
    )
    
chat_history = []

@router.post("/ask/")
async def ask_question(request: QueryRequest):
     
    if globals.qa_chain is None:
        return {"error": "QA chain is not initialized yet."}
    
    # Save user message
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO chat_sessions (role, message) VALUES (%s, %s)",
        ("user", request.query)
    )
    conn.commit()

    # Generate assistant response
    response = globals.qa_chain.invoke({
        "question": request.query,
        "chat_history": chat_history
    })
    answer = response.get("answer", "Sorry, I couldn't find an answer.")
     
    # Save assistant response
    cur.execute(
        "INSERT INTO chat_sessions (role, message) VALUES (%s, %s)",
        ("assistant", answer)
    )
    conn.commit()
    cur.close()
    conn.close()
    
    chat_history.append((request.query, response["answer"]))

    return {"answer": answer}

@router.get("/session/")
async def get_session():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(
       """
    SELECT role, message, created_at
    FROM (
        SELECT role, message, created_at
        FROM chat_sessions
        ORDER BY created_at DESC
        LIMIT 10
    ) AS sub
    ORDER BY created_at ASC
    """
)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows
