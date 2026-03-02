import ollama
from typing import Optional


class AICodeAssistant:
    
    def __init__(self, model: str = "mistral"):
        self.model = model
        self.client = ollama.Client()
        self.conversation_history = []
    
    def generate_code(
        self,
        description: str,
        language: str = "python",
        requirements: Optional[str] = None
    ) -> dict:
        prompt = f"""You are an expert programmer. Generate high-quality {language} code.

Task: {description}

{f"Requirements: {requirements}" if requirements else ""}

Requirements for your response:
1. Write clean, production-ready code
2. Include proper error handling
3. Add meaningful comments
4. Follow {language} best practices
5. Include type hints (if applicable)

Format your response as:
CODE:
[Your code here]

EXPLANATION:
[Explain what the code does and why]

BEST_PRACTICES:
[List 3-4 best practices used]"""

        response = self.client.generate(
            model=self.model,
            prompt=prompt,
            stream=False
        )
        
        content = response['response']
        return self._parse_response(content, "generate")
    
    def optimize_code(self, code: str, language: str = "python") -> dict:
        prompt = f"""You are a {language} optimization expert. Analyze and optimize this code:

```{language}
{code}
```

Provide:
1. Optimized version of the code
2. Specific improvements made
3. Performance impact
4. Readability improvements

Format your response as:
OPTIMIZED_CODE:
[Optimized code]

IMPROVEMENTS:
[List of improvements]

PERFORMANCE_IMPACT:
[How much faster/better]"""

        response = self.client.generate(
            model=self.model,
            prompt=prompt,
            stream=False
        )
        
        content = response['response']
        return self._parse_response(content, "optimize")
    
    def explain_code(self, code: str, language: str = "python") -> dict:
        prompt = f"""Explain this {language} code clearly:

```{language}
{code}
```

Provide:
1. High-level overview of what it does
2. Step-by-step breakdown
3. Time complexity
4. Space complexity
5. Potential issues or edge cases

Format your response as:
OVERVIEW:
[High-level explanation]

STEP_BY_STEP:
[Detailed breakdown]

COMPLEXITY:
Time: O(...)
Space: O(...)

POTENTIAL_ISSUES:
[List any issues]"""

        response = self.client.generate(
            model=self.model,
            prompt=prompt,
            stream=False
        )
        
        content = response['response']
        return self._parse_response(content, "explain")
    
    def generate_tests(
        self,
        code: str,
        language: str = "python",
        framework: str = "pytest"
    ) -> dict:
        prompt = f"""Generate comprehensive unit tests for this {language} code using {framework}:

```{language}
{code}
```

Provide:
1. Complete test file with multiple test cases
2. Cover normal cases, edge cases, and error cases
3. Include setup and teardown if needed
4. Add docstrings to each test

Format your response as:
TEST_CODE:
[Complete test file]

TEST_CASES:
[List of test cases covered]

COVERAGE:
[What scenarios are covered]"""

        response = self.client.generate(
            model=self.model,
            prompt=prompt,
            stream=False
        )
        
        content = response['response']
        return self._parse_response(content, "tests")
    
    def debug_code(self, code: str, error: str, language: str = "python") -> dict:
        prompt = f"""Debug this {language} code:

```{language}
{code}
```

Error: {error}

Provide:
1. Root cause analysis
2. Fixed version of the code
3. Explanation of what was wrong
4. How to prevent this bug

Format your response as:
ROOT_CAUSE:
[What caused the bug]

FIXED_CODE:
[Corrected code]

EXPLANATION:
[Why this fixes it]

PREVENTION:
[How to avoid this]"""

        response = self.client.generate(
            model=self.model,
            prompt=prompt,
            stream=False
        )
        
        content = response['response']
        return self._parse_response(content, "debug")
    
    def code_review(self, code: str, language: str = "python") -> dict:
        prompt = f"""Perform a professional code review of this {language} code:

```{language}
{code}
```

Evaluate:
1. Code quality (readability, maintainability)
2. Performance concerns
3. Security issues
4. Best practices violations
5. Documentation
6. Error handling

Format your response as:
OVERALL_RATING:
[Excellent/Good/Fair/Poor]

STRENGTHS:
[What's done well]

ISSUES:
[Issues found with severity]

SUGGESTIONS:
[Actionable improvements]

REFACTORED_CODE:
[Improved version if major changes needed]"""

        response = self.client.generate(
            model=self.model,
            prompt=prompt,
            stream=False
        )
        
        content = response['response']
        return self._parse_response(content, "review")
    
    def _parse_response(self, content: str, response_type: str) -> dict:
        sections = {}
        current_section = None
        current_content = []
        
        for line in content.split('\n'):
            if line.isupper() and ':' in line:
                if current_section:
                    sections[current_section] = '\n'.join(current_content).strip()
                current_section = line.replace(':', '').strip()
                current_content = []
            else:
                current_content.append(line)
        
        if current_section:
            sections[current_section] = '\n'.join(current_content).strip()
        
        return {
            "type": response_type,
            "sections": sections,
            "raw": content
        }


def main():
    print("="*70)
    print("AI CODE ASSISTANT - OLLAMA VERSION")
    print("="*70)
    
    assistant = AICodeAssistant()
    
    print("\nExample 1: Generate Code\n")
    print("Generating code for: Write a function that checks if a number is prime")
    result = assistant.generate_code(
        description="Write a function that checks if a number is prime",
        language="python"
    )
    print("Generated Code:")
    print(result["sections"].get("CODE", "N/A"))
    print("\nExplanation:")
    print(result["sections"].get("EXPLANATION", "N/A"))
    
    print("\n" + "="*70)
    print("Example 2: Optimize Code\n")
    sample_code = """
def find_duplicates(numbers):
    duplicates = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j and numbers[i] == numbers[j]:
                if numbers[i] not in duplicates:
                    duplicates.append(numbers[i])
    return duplicates
    """
    print("Optimizing inefficient code...")
    result = assistant.optimize_code(sample_code)
    print("Optimized Code:")
    print(result["sections"].get("OPTIMIZED_CODE", "N/A"))
    
    print("\n" + "="*70)
    print("Example 3: Explain Code\n")
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
    print("Explaining quicksort implementation...")
    result = assistant.explain_code(complex_code)
    print("Explanation:")
    print(result["sections"].get("OVERVIEW", "N/A"))
    
    print("\n" + "="*70)
    print("✓ Examples completed!")
    print("="*70)


if __name__ == "__main__":
    main()
