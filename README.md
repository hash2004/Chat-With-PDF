# Chat-With-PDF
"Chat with Your PDF" is a Q&A chatbot that lets users interact with their PDF files conversationally. This application is built using Streamlit and utilizes Retrieval-Augmented Generation (RAG) technology, which combines the benefits of information retrieval with state-of-the-art language generation. This innovative approach allows the chatbot to provide precise answers by retrieving relevant information from a PDF and then generating contextually appropriate responses.

Designed for efficiency and ease of use, the application provides a user-friendly interface where users can upload their PDF documents and start engaging with them directly through questions and answers. Whether you're a student needing quick summaries, a researcher seeking specific information, or a professional looking to extract insights without reading entire documents, "Chat with Your PDF" offers a powerful tool for interactive document analysis.

## Demo 
![Demo of the app](https://github.com/hash2004/Chat-With-PDF/blob/main/images/Demo.png)

## Architecture 
1. **Architecture Overview**: The application utilizes the Retrieval-Augmented Generation (RAG) format for efficient data handling.
2. **PDF Processing**: Upon uploading a PDF file, the program employs PDFminer to extract text, which is then segmented into manageable chunks.
3. **Embedding Creation**: These text chunks are processed using OpenAI's API to generate embeddings that capture their semantic meaning.
4. **Vector Database Storage**: The generated embeddings are stored in a vector database, facilitating quick retrieval.
5. **Query Handling**: When a user submits a question, the application converts this query into embeddings.
6. **Similarity Search**: It performs a similarity search in the vector database to find the most relevant text chunks.
7. **Result Delivery**: The program then presents the most relevant information as an answer to the user’s query.

![Architecture](https://github.com/hash2004/Chat-With-PDF/blob/main/images/Architecture.png)
