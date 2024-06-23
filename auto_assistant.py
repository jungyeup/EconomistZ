from phi.assistant import Assistant
from phi.knowledge.pdf import PDFUrlKnowledgeBase
from phi.vectordb.pgvector import PgVector2

knowledge_base = PDFUrlKnowledgeBase(
    # Read PDF from this URL
    path=r"C:\Users\jung\Desktop\EconomistLLM\data",
    # Store embeddings in the `ai.recipes` table
    vector_db=PgVector2(
        collection="pdf_documents",
        db_url="postgresql+psycopg://ai:ai@localhost:5532/ai",
    ),
)
# Comment out as the knowledge base is already loaded.
# knowledge_base.load(recreate=False)

assistant = Assistant(
    knowledge_base=knowledge_base,
    # Show tool calls in the response
    show_tool_calls=True,
    # Enable the assistant to search the knowledge base
    search_knowledge=True,
    # Enable the assistant to read the chat history
    read_chat_history=True,
)
assistant.print_response("기술적 분석이란?", markdown=True)
assistant.print_response("이전 질문이 뭐였지?", markdown=True)
