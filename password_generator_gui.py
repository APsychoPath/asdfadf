#!/usr/bin/env python3
"""
Password Generator GUI
----------------------
A simple GUI application to generate secure random passwords.
"""

import random
import string
import tkinter as tk
from tkinter import messagebox


class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x300")
        
        # Variables
        self.password_length = tk.IntVar(value=12)
        self.use_uppercase = tk.BooleanVar(value=True)
        self.use_digits = tk.BooleanVar(value=True)
        self.use_special = tk.BooleanVar(value=True)
        self.generated_password = tk.StringVar()
        
        # Create UI
        self.create_widgets()
    
    def create_widgets(self):
        """Create all UI widgets."""
        # Password Length
        tk.Label(self.root, text="Password Length:").pack(pady=5)
        tk.Scale(self.root, from_=8, to=32, variable=self.password_length, orient=tk.HORIZONTAL).pack()
        
        # Options
        tk.Label(self.root, text="Options:").pack(pady=5)
        
        tk.Checkbutton(self.root, text="Include Uppercase Letters", 
                      variable=self.use_uppercase).pack(anchor=tk.W)
        tk.Checkbutton(self.root, text="Include Digits", 
                      variable=self.use_digits).pack(anchor=tk.W)
        tk.Checkbutton(self.root, text="Include Special Characters", 
                      variable=self.use_special).pack(anchor=tk.W)
        
        # Generate Button
        tk.Button(self.root, text="Generate Password", command=self.generate_password).pack(pady=10)
        
        # Password Display
        tk.Label(self.root, text="Generated Password:").pack()
        tk.Entry(self.root, textvariable=self.generated_password, width=30, state='readonly').pack(pady=5)
        
        # Copy Button
        tk.Button(self.root, text="Copy to Clipboard", command=self.copy_to_clipboard).pack()
    
    def generate_password(self):
        """Generate a password based on user preferences."""
        try:
            length = self.password_length.get()
            uppercase = self.use_uppercase.get()
            digits = self.use_digits.get()
            special = self.use_special.get()
            
            # Define character sets
            chars = string.ascii_lowercase
            if uppercase:
                chars += string.ascii_uppercase
            if digits:
                chars += string.digits
            if special:
                chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"
            
            # Generate password
            password = ''.join(random.choice(chars) for _ in range(length))
            
            # Ensure complexity requirements
            if uppercase and not any(c.isupper() for c in password):
                password = password[:-1] + random.choice(string.ascii_uppercase)
            if digits and not any(c.isdigit() for c in password):
                password = password[:-1] + random.choice(string.digits)
            if special and not any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
                password = password[:-1] + random.choice("!@#$%^&*()_+-=[]{}|;:,.<>?")
            
            self.generated_password.set(password)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate password: {e}")
    
    def copy_to_clipboard(self):
        """Copy the generated password to clipboard."""
        password = self.generated_password.get()
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            messagebox.showinfo("Success", "Password copied to clipboard!")
        else:
            messagebox.showwarning("Warning", "No password to copy!")


def main():
    """Main function to run the application."""
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()