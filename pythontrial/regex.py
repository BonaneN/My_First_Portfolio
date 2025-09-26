import re

# Regex patterns for each category
patterns = {
    "Emails": r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$",
    "Phones": r"^(?:\(\d{3}\)\s?|\d{3}[-.])\d{3}[-.]\d{4}$",
    "Credit_cards": r"^(?:\d{4}[- ]?){3}\d{4}$",
    "Time": r"^(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?$",
    "Currency": r"^\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?$"
}

def read_test_cases(filename):
    test_cases = {category: [] for category in patterns.keys()}
    current_category = None
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                
                # Check if line is a category header
                if line.endswith(':'):
                    current_category = line[:-1]  # Remove the colon
                elif current_category and current_category in test_cases:
                    test_cases[current_category].append(line)
                    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    
    return test_cases

def test_patterns(patterns, test_cases):
    for category, pattern in patterns.items():
        print(f"\n{category.upper()} TESTING")
        print("-" * 40)
        
        for test_case in test_cases[category]:
            match = re.match(pattern, test_case)
            status = "✓ MATCH" if match else "✗ NO MATCH"
            print(f"{status}: {test_case}")

if __name__ == "__main__":
    test_cases = read_test_cases("test_cases.txt")
    if test_cases:
        test_patterns(patterns, test_cases)