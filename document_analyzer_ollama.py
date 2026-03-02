import ollama
import json
import re
from typing import Optional, List


class DocumentAnalyzer:
    
    def __init__(self, model: str = "mistral", chunk_size: int = 8000):
        self.model = model
        self.client = ollama.Client()
        self.chunk_size = chunk_size
        self.document_cache = {}
    
    def load_document(self, file_path: str) -> str:
        try:
            if file_path.endswith('.txt'):
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
            else:
                raise ValueError("Unsupported file format")
            
            self.document_cache[file_path] = content
            return content
        except FileNotFoundError:
            raise FileNotFoundError(f"Document not found: {file_path}")
    
    def _chunk_document(self, content: str) -> List[str]:
        words = content.split()
        chunks = []
        current_chunk = []
        current_length = 0
        
        for word in words:
            current_chunk.append(word)
            current_length += len(word) + 1
            
            if current_length > self.chunk_size:
                chunks.append(' '.join(current_chunk))
                current_chunk = []
                current_length = 0
        
        if current_chunk:
            chunks.append(' '.join(current_chunk))
        
        return chunks
    
    def summarize(
        self,
        content: str,
        summary_type: str = "brief",
        max_length: Optional[int] = None
    ) -> dict:
        if summary_type == "brief":
            length_instruction = "in 1-2 concise sentences"
            format_instruction = ""
        elif summary_type == "detailed":
            length_instruction = "in 3-4 paragraphs"
            format_instruction = "\nOrganize by key sections."
        elif summary_type == "executive":
            length_instruction = "in structured format"
            format_instruction = """
Format as:
OBJECTIVE: [What is this about]
KEY_POINTS: [3-5 main points]
KEY_NUMBERS: [Important statistics/figures]
RECOMMENDATIONS: [If applicable]
NEXT_STEPS: [Action items]"""
        else:
            length_instruction = "in 2-3 paragraphs"
            format_instruction = ""
        
        chunks = self._chunk_document(content)
        
        if len(chunks) > 1:
            chunk_summaries = []
            for chunk in chunks:
                summary = self._summarize_chunk(chunk, "brief")
                chunk_summaries.append(summary)
            
            combined = "\n\n".join(chunk_summaries)
            prompt = f"""Synthesize these chunk summaries into a comprehensive summary {length_instruction}:{format_instruction}

Chunk Summaries:
{combined}"""
        else:
            prompt = f"""Summarize the following document {length_instruction}:{format_instruction}

Document:
{content}"""
        
        response = self.client.generate(
            model=self.model,
            prompt=prompt,
            stream=False
        )
        
        summary = response['response']
        
        return {
            "type": "summary",
            "summary_type": summary_type,
            "content": summary,
            "word_count": len(summary.split()),
            "chunk_count": len(chunks)
        }
    
    def _summarize_chunk(self, chunk: str, summary_type: str = "brief") -> str:
        prompt = f"Summarize this text in 2-3 sentences:\n\n{chunk}"
        response = self.client.generate(
            model=self.model,
            prompt=prompt,
            stream=False
        )
        return response['response']
    
    def extract_key_information(self, content: str) -> dict:
        prompt = f"""Analyze this document and extract key information in JSON format:

Document:
{content}

Extract:
1. Main topic/title
2. Key entities (people, organizations, places)
3. Important dates
4. Key statistics or numbers
5. Main conclusions
6. Important quotes (up to 3)
7. Document type/category
8. Sentiment/tone

Provide response as valid JSON with these fields:
{{
  "topic": "...",
  "entities": {{"people": [], "organizations": [], "places": []}},
  "dates": [],
  "statistics": [],
  "conclusions": [],
  "quotes": [],
  "document_type": "...",
  "tone": "..."
}}"""

        response = self.client.generate(
            model=self.model,
            prompt=prompt,
            stream=False
        )
        
        content_text = response['response']
        
        try:
            json_match = re.search(r'\{.*\}', content_text, re.DOTALL)
            if json_match:
                extracted = json.loads(json_match.group())
            else:
                extracted = {"raw": content_text}
        except json.JSONDecodeError:
            extracted = {"raw": content_text}
        
        return {
            "type": "extraction",
            "extracted_data": extracted,
            "raw_response": content_text
        }
    
    def answer_question(self, content: str, question: str) -> dict:
        chunks = self._chunk_document(content)
        
        if len(chunks) > 1:
            relevant_chunks = self._find_relevant_chunks(chunks, question)
            context = "\n\n".join(relevant_chunks)
        else:
            context = content
        
        prompt = f"""Based on the following document, answer this question:

Question: {question}

Document:
{context}

Provide:
1. Direct answer
2. Supporting evidence from the document
3. Confidence level (high/medium/low)

Format as:
ANSWER: [Your answer]
EVIDENCE: [Quote or reference from document]
CONFIDENCE: [high/medium/low]
REASONING: [Why this answer]"""

        response = self.client.generate(
            model=self.model,
            prompt=prompt,
            stream=False
        )
        
        content_text = response['response']
        parsed = self._parse_structured_response(content_text)
        
        return {
            "type": "qa",
            "question": question,
            "answer": parsed.get("ANSWER", "N/A"),
            "evidence": parsed.get("EVIDENCE", "N/A"),
            "confidence": parsed.get("CONFIDENCE", "unknown"),
            "reasoning": parsed.get("REASONING", "N/A"),
            "raw": content_text
        }
    
    def _find_relevant_chunks(self, chunks: List[str], question: str) -> List[str]:
        question_words = set(question.lower().split())
        
        chunk_scores = []
        for chunk in chunks:
            chunk_words = set(chunk.lower().split())
            overlap = len(question_words & chunk_words)
            chunk_scores.append((overlap, chunk))
        
        chunk_scores.sort(reverse=True)
        return [chunk for _, chunk in chunk_scores[:3] if chunk]
    
    def identify_topics(self, content: str) -> dict:
        prompt = f"""Analyze this document and identify all major topics and themes:

Document:
{content}

Provide:
1. Main topics (with brief descriptions)
2. Secondary topics
3. Key themes
4. Topic relationships
5. Content categorization

Format as:
MAIN_TOPICS:
[List with descriptions]

SECONDARY_TOPICS:
[List]

KEY_THEMES:
[List]

RELATIONSHIPS:
[How topics relate to each other]

CATEGORY:
[Overall document category]"""

        response = self.client.generate(
            model=self.model,
            prompt=prompt,
            stream=False
        )
        
        content_text = response['response']
        parsed = self._parse_structured_response(content_text)
        
        return {
            "type": "topic_analysis",
            "topics": parsed,
            "raw": content_text
        }
    
    def compare_documents(self, content1: str, content2: str, doc_names: tuple = ("Doc1", "Doc2")) -> dict:
        prompt = f"""Compare these two documents:

{doc_names[0]}:
{content1}

{doc_names[1]}:
{content2}

Provide:
1. Similarities (content, tone, structure)
2. Differences (main disparities)
3. Overlapping topics
4. Unique to each document
5. Quality/depth comparison

Format as:
SIMILARITIES:
[List]

DIFFERENCES:
[List]

OVERLAPPING:
[List]

UNIQUE_TO_{doc_names[0].upper()}:
[List]

UNIQUE_TO_{doc_names[1].upper()}:
[List]

COMPARISON:
[Which is more detailed, better written, etc.]"""

        response = self.client.generate(
            model=self.model,
            prompt=prompt,
            stream=False
        )
        
        content_text = response['response']
        parsed = self._parse_structured_response(content_text)
        
        return {
            "type": "comparison",
            "document_pair": doc_names,
            "analysis": parsed,
            "raw": content_text
        }
    
    def generate_report(self, content: str, report_type: str = "comprehensive") -> dict:
        if report_type == "executive":
            structure = """
1. EXECUTIVE SUMMARY (2-3 sentences)
2. KEY FINDINGS (3-5 bullet points)
3. CRITICAL METRICS (if applicable)
4. RECOMMENDATIONS (2-3 action items)
5. NEXT STEPS"""
        elif report_type == "technical":
            structure = """
1. OVERVIEW
2. TECHNICAL DETAILS
3. METHODOLOGY (if applicable)
4. RESULTS/FINDINGS
5. ANALYSIS
6. LIMITATIONS
7. CONCLUSIONS
8. REFERENCES"""
        else:
            structure = """
1. DOCUMENT OVERVIEW
2. KEY INFORMATION
3. MAIN TOPICS
4. DETAILED ANALYSIS
5. IMPORTANT FINDINGS
6. IMPLICATIONS
7. RELATED TOPICS
8. CONCLUSIONS
9. RECOMMENDATIONS"""
        
        prompt = f"""Generate a {report_type} report for this document:

Document:
{content}

Use this structure:
{structure}

Write in professional language with clear sections."""

        response = self.client.generate(
            model=self.model,
            prompt=prompt,
            stream=False
        )
        
        report = response['response']
        
        return {
            "type": "report",
            "report_type": report_type,
            "content": report,
            "word_count": len(report.split())
        }
    
    def _parse_structured_response(self, content: str) -> dict:
        sections = {}
        current_section = None
        current_content = []
        
        for line in content.split('\n'):
            if ':' in line and line.split(':')[0].isupper():
                if current_section:
                    sections[current_section] = '\n'.join(current_content).strip()
                current_section = line.split(':')[0].strip()
                current_content = []
            else:
                current_content.append(line)
        
        if current_section:
            sections[current_section] = '\n'.join(current_content).strip()
        
        return sections


def main():
    analyzer = DocumentAnalyzer()
    
    sample_doc = """
    Artificial Intelligence and Machine Learning Trends 2024
    
    The artificial intelligence industry has experienced unprecedented growth in 2024. 
    Major technology companies have invested over $100 billion in AI development. 
    Key trends include:
    
    1. Large Language Models: ChatGPT, Claude, and Gemini have become mainstream tools.
       These models can now handle complex reasoning and multimodal inputs.
    
    2. Enterprise Adoption: 60% of enterprises have implemented AI solutions in their 
       operations. This represents a 40% increase from 2023.
    
    3. Regulation and Ethics: Governments worldwide are implementing AI regulations.
       The EU AI Act came into effect with strict requirements for high-risk applications.
    
    4. Multimodal AI: Systems that can process text, images, audio, and video simultaneously
       are becoming standard. This enables new applications in content creation and analysis.
    
    5. AI Safety and Alignment: Research into AI safety has become a priority for major labs.
       New techniques for model alignment and interpretability have emerged.
    
    Key Statistics:
    - AI job market grew by 45%
    - Average AI engineer salary: $180,000-$220,000
    - AI startups received $20.1 billion in funding
    - GPU shortages reduced due to increased manufacturing
    
    Outlook for 2025:
    The AI industry is expected to mature further with focus on practical applications
    rather than theoretical research. Integration of AI into existing systems will accelerate.
    Ethics and safety will remain central concerns as the technology impacts society.
    """
    
    print("=" * 70)
    print("INTELLIGENT DOCUMENT ANALYZER")
    print("=" * 70)
    
    print("\n1. SUMMARIZATION\n")
    result = analyzer.summarize(sample_doc, summary_type="executive")
    print(result["content"])
    
    print("\n" + "=" * 70)
    print("2. KEY INFORMATION EXTRACTION\n")
    result = analyzer.extract_key_information(sample_doc)
    print(json.dumps(result["extracted_data"], indent=2))
    
    print("\n" + "=" * 70)
    print("3. QUESTION ANSWERING\n")
    result = analyzer.answer_question(sample_doc, "What is the outlook for AI in 2025?")
    print(f"Question: {result['question']}")
    print(f"Answer: {result['answer']}")
    print(f"Confidence: {result['confidence']}")
    
    print("\n" + "=" * 70)
    print("4. TOPIC ANALYSIS\n")
    result = analyzer.identify_topics(sample_doc)
    print(result["raw"])
    
    print("\n" + "=" * 70)
    print("5. EXECUTIVE REPORT\n")
    result = analyzer.generate_report(sample_doc, report_type="executive")
    print(result["content"])


if __name__ == "__main__":
    main()
