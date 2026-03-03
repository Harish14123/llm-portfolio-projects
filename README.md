# LLM Portfolio Projects

Two AI-powered applications using Ollama for local, offline AI processing.

## 🎯 Projects Included

### 1. AI Code Assistant
Generate, optimize, explain, test, and debug code using AI.

**Features:**
- Generate code from natural language descriptions
- Optimize code for performance and readability
- Explain complex code with clear breakdowns
- Generate comprehensive unit tests
- Debug code and identify issues
- Perform professional code reviews

**Supported Languages:** Python, JavaScript, Java, Go, C++, and more

### 2. Document Analyzer
Analyze, summarize, and extract insights from documents.

**Features:**
- Summarize documents (brief, detailed, executive formats)
- Extract key information and entities
- Answer questions about document content
- Identify main topics and themes
- Generate structured reports
- Compare and analyze multiple documents

## 🎨 Web Interface

You can now use the beautiful web interface!

### Running the Web App

```bash
# Install dependencies
pip install -r requirements.txt
pip install streamlit

# Make sure Ollama is running
ollama serve

# Run the web app (in another terminal)
streamlit run streamlit_app.py
```

Then visit: `http://localhost:8501`

**Features Available in Web App:**
- AI Code Assistant (all 6 features)
- Document Analyzer (all 6 features)
- Beautiful, user-friendly interface
- Real-time processing and results

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Ollama installed (https://ollama.ai)
- Mistral model downloaded

### Installation

```bash
# 1. Create virtual environment
python -m venv venv

# 2. Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
pip install ollama

# 4. Make sure Ollama is running
ollama serve

# 5. Choose how to use:
# Option A: Run web app (another terminal)
streamlit run streamlit_app.py

# Option B: Run examples
python examples.py

# Option C: Use command line
python ai_code_assistant.py
python document_analyzer.py
```

## 💻 Usage Examples

### Using Web Interface (Recommended)

1. Run: `streamlit run streamlit_app.py`
2. Browser opens automatically
3. Select application from sidebar
4. Choose task and fill in details
5. Click button and see results!

### Using Command Line

#### Code Assistant Example
```python
from ai_code_assistant_ollama import AICodeAssistant

assistant = AICodeAssistant()

# Generate code
result = assistant.generate_code(
    description="Write a function to check if a number is prime",
    language="python"
)
print(result["sections"]["CODE"])

# Optimize code
result = assistant.optimize_code(your_code)
print(result["sections"]["OPTIMIZED_CODE"])

# Explain code
result = assistant.explain_code(complex_code)
print(result["sections"]["EXPLANATION"])

# Generate tests
result = assistant.generate_tests(code)
print(result["sections"]["TEST_CODE"])

# Debug code
result = assistant.debug_code(buggy_code, error_message)
print(result["sections"]["FIXED_CODE"])

# Code review
result = assistant.code_review(code)
print(result["sections"]["ISSUES"])
```

#### Document Analyzer Example
```python
from document_analyzer_ollama import DocumentAnalyzer

analyzer = DocumentAnalyzer()

# Summarize document
result = analyzer.summarize(document_content)
print(result["content"])

# Answer questions
result = analyzer.answer_question(document_content, "What is the main topic?")
print(result["answer"])

# Extract information
result = analyzer.extract_key_information(document_content)
print(result["extracted_data"])

# Identify topics
result = analyzer.identify_topics(document_content)
print(result["topics"])

# Generate report
result = analyzer.generate_report(document_content)
print(result["content"])

# Compare documents
result = analyzer.compare_documents(doc1, doc2)
print(result["analysis"])
```

## ✨ Features

- **Local Processing** - All AI runs on your computer
- **Offline** - No internet required after initial setup
- **Free** - Completely free, no API costs
- **Fast** - Optimized Mistral model
- **Private** - Your data never leaves your computer
- **Production Ready** - Clean, well-structured code
- **Web Interface** - Beautiful Streamlit UI
- **Multiple Interfaces** - CLI, Web, and Python API

## 🏗️ Architecture

- Uses Ollama for local LLM execution
- Mistral model (4GB) for code and document processing
- Structured prompting for consistent outputs
- Modular design for easy feature addition
- Error handling throughout
- Streamlit for web interface

## 📊 Performance

| Operation | Time | Quality |
|-----------|------|---------|
| Generate Code | 10-15 sec | Excellent |
| Optimize Code | 10-15 sec | Very Good |
| Summarize Document | 10-15 sec | Very Good |
| Answer Question | 10-15 sec | Very Good |

**Note:** First request takes longer (20-30 sec) as the model loads. Subsequent requests are faster (10-15 sec).

## 📁 File Structure

```
llm-portfolio-projects/
├── ai_code_assistant_ollama.py     Code generation system
├── document_analyzer_ollama.py     Document analysis system
├── examples_ollama.py              Usage examples
├── streamlit_app.py                Web interface
├── requirements.txt                Python dependencies
├── README.md                       This file
├── .gitignore                      Git ignore rules
└── .env.example                    Environment template
```

## 🔐 Setup Notes

1. Ollama runs locally on port 11434
2. Streamlit web app runs on http://localhost:8501
3. First run takes longer (loading model)
4. Subsequent runs are faster (model cached)
5. No API key needed for Ollama version
6. All processing happens on your machine

## 🌐 Deployment (Optional)

You can deploy the Streamlit app for free:

### Streamlit Cloud (Easiest)
1. Push code to GitHub
2. Go to https://share.streamlit.io
3. Connect your GitHub repository
4. Select `streamlit_app.py`
5. Deploy!
6. Get a public URL to share

### Other Options
- Heroku (free tier may have changed)
- Railway (free tier available)
- AWS (various free options)

## 📞 Support

For issues:
1. Check Ollama is running: `ollama serve`
2. Verify model is downloaded: `ollama list`
3. Check dependencies: `pip list`
4. Review error messages carefully
5. Check that Streamlit is installed: `pip install streamlit`

## 📄 License

MIT License - Feel free to use this for personal or commercial projects

## 👨‍💻 Author

Your Name
your.email@example.com

## 🙏 Acknowledgments

- Ollama team for local LLM execution
- Mistral team for excellent open-source model
- Anthropic for Claude API reference
- Streamlit team for amazing web framework

---

**Last Updated:** 2024
**Version:** 2.0.0 (Added Streamlit web interface)
