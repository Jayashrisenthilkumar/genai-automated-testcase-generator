from ast_parser import extract_functions
from test_generator import generate_tests

with open("../sample_code/calculator.py") as f:
    code = f.read()

functions = extract_functions(code)
tests = generate_tests(functions)

with open("../generated_tests/test_calculator.py", "w") as f:
    f.write(tests)

print("✅ Test cases generated successfully")
