# docker run -d -e POSTGRES_DB=ai -e POSTGRES_USER=ai -e POSTGRES_PASSWORD=ai -e PGDATA=/var/lib/postgresql/data/pgdata -v pgvolume:/var/lib/postgresql/data -p 5532:5432 --name pgvector phidata/pgvector:16


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
# Load the knowledge base
knowledge_base.load(recreate=False)

assistant = Assistant(
    knowledge_base=knowledge_base,
    # The add_references_to_prompt will update the prompt with references from the knowledge base.
    add_references_to_prompt=True,
)
assistant.print_response("기술적 분석이란?", markdown=True)
