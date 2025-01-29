from flask import Flask, request, jsonify
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

app = Flask(__name__)

# Load the vector store
embeddings = OpenAIEmbeddings()
vector_store = FAISS.load_local("vector_store", embeddings)

@app.route('/query', methods=['POST'])
def query():
    """Handle user queries."""
    query = request.json['query']
    llm = OpenAI()
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vector_store.as_retriever())
    result = qa.run(query)
    return jsonify({"answer": result})

if __name__ == '__main__':
    app.run(debug=True)