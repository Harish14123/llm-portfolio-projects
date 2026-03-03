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

# 5. Run examples (in another terminal)
python examples.py
```

### Running the Projects

**Run all examples:**
```bash
python examples.py
```

**Run Code Assistant only:**
```bash
python ai_code_assistant.py
```

**Run Document Analyzer only:**
```bash
python document_analyzer.py
```

## 💻 Usage Examples

### Code Assistant Example
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
```

### Document Analyzer Example
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
```

## ✨ Features

- **Local Processing** - All AI runs on your computer
- **Offline** - No internet required after initial setup
- **Free** - Completely free, no API costs
- **Fast** - Optimized Mistral model
- **Private** - Your data never leaves your computer
- **Production Ready** - Clean, well-structured code

## 🏗️ Architecture

- Uses Ollama for local LLM execution
- Mistral model (4GB) for code and document processing
- Structured prompting for consistent outputs
- Modular design for easy feature addition
- Error handling throughout

## 📊 Performance

| Operation | Time | Quality |
|-----------|------|---------|
| Generate Code | 10-15 sec | Excellent |
| Optimize Code | 10-15 sec | Very Good |
| Summarize Document | 10-15 sec | Very Good |
| Answer Question | 10-15 sec | Very Good |

## 📝 File Structure

```
llm-portfolio-projects/
├── ai_code_assistant_ollama.py     Code generation system
├── document_analyzer_ollama.py     Document analysis system
├── examples_ollama.py              Usage examples
├── requirements.txt                Python dependencies
├── README.md                       This file
├── .gitignore                      Git ignore rules
└── .env.example                    Environment template
```

## 🔐 Setup Notes

1. Ollama runs locally on port 11434
2. First run takes longer (loading model)
3. Subsequent runs are faster (model cached)
4. No API key needed for Ollama version
5. All processing happens on your machine

## 📞 Support

For issues:
1. Check Ollama is running: `ollama serve`
2. Verify model is downloaded: `ollama list`
3. Check dependencies: `pip list`
4. Review error messages carefully

## 📄 License

MIT License - Feel free to use this for personal or commercial projects

## 👨‍💻 Author

Harish
harishbandarupalli56@gmail.com

---

**Last Updated:** 2026
**Version:** 1.0.0
