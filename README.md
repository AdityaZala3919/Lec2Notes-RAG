# 📚 Lec2Notes: RAG-Powered Lecture Summaries

Transform your lecture transcripts into organized, readable, and exportable study material with the power of **Retrieval-Augmented Generation (RAG)**.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## 🚀 Features

### 📝 **Smart Note Generation**
- **Multiple formats**: Choose from 16+ predefined templates including Mind Maps, Flashcards, Exam Highlights, and more
- **Custom templates**: Create your own personalized note format
- **RAG-powered**: Notes are generated based on actual lecture content, not just LLM guesswork

### 💬 **Interactive Chat Interface**
- Ask questions about your lecture content
- Get contextually relevant answers from your transcript
- Fallback to general AI knowledge when specific information isn't found

### 📤 **Export Options**
- Download notes as **Markdown** files
- Export to **PDF** with custom styling
- Ready-to-use formats for studying and sharing

### ⚙️ **Customizable Parameters**
- **Chunk Size**: Control how text is segmented (100-5000 characters)
- **Chunk Overlap**: Ensure context continuity between chunks
- **Retriever Top-K**: Adjust number of relevant documents retrieved
- **LLM Temperature**: Fine-tune creativity vs. consistency in outputs

### 📁 **Multiple File Formats**
- **TXT**: Plain text transcripts
- **PDF**: Extracted text from PDF documents
- **SRT**: Subtitle files from video recordings

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- Google Gemini API key

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/AdityaZala3919/Lec2Notes-RAG.git
   cd Lec2Notes-RAG
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env.txt` file in the root directory:
   ```
   GOOGLE_API_KEY=your_google_gemini_api_key_here
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

## 📋 Requirements

Create a `requirements.txt` file with these dependencies:

```txt
faiss-cpu
langchain>=0.1.17
langchain-community>=0.0.24
langchain-core>=0.1.44
streamlit
google-generativeai>=0.3.2
langchain-google-genai>=0.0.9
markdown-pdf
python-dotenv
```

## 🎯 Usage

### Basic Workflow

1. **Upload your transcript** (TXT, PDF, or SRT format)
2. **Select a note format** from the dropdown menu
3. **Adjust hyperparameters** (optional) in the sidebar
4. **Click "Generate Notes"** to create your study material
5. **Download** your notes in Markdown or PDF format
6. **Chat with your transcript** using the Q&A interface

### Available Note Formats

- **Detailed Structured Study Notes**: Comprehensive academic summaries
- **Conceptual Mind Map Style**: Hierarchical concept organization
- **Step-by-Step Explanation**: Sequential learning format
- **Comparison Table**: Side-by-side concept analysis
- **Key Terms and Definitions**: Glossary-style notes
- **Flashcard Style**: Question-answer format for memorization
- **Formula + Concept Sheet**: Mathematical formulas and explanations
- **Topic Clusters**: Grouped related concepts
- **Cause and Effect Notes**: Causal relationship mapping
- **Exam-Ready Highlights**: Test-focused summaries
- **Practical Applications**: Real-world use cases
- **Pros and Cons**: Balanced analysis format
- **Problem-Solution Format**: Issue-resolution structure
- **Explainer with Analogies**: Concept explanation with comparisons
- **Highlight + Expand**: Key terms with detailed explanations
- **Quick Review Cheat Sheet**: Concise reference material
- **Custom Template**: Your personalized format

## 🏗️ Architecture

### RAG Pipeline
```
Transcript → Text Chunking → Vector Embeddings → Vector Database (FAISS) → Retrieval → LLM Generation → Formatted Notes
```

### Tech Stack
- **Frontend**: Streamlit for interactive web interface
- **RAG Framework**: LangChain for document processing and retrieval
- **Embeddings**: Google Generative AI Embeddings (`models/embedding-001`)
- **LLM**: Google Gemini 1.5 Flash
- **Vector Store**: FAISS for efficient similarity search
- **PDF Processing**: pdfplumber for text extraction

## 📂 Project Structure

```
Lec2Notes-RAG/
├── app.py                 # Main Streamlit application
├── rag_pipeline.py        # RAG implementation and LLM integration
├── transcript_loader.py   # File processing utilities
├── prompts.py            # Note format templates
├── pdf_style.css         # PDF export styling
├── requirements.txt      # Python dependencies
├── .env.txt             # Environment variables (create this)
└── README.md            # Project documentation
```

## 🔧 Configuration

### Hyperparameters

- **Chunk Size** (100-5000): Size of text segments for processing
- **Chunk Overlap** (0-1000): Overlap between chunks for context preservation
- **Retriever Top-K** (1-20): Number of relevant documents retrieved
- **LLM Temperature** (0.0-1.0): Controls randomness in generation

### Environment Variables

```bash
GOOGLE_API_KEY=your_google_gemini_api_key
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **LangChain** for the RAG framework
- **Google Gemini** for powerful language modeling
- **Streamlit** for the intuitive web interface
- **FAISS** for efficient vector similarity search

## 🌟 Star History

If you find this project useful, please consider giving it a star! ⭐

## 🔮 Future Updates

I am constantly working to improve Lec2Notes! Here's what's coming next:

### 🎥 YouTube Video Integration
- **Direct YouTube URL input**: Simply paste a YouTube video link to generate notes
- **Automatic transcription**: Extract audio and convert speech to text using Google Speech-to-Text API
- **Timestamp references**: Notes will include clickable timestamps linking back to specific video moments
- **Multi-language support**: Generate notes from videos in different languages
- **Video chapter detection**: Automatically segment notes based on video chapters

### ☁️ Google Cloud Platform Integration
- **Cloud Storage**: Store transcripts and generated notes in Google Cloud Storage
- **Cloud Functions**: Deploy RAG pipeline as serverless functions for better scalability
- **Cloud Run**: Container-based deployment for production-ready applications
- **Cloud Firestore**: Real-time database for session management and user data
- **Cloud AI Platform**: Enhanced ML model serving with auto-scaling capabilities
- **Cloud CDN**: Faster content delivery for global users

### 🗄️ MongoDB Session Management
- **User authentication**: Secure login/signup with session management
- **Session persistence**: Save and resume note generation sessions
- **Note history**: Access previously generated notes from any device
- **User preferences**: Store custom templates and hyperparameter settings
- **Collaboration features**: Share notes and sessions with classmates
- **Analytics dashboard**: Track usage patterns and note generation statistics

Stay tuned for these exciting updates! Follow the repository to get notified about new releases.

---
## 📧 Contact

For questions or suggestions, please open an issue or contact [adityazala404@gmail.com](mailto:adityazala404@gmail.com).<br>
**Made with ❤️ by [Aditya Zala](https://github.com/AdityaZala3919)**
