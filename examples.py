from ai_code_assistant_ollama import AICodeAssistant
from document_analyzer_ollama import DocumentAnalyzer


def example_code_assistant():
    print("\n" + "="*70)
    print("AI CODE ASSISTANT EXAMPLES")
    print("="*70)
    
    assistant = AICodeAssistant()
    
    print("\n1. GENERATE SORTING ALGORITHM\n")
    print("Task: Generate a function that finds the longest palindrome substring...")
    result = assistant.generate_code(
        description="Implement merge sort algorithm with proper sorting",
        language="python",
        requirements="Should handle edge cases and be well-documented"
    )
    print("Generated Code:")
    print(result["sections"].get("CODE", "N/A"))
    
    print("\n" + "-"*70)
    print("\n2. OPTIMIZE CODE\n")
    print("Original Code (inefficient):")
    inefficient_code = """
def find_duplicates(numbers):
    duplicates = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j and numbers[i] == numbers[j]:
                if numbers[i] not in duplicates:
                    duplicates.append(numbers[i])
    return duplicates
    """
    print(inefficient_code)
    
    result = assistant.optimize_code(inefficient_code)
    print("\nOptimized Code:")
    print(result["sections"].get("OPTIMIZED_CODE", "N/A"))
    print("\nImprovements:")
    print(result["sections"].get("IMPROVEMENTS", "N/A"))
    
    print("\n" + "-"*70)
    print("\n3. EXPLAIN CODE\n")
    complex_code = """
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
    """
    
    result = assistant.explain_code(complex_code)
    print("Code Explanation:")
    print(result["sections"].get("OVERVIEW", "N/A"))
    
    print("\n" + "-"*70)
    print("\n4. GENERATE TESTS\n")
    test_code = """
def calculate_area(radius):
    import math
    if radius <= 0:
        raise ValueError("Radius must be positive")
    return math.pi * radius ** 2
    """
    
    result = assistant.generate_tests(test_code, framework="pytest")
    print("Generated Tests:")
    print(result["sections"].get("TEST_CODE", "N/A"))
    
    print("\n" + "-"*70)
    print("\n5. DEBUG CODE\n")
    buggy_code = """
def find_max(numbers):
    max_val = None
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val
    """
    
    error_msg = "TypeError: '>' not supported between instances of 'int' and 'NoneType'"
    
    result = assistant.debug_code(buggy_code, error_msg)
    print("Fixed Code:")
    print(result["sections"].get("FIXED_CODE", "N/A"))
    print("\nExplanation:")
    print(result["sections"].get("EXPLANATION", "N/A"))


def example_document_analyzer():
    print("\n" + "="*70)
    print("DOCUMENT ANALYZER EXAMPLES")
    print("="*70)
    
    analyzer = DocumentAnalyzer()
    
    sample_doc = """
    THE FUTURE OF RENEWABLE ENERGY
    
    Executive Summary:
    Renewable energy sources are becoming increasingly important in the global 
    transition away from fossil fuels. Solar, wind, and hydroelectric power are 
    growing at unprecedented rates. By 2030, renewables are expected to account 
    for 40% of global electricity generation.
    
    Current Status:
    As of 2024, renewable energy accounts for 30% of global electricity generation.
    Solar power capacity has increased by 45% in the last 3 years. Wind power 
    represents 25% of Europe's electricity supply. Battery storage technology 
    is rapidly improving, with costs dropping 70% in the past 5 years.
    
    Key Technologies:
    
    1. Solar Photovoltaics (PV)
    Solar panels convert sunlight directly into electricity. Modern panels achieve 
    22-24% efficiency. Distributed solar installations are growing in both 
    residential and commercial sectors.
    
    2. Wind Power
    Both onshore and offshore wind turbines generate substantial electricity. 
    Offshore wind is particularly promising, with capacity factors exceeding 40%.
    
    3. Battery Storage
    Lithium-ion batteries are the dominant technology. Energy density continues 
    to improve while costs decrease. Grid-scale battery storage enables renewable 
    integration and load balancing.
    
    Challenges:
    - Intermittency issues requiring energy storage solutions
    - Grid integration complexity
    - High initial capital costs
    - Land use considerations
    - Supply chain vulnerabilities for critical materials
    
    Opportunities:
    - Job creation in renewable energy sector
    - Decreased electricity costs over time
    - Reduced carbon emissions
    - Energy independence for nations
    - Technological innovation and export opportunities
    
    Projections for 2030:
    - Renewable energy to reach 40% of global electricity
    - Solar capacity to exceed 2 TW (terawatts)
    - Battery storage costs to drop another 50%
    - Electric vehicles to represent 50% of new car sales
    - Energy-related CO2 emissions to peak and begin declining
    
    Conclusion:
    The transition to renewable energy is accelerating. With continued investment, 
    technological advancement, and supportive policies, renewables will become 
    the dominant energy source by 2040.
    """
    
    print("\n1. BRIEF SUMMARY\n")
    result = analyzer.summarize(sample_doc, summary_type="brief")
    print("Summary:")
    print(result["content"])
    
    print("\n" + "-"*70)
    print("\n2. EXECUTIVE SUMMARY\n")
    result = analyzer.summarize(sample_doc, summary_type="executive")
    print("Executive Summary:")
    print(result["content"])
    
    print("\n" + "-"*70)
    print("\n3. EXTRACT KEY INFORMATION\n")
    result = analyzer.extract_key_information(sample_doc)
    print("Extracted Data:")
    import json
    print(json.dumps(result["extracted_data"], indent=2))
    
    print("\n" + "-"*70)
    print("\n4. QUESTION ANSWERING\n")
    
    questions = [
        "What is the expected percentage of renewable energy by 2030?",
        "What are the main challenges in renewable energy adoption?",
        "Which renewable technology is most important?"
    ]
    
    for question in questions:
        result = analyzer.answer_question(sample_doc, question)
        print(f"Q: {result['question']}")
        print(f"A: {result['answer']}")
        print(f"Confidence: {result['confidence']}\n")
    
    print("-"*70)
    print("\n5. TOPIC IDENTIFICATION\n")
    result = analyzer.identify_topics(sample_doc)
    print("Topics and Themes:")
    print(result["raw"])
    
    print("\n" + "-"*70)
    print("\n6. GENERATE EXECUTIVE REPORT\n")
    result = analyzer.generate_report(sample_doc, report_type="executive")
    print("Report:")
    print(result["content"])
    print(f"\nWord Count: {result['word_count']}")


def example_document_comparison():
    print("\n" + "="*70)
    print("DOCUMENT COMPARISON EXAMPLE")
    print("="*70)
    
    analyzer = DocumentAnalyzer()
    
    doc1 = """
    TRADITIONAL ENERGY
    Coal, natural gas, and nuclear energy have powered civilization 
    for decades. These reliable sources provide baseload power but 
    generate significant carbon emissions. Nuclear offers high capacity 
    factors but faces public acceptance challenges.
    """
    
    doc2 = """
    RENEWABLE ENERGY
    Solar and wind power are rapidly growing alternatives that produce 
    zero emissions. They offer decentralized generation and technological 
    scalability. However, intermittency remains a challenge requiring 
    advanced storage solutions.
    """
    
    print("\nDocument 1: Traditional Energy\n")
    print(doc1)
    
    print("\nDocument 2: Renewable Energy\n")
    print(doc2)
    
    print("\nComparison Analysis:\n")
    result = analyzer.compare_documents(
        doc1, 
        doc2, 
        doc_names=("Traditional Energy", "Renewable Energy")
    )
    
    for section, content in result["analysis"].items():
        print(f"{section}:")
        print(content)
        print()


if __name__ == "__main__":
    print("\n" + "="*70)
    print("LLM PORTFOLIO PROJECTS - USAGE EXAMPLES")
    print("="*70)
    
    try:
        example_code_assistant()
    except Exception as e:
        print(f"Code Assistant Example Error: {e}")
    
    try:
        example_document_analyzer()
    except Exception as e:
        print(f"Document Analyzer Example Error: {e}")
    
    try:
        example_document_comparison()
    except Exception as e:
        print(f"Document Comparison Example Error: {e}")
    
    print("\n" + "="*70)
    print("Examples completed!")
    print("="*70)
