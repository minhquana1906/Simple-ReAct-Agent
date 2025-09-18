from backend.src.services import rag_service


def test_add_document_embedding():
    # Should not raise error with dummy data
    rag_service.add_document_embedding(1, [0.1] * 768, {"meta": "test"})


def test_query_rag():
    # Should return a list (may be empty)
    result = rag_service.query_rag([0.1] * 768)
    assert isinstance(result, list)
