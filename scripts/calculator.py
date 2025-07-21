import tkinter as tk
from tkinter import ttk
import math

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("מחשבון חוח")
        self.window.geometry("300x450")
        self.window.resizable(False, False)
        self.window.configure(bg='#f0f0f0')
        
        # Variables
        self.current = "0"
        self.previous = ""
        self.operator = ""
        self.should_reset = False
        self.calculation_display = ""  # To show the full calculation
        
        self.create_widgets()
        
    def create_widgets(self):
        # Calculation history display (shows the full calculation)
        self.history_var = tk.StringVar(value="")
        history_display = tk.Entry(
            self.window,
            textvariable=self.history_var,
            font=("Arial", 12),
            justify="right",
            state="readonly",
            bg="white",
            fg="gray",
            bd=0,
            relief="flat"
        )
        history_display.grid(row=0, column=0, columnspan=4, padx=5, pady=(5,0), sticky="ew")
        
        # Main display (shows current number)
        self.display_var = tk.StringVar(value="0")
        display = tk.Entry(
            self.window,
            textvariable=self.display_var,
            font=("Arial", 24, "bold"),
            justify="right",
            state="readonly",
            bg="black",
            fg="white",
            bd=0,
            relief="flat"
        )
        display.grid(row=1, column=0, columnspan=4, padx=5, pady=(0,10), sticky="ew", ipady=10)
        
        # Button layout
        buttons = [
            ["C", "±", "%", "÷"],
            ["7", "8", "9", "×"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "="]
        ]
        
        # Create buttons
        for i, row in enumerate(buttons):
            for j, text in enumerate(row):
                if text == "0":
                    # Zero button spans 2 columns
                    btn = tk.Button(
                        self.window,
                        text=text,
                        font=("Arial", 18, "bold"),
                        command=lambda t=text: self.button_click(t),
                        bg="#e0e0e0",
                        fg="black",
                        relief="raised",
                        bd=1,
                        activebackground="#d0d0d0"
                    )
                    btn.grid(row=i+2, column=j, columnspan=2, padx=1, pady=1, sticky="ew", ipady=15)
                elif text in ["÷", "×", "-", "+", "="]:
                    # Operator buttons
                    color = "#ff9500" if text != "=" else "#ff9500"
                    btn = tk.Button(
                        self.window,
                        text=text,
                        font=("Arial", 18, "bold"),
                        command=lambda t=text: self.button_click(t),
                        bg=color,
                        fg="white",
                        relief="raised",
                        bd=1,
                        activebackground="#e08600"
                    )
                    if text == "0":
                        continue  # Skip since we already handled it
                    else:
                        btn.grid(row=i+2, column=j, padx=1, pady=1, sticky="ew", ipady=15)
                elif text in ["C", "±", "%"]:
                    # Special buttons
                    btn = tk.Button(
                        self.window,
                        text=text,
                        font=("Arial", 18, "bold"),
                        command=lambda t=text: self.button_click(t),
                        bg="#a6a6a6",
                        fg="white",
                        relief="raised",
                        bd=1,
                        activebackground="#8a8a8a"
                    )
                    btn.grid(row=i+2, column=j, padx=1, pady=1, sticky="ew", ipady=15)
                else:
                    # Number buttons
                    btn = tk.Button(
                        self.window,
                        text=text,
                        font=("Arial", 18, "bold"),
                        command=lambda t=text: self.button_click(t),
                        bg="#e0e0e0",
                        fg="black",
                        relief="raised",
                        bd=1,
                        activebackground="#d0d0d0"
                    )
                    btn.grid(row=i+2, column=j, padx=1, pady=1, sticky="ew", ipady=15)
        
        # Configure grid weights
        for i in range(4):
            self.window.grid_columnconfigure(i, weight=1)
            
    def update_history_display(self):
        """Update the calculation history display"""
        if self.previous and self.operator:
            display_text = f"{self.previous} {self.operator} {self.current}"
            self.history_var.set(display_text)
        else:
            self.history_var.set("")
            
    def button_click(self, value):
        if value.isdigit() or value == ".":
            self.handle_number(value)
        elif value in ["÷", "×", "-", "+"]:
            self.handle_operator(value)
        elif value == "=":
            self.handle_equals()
        elif value == "C":
            self.handle_clear()
        elif value == "±":
            self.handle_plus_minus()
        elif value == "%":
            self.handle_percent()
            
    def handle_number(self, num):
        if self.should_reset:
            self.current = "0"
            self.should_reset = False
            
        if self.current == "0" and num != ".":
            self.current = num
        elif num == "." and "." not in self.current:
            self.current += num
        elif num != ".":
            self.current += num
            
        self.display_var.set(self.current)
        self.update_history_display()
        
    def handle_operator(self, op):
        if self.operator and not self.should_reset:
            # Calculate intermediate result and show it normally
            self.calculate_intermediate()
            
        self.previous = self.current
        self.operator = op
        self.should_reset = True
        self.update_history_display()
        
    def calculate_intermediate(self):
        """Calculate intermediate results (shown normally)"""
        try:
            prev_num = float(self.previous)
            curr_num = float(self.current)
            
            if self.operator == "+":
                result = prev_num + curr_num
            elif self.operator == "-":
                result = prev_num - curr_num
            elif self.operator == "×":
                result = prev_num * curr_num
            elif self.operator == "÷":
                if curr_num == 0:
                    raise ZeroDivisionError
                result = prev_num / curr_num
            else:
                return
                
            # Format result normally
            if result == int(result):
                self.current = str(int(result))
            else:
                self.current = f"{result:.10g}"  # Remove trailing zeros
                
            self.display_var.set(self.current)
            
        except ZeroDivisionError:
            self.display_var.set("Error")
            self.current = "0"
        except:
            self.display_var.set("Error")
            self.current = "0"
        
    def handle_equals(self):
        """Handle equals - this is where we show 'חוח' instead of result"""
        if self.operator and self.previous:
            try:
                # Show the complete calculation in history
                complete_calc = f"{self.previous} {self.operator} {self.current} ="
                self.history_var.set(complete_calc)
                
                # Instead of showing the actual result, show "חוח"
                self.display_var.set("חוח")
                self.current = "0"  # Reset for next calculation
                self.operator = ""
                self.previous = ""
                self.should_reset = True
                
            except:
                self.display_var.set("Error")
                self.current = "0"
                self.operator = ""
                self.previous = ""
                self.should_reset = True
                
    def handle_clear(self):
        self.current = "0"
        self.previous = ""
        self.operator = ""
        self.should_reset = False
        self.display_var.set("0")
        self.history_var.set("")
        
    def handle_plus_minus(self):
        if self.current != "0" and self.current != "חוח":
            try:
                if self.current.startswith("-"):
                    self.current = self.current[1:]
                else:
                    self.current = "-" + self.current
                self.display_var.set(self.current)
                self.update_history_display()
            except:
                pass
            
    def handle_percent(self):
        if self.current != "0" and self.current != "חוח":
            try:
                result = float(self.current) / 100
                if result == int(result):
                    self.current = str(int(result))
                else:
                    self.current = f"{result:.10g}"
                self.display_var.set(self.current)
                self.update_history_display()
            except:
                pass
                
    def run(self):
        self.window.mainloop()

# Create and run calculator
if __name__ == "__main__":
    calc = Calculator()
    print("מחשבון חוח מופעל!")
    print("המחשבון מציג מספרים רגיל במהלך החישוב")
    print("אבל כשלוחצים '=' הוא מציג 'חוח' במקום התוצאה!")
    calc.run()
