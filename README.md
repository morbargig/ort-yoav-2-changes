עבודה בינונית

tudents implement calculator methods in `calculator.py` and test them via a web interface.

## 🚀 Setup

1. **Open in VS Code**
2. **Reopen in Container** (VS Code will prompt you)
3. **Run the calculator**:
   ```bash
   python app.py
   ```
4. **Open browser**: `http://localhost:5001`

## 🧪 Test Your Code

```bash
python main.py    # CLI version
pytest           # Run tests
```

## 📝 Student Task

Implement these methods in `calculator.py`:

```python
def add(self, a, b):
    # TODO: Implement addition
    result = a + b
    self.history.append(f"{a} + {b} = {result}")
    return result

def subtract(self, a, b):
    # TODO: Implement subtraction
    result = a - b
    self.history.append(f"{a} - {b} = {result}")
    return result

def multiply(self, a, b):
    # TODO: Implement multiplication
    result = a * b
    self.history.append(f"{a} × {b} = {result}")
    return result

def divide(self, a, b):
    # TODO: Implement division
    if b == 0:
        raise ValueError("Cannot divide by zero")
    result = a / b
    self.history.append(f"{a} ÷ {b} = {result}")
    return result
```

## 🎮 How It Works

1. **Unimplemented**: Calculator shows "method not implemented yet!"
2. **Implement**: Add code to calculator methods
3. **Test**: Use web calculator to see results
4. **History**: View calculation history

## 📝 What to Do

1. **Implement methods** in `calculator.py` (replace `pass` with real code)
2. **Test your work** by running the web app or CLI
3. **Check tests** with `pytest`

## 📁 Files

- `calculator.py` - **Implement methods here** 
- `app.py` - Web server (already done)
- `main.py` - CLI version (already done)
- `test_calculator.py` - Tests (already done)

## ✅ Done!

When all methods work, the calculator will be complete! 🎉
