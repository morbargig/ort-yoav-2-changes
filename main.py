#!/usr/bin/env python3
"""
Calculator Demo Script

This script demonstrates how to use the Calculator class.
Students can run this script to test their implementations interactively.

Usage: python main.py
"""

from calculator import Calculator


def demo_calculator():
    """Demonstrate calculator functionality with example calculations."""
    print("🧮 Welcome to the Python Calculator Demo!")
    print("=" * 50)
    
    # Create calculator instance
    calc = Calculator()
    
    print("\n📝 Running example calculations...")
    print("-" * 30)
    
    try:
        # Basic arithmetic operations
        print(f"Addition: 10 + 5 = {calc.add(10, 5)}")
        print(f"Subtraction: 10 - 3 = {calc.subtract(10, 3)}")
        print(f"Multiplication: 4 * 6 = {calc.multiply(4, 6)}")
        print(f"Division: 15 / 3 = {calc.divide(15, 3)}")
        
        # Advanced operations
        print(f"Power: 2^4 = {calc.power(2, 4)}")
        print(f"Square root: √25 = {calc.square_root(25)}")
        print(f"Factorial: 5! = {calc.factorial(5)}")
        print(f"Percentage: 25% of 200 = {calc.percentage(200, 25)}")
        
        # Show calculation history
        print("\n📋 Calculation History:")
        print("-" * 20)
        history = calc.get_history()
        if history:
            for i, calculation in enumerate(history, 1):
                print(f"{i}. {calculation}")
        else:
            print("No calculations in history (methods not implemented yet)")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        print("💡 This probably means some methods are not implemented yet.")
        print("   Check calculator.py and implement the missing methods!")


def interactive_calculator():
    """Run an interactive calculator session."""
    print("\n🎮 Interactive Calculator Mode")
    print("=" * 30)
    print("Available operations:")
    print("1. Addition (a + b)")
    print("2. Subtraction (a - b)")
    print("3. Multiplication (a * b)")
    print("4. Division (a / b)")
    print("5. Power (a ^ b)")
    print("6. Square root (√a)")
    print("7. Factorial (a!)")
    print("8. Percentage (b% of a)")
    print("9. Show history")
    print("0. Exit")
    
    calc = Calculator()
    
    while True:
        try:
            choice = input("\nEnter your choice (0-9): ").strip()
            
            if choice == "0":
                print("👋 Goodbye!")
                break
            elif choice == "1":
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                result = calc.add(a, b)
                print(f"Result: {a} + {b} = {result}")
            elif choice == "2":
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                result = calc.subtract(a, b)
                print(f"Result: {a} - {b} = {result}")
            elif choice == "3":
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                result = calc.multiply(a, b)
                print(f"Result: {a} * {b} = {result}")
            elif choice == "4":
                a = float(input("Enter dividend: "))
                b = float(input("Enter divisor: "))
                result = calc.divide(a, b)
                print(f"Result: {a} / {b} = {result}")
            elif choice == "5":
                a = float(input("Enter base: "))
                b = float(input("Enter exponent: "))
                result = calc.power(a, b)
                print(f"Result: {a} ^ {b} = {result}")
            elif choice == "6":
                a = float(input("Enter number: "))
                result = calc.square_root(a)
                print(f"Result: √{a} = {result}")
            elif choice == "7":
                a = int(input("Enter non-negative integer: "))
                result = calc.factorial(a)
                print(f"Result: {a}! = {result}")
            elif choice == "8":
                a = float(input("Enter total value: "))
                b = float(input("Enter percentage: "))
                result = calc.percentage(a, b)
                print(f"Result: {b}% of {a} = {result}")
            elif choice == "9":
                history = calc.get_history()
                if history:
                    print("\n📋 Calculation History:")
                    for i, calculation in enumerate(history, 1):
                        print(f"{i}. {calculation}")
                else:
                    print("No calculations in history yet.")
            else:
                print("❌ Invalid choice. Please enter a number from 0-9.")
                
        except ValueError as e:
            print(f"❌ Error: {e}")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            print("💡 This might mean the method is not implemented yet!")


def main():
    """Main function to run the calculator demo."""
    print("🐍 Python Calculator Practice Project")
    print("=" * 50)
    print("This project helps students practice Python programming")
    print("by implementing calculator methods in calculator.py")
    print()
    
    # Run demonstration
    demo_calculator()
    
    # Ask if user wants interactive mode
    print("\n" + "=" * 50)
    choice = input("Would you like to try interactive mode? (y/n): ").lower().strip()
    
    if choice in ['y', 'yes']:
        interactive_calculator()
    else:
        print("\n💡 Tips for students:")
        print("- Implement methods in calculator.py")
        print("- Run tests with: python -m pytest test_calculator.py")
        print("- Run this demo again with: python main.py")
        print("- Check the README.md for detailed instructions")


if __name__ == "__main__":
    main() 