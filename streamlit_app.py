import streamlit as st
from ai_code_assistant_ollama import AICodeAssistant
from document_analyzer_ollama import DocumentAnalyzer
import json

st.set_page_config(
    page_title="LLM Portfolio Projects",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 LLM Portfolio Projects")
st.write("AI Code Assistant & Document Analyzer using Ollama")

with st.sidebar:
    st.header("Navigation")
    app_mode = st.radio(
        "Select an application:",
        ["Home", "AI Code Assistant", "Document Analyzer"]
    )

if app_mode == "Home":
    st.header("Welcome to LLM Portfolio Projects")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🔧 AI Code Assistant")
        st.write("""
        Generate, optimize, explain, test, and debug code using AI.
        
        **Features:**
        - Generate code from descriptions
        - Optimize code for performance
        - Explain complex code
        - Generate unit tests
        - Debug code issues
        - Perform code reviews
        """)
    
    with col2:
        st.subheader("📄 Document Analyzer")
        st.write("""
        Analyze, summarize, and extract insights from documents.
        
        **Features:**
        - Summarize documents
        - Extract key information
        - Answer questions
        - Identify topics
        - Generate reports
        - Compare documents
        """)
    
    st.divider()
    st.info("Select an application from the sidebar to get started!")
    
    st.subheader("How It Works")
    st.write("""
    This project uses **Ollama** for local, offline AI processing:
    
    - ✅ No internet required after setup
    - ✅ Completely free (no API costs)
    - ✅ Your data stays on your computer
    - ✅ Uses Mistral AI model
    - ✅ Fast and reliable
    
    **Setup Instructions:**
    1. Install Ollama: https://ollama.ai
    2. Download Mistral model: `ollama pull mistral`
    3. Run: `streamlit run app.py`
    """)

elif app_mode == "AI Code Assistant":
    st.header("🔧 AI Code Assistant")
    
    assistant = AICodeAssistant()
    
    task = st.selectbox(
        "Choose a task:",
        [
            "Generate Code",
            "Optimize Code",
            "Explain Code",
            "Generate Tests",
            "Debug Code",
            "Code Review"
        ]
    )
    
    st.divider()
    
    if task == "Generate Code":
        st.subheader("Generate Code")
        
        description = st.text_area(
            "What code do you want to generate?",
            placeholder="E.g., Write a function to check if a number is prime",
            height=100
        )
        
        language = st.selectbox(
            "Programming Language:",
            ["python", "javascript", "java", "go", "cpp", "rust"]
        )
        
        requirements = st.text_area(
            "Additional requirements (optional):",
            placeholder="E.g., Should handle edge cases, use type hints",
            height=80
        )
        
        if st.button("Generate Code", key="generate"):
            if description:
                with st.spinner("Generating code..."):
                    result = assistant.generate_code(
                        description=description,
                        language=language,
                        requirements=requirements if requirements else None
                    )
                    
                    st.success("Code generated successfully!")
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.subheader("Generated Code")
                        st.code(result["sections"].get("CODE", "N/A"), language=language)
                    
                    with col2:
                        st.subheader("Explanation")
                        st.write(result["sections"].get("EXPLANATION", "N/A"))
                        
                        st.subheader("Best Practices")
                        st.write(result["sections"].get("BEST_PRACTICES", "N/A"))
            else:
                st.error("Please describe the code you want to generate")
    
    elif task == "Optimize Code":
        st.subheader("Optimize Code")
        
        code = st.text_area(
            "Paste your code here:",
            placeholder="def your_function():\n    pass",
            height=200
        )
        
        language = st.selectbox(
            "Programming Language:",
            ["python", "javascript", "java", "go", "cpp"]
        )
        
        if st.button("Optimize Code", key="optimize"):
            if code:
                with st.spinner("Optimizing code..."):
                    result = assistant.optimize_code(code, language)
                    
                    st.success("Code optimized!")
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.subheader("Optimized Code")
                        st.code(result["sections"].get("OPTIMIZED_CODE", "N/A"), language=language)
                    
                    with col2:
                        st.subheader("Improvements")
                        st.write(result["sections"].get("IMPROVEMENTS", "N/A"))
                        
                        st.subheader("Performance Impact")
                        st.write(result["sections"].get("PERFORMANCE_IMPACT", "N/A"))
            else:
                st.error("Please paste some code to optimize")
    
    elif task == "Explain Code":
        st.subheader("Explain Code")
        
        code = st.text_area(
            "Paste your code here:",
            placeholder="def your_function():\n    pass",
            height=200
        )
        
        language = st.selectbox(
            "Programming Language:",
            ["python", "javascript", "java", "go", "cpp"]
        )
        
        if st.button("Explain Code", key="explain"):
            if code:
                with st.spinner("Explaining code..."):
                    result = assistant.explain_code(code, language)
                    
                    st.success("Code explained!")
                    
                    st.subheader("Overview")
                    st.write(result["sections"].get("OVERVIEW", "N/A"))
                    
                    st.subheader("Step by Step")
                    st.write(result["sections"].get("STEP_BY_STEP", "N/A"))
                    
                    st.subheader("Complexity Analysis")
                    st.write(result["sections"].get("COMPLEXITY", "N/A"))
                    
                    st.subheader("Potential Issues")
                    st.write(result["sections"].get("POTENTIAL_ISSUES", "N/A"))
            else:
                st.error("Please paste some code to explain")
    
    elif task == "Generate Tests":
        st.subheader("Generate Tests")
        
        code = st.text_area(
            "Paste your code here:",
            placeholder="def your_function():\n    pass",
            height=200
        )
        
        language = st.selectbox(
            "Programming Language:",
            ["python", "javascript", "java"]
        )
        
        framework = st.selectbox(
            "Testing Framework:",
            ["pytest", "unittest", "jest"]
        )
        
        if st.button("Generate Tests", key="tests"):
            if code:
                with st.spinner("Generating tests..."):
                    result = assistant.generate_tests(code, language, framework)
                    
                    st.success("Tests generated!")
                    
                    st.subheader("Test Code")
                    st.code(result["sections"].get("TEST_CODE", "N/A"), language=language)
                    
                    st.subheader("Test Cases")
                    st.write(result["sections"].get("TEST_CASES", "N/A"))
                    
                    st.subheader("Coverage")
                    st.write(result["sections"].get("COVERAGE", "N/A"))
            else:
                st.error("Please paste some code to test")
    
    elif task == "Debug Code":
        st.subheader("Debug Code")
        
        code = st.text_area(
            "Paste your buggy code:",
            placeholder="def your_function():\n    pass",
            height=150
        )
        
        error = st.text_area(
            "Paste the error message:",
            placeholder="TypeError: ...",
            height=100
        )
        
        language = st.selectbox(
            "Programming Language:",
            ["python", "javascript", "java"]
        )
        
        if st.button("Debug Code", key="debug"):
            if code and error:
                with st.spinner("Debugging code..."):
                    result = assistant.debug_code(code, error, language)
                    
                    st.success("Bug found and fixed!")
                    
                    st.subheader("Root Cause")
                    st.write(result["sections"].get("ROOT_CAUSE", "N/A"))
                    
                    st.subheader("Fixed Code")
                    st.code(result["sections"].get("FIXED_CODE", "N/A"), language=language)
                    
                    st.subheader("Explanation")
                    st.write(result["sections"].get("EXPLANATION", "N/A"))
                    
                    st.subheader("Prevention")
                    st.write(result["sections"].get("PREVENTION", "N/A"))
            else:
                st.error("Please provide both code and error message")
    
    elif task == "Code Review":
        st.subheader("Code Review")
        
        code = st.text_area(
            "Paste your code for review:",
            placeholder="def your_function():\n    pass",
            height=200
        )
        
        language = st.selectbox(
            "Programming Language:",
            ["python", "javascript", "java"]
        )
        
        if st.button("Review Code", key="review"):
            if code:
                with st.spinner("Reviewing code..."):
                    result = assistant.code_review(code, language)
                    
                    st.success("Code review complete!")
                    
                    st.subheader("Overall Rating")
                    st.write(result["sections"].get("OVERALL_RATING", "N/A"))
                    
                    st.subheader("Strengths")
                    st.write(result["sections"].get("STRENGTHS", "N/A"))
                    
                    st.subheader("Issues")
                    st.write(result["sections"].get("ISSUES", "N/A"))
                    
                    st.subheader("Suggestions")
                    st.write(result["sections"].get("SUGGESTIONS", "N/A"))
                    
                    if "REFACTORED_CODE" in result["sections"]:
                        st.subheader("Refactored Code")
                        st.code(result["sections"]["REFACTORED_CODE"], language=language)
            else:
                st.error("Please paste some code to review")

elif app_mode == "Document Analyzer":
    st.header("📄 Document Analyzer")
    
    analyzer = DocumentAnalyzer()
    
    task = st.selectbox(
        "Choose a task:",
        [
            "Summarize Document",
            "Extract Information",
            "Answer Questions",
            "Identify Topics",
            "Generate Report",
            "Compare Documents"
        ]
    )
    
    st.divider()
    
    if task == "Summarize Document":
        st.subheader("Summarize Document")
        
        document = st.text_area(
            "Paste your document here:",
            height=250
        )
        
        summary_type = st.selectbox(
            "Summary Type:",
            ["brief", "detailed", "executive"]
        )
        
        if st.button("Summarize", key="summarize"):
            if document:
                with st.spinner("Summarizing document..."):
                    result = analyzer.summarize(document, summary_type)
                    
                    st.success("Document summarized!")
                    st.subheader("Summary")
                    st.write(result["content"])
                    st.info(f"Word count: {result['word_count']}")
            else:
                st.error("Please paste a document")
    
    elif task == "Extract Information":
        st.subheader("Extract Information")
        
        document = st.text_area(
            "Paste your document here:",
            height=250
        )
        
        if st.button("Extract", key="extract"):
            if document:
                with st.spinner("Extracting information..."):
                    result = analyzer.extract_key_information(document)
                    
                    st.success("Information extracted!")
                    st.json(result["extracted_data"])
            else:
                st.error("Please paste a document")
    
    elif task == "Answer Questions":
        st.subheader("Answer Questions About Document")
        
        document = st.text_area(
            "Paste your document here:",
            height=200
        )
        
        question = st.text_input(
            "Ask a question about the document:",
            placeholder="What is the main topic?"
        )
        
        if st.button("Answer", key="answer"):
            if document and question:
                with st.spinner("Answering question..."):
                    result = analyzer.answer_question(document, question)
                    
                    st.success("Question answered!")
                    
                    st.subheader("Answer")
                    st.write(result["answer"])
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        st.subheader("Evidence")
                        st.write(result["evidence"])
                    
                    with col2:
                        st.subheader("Confidence")
                        st.write(result["confidence"])
                    
                    st.subheader("Reasoning")
                    st.write(result["reasoning"])
            else:
                st.error("Please provide both document and question")
    
    elif task == "Identify Topics":
        st.subheader("Identify Topics & Themes")
        
        document = st.text_area(
            "Paste your document here:",
            height=250
        )
        
        if st.button("Analyze Topics", key="topics"):
            if document:
                with st.spinner("Analyzing topics..."):
                    result = analyzer.identify_topics(document)
                    
                    st.success("Topics identified!")
                    st.write(result["raw"])
            else:
                st.error("Please paste a document")
    
    elif task == "Generate Report":
        st.subheader("Generate Report")
        
        document = st.text_area(
            "Paste your document here:",
            height=250
        )
        
        report_type = st.selectbox(
            "Report Type:",
            ["comprehensive", "executive", "technical"]
        )
        
        if st.button("Generate Report", key="report"):
            if document:
                with st.spinner("Generating report..."):
                    result = analyzer.generate_report(document, report_type)
                    
                    st.success("Report generated!")
                    st.subheader("Report")
                    st.write(result["content"])
                    st.info(f"Word count: {result['word_count']}")
            else:
                st.error("Please paste a document")
    
    elif task == "Compare Documents":
        st.subheader("Compare Documents")
        
        col1, col2 = st.columns(2)
        
        with col1:
            doc1 = st.text_area(
                "Paste first document:",
                height=200,
                key="doc1"
            )
            name1 = st.text_input("Document 1 name:", "Document 1")
        
        with col2:
            doc2 = st.text_area(
                "Paste second document:",
                height=200,
                key="doc2"
            )
            name2 = st.text_input("Document 2 name:", "Document 2")
        
        if st.button("Compare", key="compare"):
            if doc1 and doc2:
                with st.spinner("Comparing documents..."):
                    result = analyzer.compare_documents(
                        doc1, doc2,
                        doc_names=(name1, name2)
                    )
                    
                    st.success("Documents compared!")
                    
                    for section, content in result["analysis"].items():
                        st.subheader(section)
                        st.write(content)
            else:
                st.error("Please paste both documents")

st.divider()
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>Built with ❤️ using Ollama & Streamlit</p>
    <p><a href='https://github.com/Harish14123/llm-portfolio-projects'>View on GitHub</a></p>
</div>
""", unsafe_allow_html=True)
