import numpy as np
import logging
from typing import List, Dict, Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class VectorMemory:
    """
    Omega-System Distributed Vector Memory Mesh.
    Handles embedding storage and similarity search for autonomous agents.
    """
    def __init__(self, dimension: int = 1536):
        self.dimension = dimension
        self.vectors = np.empty((0, dimension))
        self.metadata: List[Dict] = []
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger("VectorMemory")

    def add_embedding(self, embedding: List[float], meta: Dict):
        """Adds a high-dimensional embedding to the memory mesh."""
        emb_np = np.array(embedding).reshape(1, -1)
        if emb_np.shape[1] != self.dimension:
            raise ValueError(f"Dimension mismatch: expected {self.dimension}")
        
        self.vectors = np.vstack([self.vectors, emb_np])
        self.metadata.append(meta)
        self.logger.info(f"Stored embedding for {meta.get('source', 'unknown')}")

    def search(self, query: List[float], top_k: int = 5) -> List[Dict]:
        """Performs cosine similarity search."""
        if not isinstance(top_k, int) or top_k <= 0:
            return []
        if self.vectors.shape[0] == 0:
            return []

        query_np = np.array(query).reshape(1, -1)
        if query_np.shape[1] != self.dimension:
            raise ValueError(f"Dimension mismatch: expected {self.dimension}")
        similarities = np.dot(self.vectors, query_np.T).flatten()
        top_indices = np.argsort(similarities)[-top_k:][::-1]

        return [self.metadata[i] for i in top_indices]

if __name__ == "__main__":
    mem = VectorMemory()
    dummy_emb = [0.1] * 1536
    mem.add_embedding(dummy_emb, {"source": "kernel_boot_log"})
    results = mem.search(dummy_emb)
    print(f"Found {len(results)} matches.")