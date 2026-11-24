from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = PyMuPDFLoader(
    r"C:\Users\rolex\OneDrive\Desktop\Agentic AI\Agentic_AI_Roadmap.pdf"
)

document = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)

result = splitter.split_documents(document)

print(result)
