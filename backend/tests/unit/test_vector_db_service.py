from backend.src.services import vector_db_service


def test_ensure_collection():
    # Should not raise error
    vector_db_service.ensure_collection()


def test_upsert_and_search():
    # Should not raise error with dummy data
    vector_db_service.upsert_vector(123, [0.1] * 768, {"meta": "test"})
    hits = vector_db_service.search_vector([0.1] * 768)
    assert isinstance(hits, list) or hasattr(hits, "__iter__")
