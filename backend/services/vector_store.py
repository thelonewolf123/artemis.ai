from langchain_community.vectorstores import SQLiteVec
from langchain_text_splitters import RecursiveCharacterTextSplitter

from typing import List

from backend.services.embedding import embedding_function
from backend.config import settings


class VectorStore:
    vector_store: SQLiteVec

    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100,
        )

        self.vector_store = SQLiteVec(
            table="long_term_memory",
            db_file=settings.vector_db_path,
            embedding=embedding_function,
        )

    def add(self, doc: str, user_id: str):
        """
        Split and store a document in long-term memory for a user.
        """
        chunks = self.text_splitter.split_text(doc)

        metadatas = [{"user_id": user_id} for _ in chunks]

        self.vector_store.add_texts(
            texts=chunks,
            metadatas=metadatas,
        )

    def search(self, query: str, user_id: str, k: int = 5) -> List[str]:
        """
        Retrieve top-k relevant chunks for a user.
        """
        results = self.vector_store.similarity_search(
            query=query,
            k=k,
            filter={"user_id": user_id},
        )

        return [doc.page_content for doc in results]
