# Multi-Modal Semantic Search Using LangChain
This project implements a multi-modal semantic search system that supports PDF, CSV, and image files. Utilizing LangChain for document loading, splitting, and vector storage with Qdrant, it enables efficient retrieval-augmented generation (RAG) to provide contextually accurate answers using HuggingFace embeddings and a Ollama large language model.

## Overview

This project implements a multi-modal question-answering system that supports PDF, CSV, and image files as data sources. Leveraging LangChain's components, the system allows for efficient loading, processing, and semantic search of documents using embeddings and vector storage with Qdrant.

## Features

- **Multi-Modal Support**: Load and process PDF, CSV, and image files.
- **Document Loading**: Utilizes LangChain document loaders for various file types.
- **Content Splitting**: Splits documents into manageable chunks for improved processing.
- **Vector Storage**: Implements Qdrant for efficient vector storage and retrieval.
- **Semantic Search**: Uses retrieval-augmented generation (RAG) for contextually accurate answers.
- **Integration with HuggingFace**: Employs HuggingFace embeddings for enhanced vector representation.
- **Language Model**: Integrates with Ollama's LLM for nuanced and comprehensive responses.

## Getting Started

### Prerequisites

- Python 3.7 or higher
  
### Installation

  1. Clone the repository:
   ```bash
   git clone https://github.com/MubashirAI12/Multi-Modal-Semantic-Search-LangChain-.git
   cd multi-modal-semantic-search
   ```
  2. Set up environment variables: Create a .env file in the root directory and add the following variables:
   ```
   qdrant_url=your_qdrant_url
   qdrant_api=your_qdrant_api_key
  ```


### Usage
1. Run the main script:
  ```bash
  python main.py
  ```

2. Select the type of file you wish to process:
  - Enter 1 for a PDF file
  - Enter 2 for a CSV file
  - Enter 3 for an image file

3. Input your query when prompted.
