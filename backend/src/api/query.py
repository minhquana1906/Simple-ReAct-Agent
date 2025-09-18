from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class QueryRequest(BaseModel):
    query: str


@router.post("/query")
async def query_endpoint(request: QueryRequest):
    # Placeholder: In production, embed the query and call query_rag
    # Here, return 501 Not Implemented
    raise HTTPException(status_code=501, detail="RAG query not implemented yet.")
    # Example for future:
    # embedding = embed_query(request.query)
    # results = query_rag(embedding)
    # return {"result": results}
