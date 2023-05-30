import string
import tkinter as tk
from tkinter import messagebox

def preprocess_text(text):
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    words = text.split()
    return words

def calculate_similarity(text1, text2):
    words1 = preprocess_text(text1)
    words2 = preprocess_text(text2)
    
    common_words = set(words1) & set(words2)
    
    similarity = len(common_words) / (len(set(words1)) + len(set(words2)) - len(common_words))
    return similarity

def check_plagiarism():
    text1 = text_input1.get("1.0", tk.END).strip()
    text2 = text_input2.get("1.0", tk.END).strip()

    similarity = calculate_similarity(text1, text2)
    if similarity >= 0.5:
        result = f"Plagiarism detected!\nSimilarity: {similarity}"
    else:
        result = f"No plagiarism detected.\nSimilarity: {similarity}"
    
    plagiarism_value.config(state=tk.NORMAL)
    plagiarism_value.delete("1.0", tk.END)
    plagiarism_value.insert(tk.END, result)
    plagiarism_value.config(state=tk.DISABLED)

# Create the main window
window = tk.Tk()
window.title("Plagiarism Checker")
window.geometry("400x300")

# Create input labels
label1 = tk.Label(window, text="Enter the first text:", font=("Arial", 12))
label1.pack()
text_input1 = tk.Text(window, height=5, font=("Arial", 12))
text_input1.pack()

label2 = tk.Label(window, text="Enter the second text:", font=("Arial", 12))
label2.pack()
text_input2 = tk.Text(window, height=5, font=("Arial", 12))
text_input2.pack()

# Create a button to check plagiarism
plagiarism_button = tk.Button(window, text="Check Plagiarism", command=check_plagiarism, font=("Arial", 12), bg="#4caf50", fg="white")
plagiarism_button.pack(pady=10)

# Create a box to display plagiarism value
plagiarism_value = tk.Text(window, height=2, font=("Arial", 12), state=tk.DISABLED, bg="#f0f0f0")
plagiarism_value.pack()

# Start the main event loop
window.mainloop()