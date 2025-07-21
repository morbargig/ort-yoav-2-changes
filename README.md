# 🐍 Python Calculator Practice Project

A hands-on Python programming exercise designed for students to practice implementing mathematical operations in a class-based structure. This project uses VS Code Dev Containers for a consistent development environment.

## 📚 What You'll Learn

- **Object-Oriented Programming**: Working with classes and methods
- **Error Handling**: Implementing proper exception handling with `try/except` and `raise`
- **Documentation**: Writing and reading docstrings
- **Testing**: Understanding how to write and run unit tests
- **Mathematical Operations**: Implementing various mathematical functions
- **History Tracking**: Managing state within a class

## 🚀 Getting Started

### Prerequisites

- [VS Code](https://code.visualstudio.com/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Dev Containers Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) for VS Code

### Setup Instructions

1. **Clone/Download this project**
   ```bash
   git clone <repository-url>
   # or download and extract the ZIP file
   ```

2. **Open in VS Code**
   - Open VS Code
   - File → Open Folder → Select this project folder

3. **Open in Dev Container**
   - VS Code should prompt you to "Reopen in Container"
   - Or press `Ctrl+Shift+P` (Cmd+Shift+P on Mac) and select "Dev Containers: Reopen in Container"
   - Wait for the container to build (first time may take a few minutes)

4. **You're ready to code!** 🎉

## 📝 Assignment Overview

Your task is to implement all the methods in `calculator.py` that currently contain `pass` statements. Each method has detailed documentation explaining what it should do.

### Methods to Implement

1. **`add(a, b)`** - Add two numbers
2. **`subtract(a, b)`** - Subtract second number from first
3. **`multiply(a, b)`** - Multiply two numbers
4. **`divide(a, b)`** - Divide first number by second (handle division by zero!)
5. **`power(base, exponent)`** - Raise base to the power of exponent
6. **`square_root(number)`** - Calculate square root (handle negative numbers!)
7. **`factorial(n)`** - Calculate factorial (handle negative numbers and non-integers!)
8. **`percentage(value, percent)`** - Calculate percentage of a value

### Special Requirements

- **History Tracking**: Each calculation should be stored in `self.history` as a formatted string
- **Error Handling**: Some methods should raise `ValueError` for invalid inputs
- **Type Checking**: Handle different number types appropriately

## 🧪 Testing Your Code

### Run the Demo
```bash
python main.py
```
This will show you how your calculator works and let you test it interactively.

### Run Unit Tests
```bash
python -m pytest test_calculator.py -v
```
This runs comprehensive tests to verify your implementations.

### Test Individual Methods
```bash
# Test just addition
python -m pytest test_calculator.py::TestCalculator::test_add -v

# Test just division
python -m pytest test_calculator.py::TestCalculator::test_divide -v
```

## 💡 Implementation Tips

### 1. Start Simple
Begin with basic operations like `add`, `subtract`, `multiply`.

### 2. History Tracking
Each method should add a string to `self.history`:
```python
def add(self, a, b):
    result = a + b
    self.history.append(f"{a} + {b} = {result}")
    return result
```

### 3. Error Handling
Use `raise ValueError("message")` for invalid inputs:
```python
def divide(self, a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    # ... rest of implementation
```

### 4. Factorial Implementation
Remember that:
- `0! = 1`
- Only works for non-negative integers
- You can use a loop or recursion

### 5. Square Root
You can use:
- `number ** 0.5`
- Or `import math` and use `math.sqrt(number)`

## 📖 Example Usage

```python
from calculator import Calculator

calc = Calculator()

# Basic operations
result = calc.add(5, 3)        # Returns 8
result = calc.divide(10, 2)    # Returns 5.0
result = calc.power(2, 3)      # Returns 8
result = calc.factorial(5)     # Returns 120

# Check calculation history
history = calc.get_history()
print(history)  # ['5 + 3 = 8', '10 / 2 = 5.0', '2 ^ 3 = 8', '5! = 120']

# Clear history
calc.clear_history()
```

## 🎯 Success Criteria

Your implementation is complete when:

1. ✅ All tests pass: `python -m pytest test_calculator.py`
2. ✅ Demo runs without errors: `python main.py`
3. ✅ Interactive mode works for all operations
4. ✅ History tracking works correctly
5. ✅ Error cases are handled properly

## 📁 Project Structure

```
├── .devcontainer/           # VS Code dev container configuration
│   └── devcontainer.json
├── calculator.py           # 👈 Main file to edit (implement methods here)
├── test_calculator.py      # Unit tests to verify your implementation
├── main.py                # Demo script to test your calculator
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

## 🔧 Troubleshooting

### Container Issues
- Make sure Docker Desktop is running
- Try "Dev Containers: Rebuild Container" if something isn't working

### Import Errors
- Make sure you're running commands from the project root directory
- Check that all files are in the same folder

### Test Failures
- Read the error messages carefully - they tell you what's expected
- Check your method implementations against the docstring requirements
- Make sure you're handling edge cases (negative numbers, zero, etc.)

## 🎓 Learning Objectives

By completing this project, you will have practiced:

- **Class Design**: Understanding how to structure code using classes
- **Method Implementation**: Writing functions that work together
- **Error Handling**: Implementing robust error checking
- **Testing**: Writing and running tests to verify code correctness
- **Documentation**: Reading and following specifications from docstrings
- **Development Environment**: Using modern development tools (VS Code, Docker, Python packages)

## 📞 Need Help?

1. **Read the docstrings** in `calculator.py` - they contain detailed specifications
2. **Check the test file** - `test_calculator.py` shows exactly what each method should do
3. **Run the demo** - `python main.py` to see how things should work
4. **Look at error messages** - they often tell you exactly what's wrong

Good luck, and happy coding! 🚀
