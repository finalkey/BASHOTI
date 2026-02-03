from typing import List, Dict
from qdrant_client import QdrantClient
from qdrant_client.http import models as rest
from app.core.config import settings

class VectorService:
    def __init__(self, collection_name: str = "documents"):
        # Assumes Qdrant runs at settings.QDRANT_URL
        url = settings.QDRANT_URL.replace("http://", "").replace("https://", "")
        host, port = url.split(":")
        port = int(port)
        self.client = QdrantClient(host=host, port=port, prefer_grpc=False, api_key=settings.QDRANT_API_KEY)
        self.collection_name = collection_name

    def search(self, query: str, top_k: int = 5) -> List[Dict]:
        # In a real implementation you'd compute embeddings for 'query' then search
        # Here we use qdrant simple payload search placeholder
        results = self.client.search(
            collection_name=self.collection_name,
            query_vector=[0.0] * 768,  # placeholder: replace with real embedding
            limit=top_k,
        )
        # Convert qdrant hits to dicts
        hits = [{"id": r.id, "score": r.score, "payload": r.payload} for r in results]
        return hits
