def format_code_snippet(code):
    return f"```python\n{code}\n```"

def format_explanation(explanation):
    return explanation.strip()

def validate_code_snippet(code):
    if not code.strip():
        raise ValueError("Code snippet cannot be empty.")
    return True