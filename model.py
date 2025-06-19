from sentence_transformers import SentenceTransformer, util
import os

# Load BERT model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load documents
DOC_DIR = "AILA_2019_dataset/Object_casedocs"
documents = {}
for filename in os.listdir(DOC_DIR):
    with open(os.path.join(DOC_DIR, filename), 'r', encoding='utf-8') as f:
        documents[filename] = f.read()

# Precompute embeddings
doc_embeddings = model.encode(list(documents.values()), convert_to_tensor=True)
doc_names = list(documents.keys())

def get_top_k_documents(query, k=5):
    query_embedding = model.encode(query, convert_to_tensor=True)
    similarities = util.pytorch_cos_sim(query_embedding, doc_embeddings)[0]
    top_k = similarities.argsort(descending=True)[:k]
    return [doc_names[i] for i in top_k]
