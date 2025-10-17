from langchain_astradb import AstraDBVectorStore
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from src.data_converter import DataConverter
from src.config import Config

class DataIngestion:
    def __init__(self):
        self.embedding = HuggingFaceEndpointEmbeddings(model = Config.EMBEDDING_MODEL)
        
        self.vstore = AstraDBVectorStore(
            embedding = self.embedding,
            collection_name = "Flipkart",
            api_endpoint = Config.ASTRA_DB_API_ENDPOINT,
            token = Config.ASTRA_DB_APPLICATION_TOKEN,
            namespace = Config.ASTRA_DB_KEYSPACE
        )
        
        
    def ingest(self, load_existing:True):
        if load_existing:
            return self.vstore
        
        docs = DataConverter("data\Flipkart_Reviews - Electronics.csv").convert()
        
        BATCH_SIZE = 200
        
        for i in range(0, len(docs), BATCH_SIZE):
            batch = docs[i:i + BATCH_SIZE]
            self.vstore.add_documents(batch)
        
        return self.vstore
    
# if __name__ =="__main__":
#     ingestor = DataIngestion()
#     ingestor.ingest(load_existing=False)