import tkinter as tk
from tkinter import messagebox, filedialog, font, colorchooser, simpledialog

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Editor")
        self.textarea = tk.Text(self.root, undo=True)
        self.textarea.pack(fill=tk.BOTH, expand=True)

        # Create the menu bar
        self.menubar = tk.Menu(self.root)
        self.root.config(menu=self.menubar)

        # Add file menu
        self.file_menu = tk.Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_file_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)

        # Add edit menu
        self.edit_menu = tk.Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo", command=self.textarea.edit_undo)
        self.edit_menu.add_command(label="Redo", command=self.textarea.edit_redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Cut", command=self.cut)
        self.edit_menu.add_command(label="Copy", command=self.copy)
        self.edit_menu.add_command(label="Paste", command=self.paste)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Select All", command=self.select_all)

        # Add format menu
        self.format_menu = tk.Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label="Format", menu=self.format_menu)
        self.format_menu.add_command(label="Font", command=self.change_font)
        self.format_menu.add_command(label="Text Color", command=self.change_text_color)
        self.format_menu.add_command(label="Background Color", command=self.change_bg_color)
        self.format_menu.add_command(label="Toggle Bold", command=self.toggle_bold)

        # Add view menu
        self.view_menu = tk.Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label="View", menu=self.view_menu)
        self.view_menu.add_command(label="Increase Text Size", command=self.increase_text_size)
        self.view_menu.add_command(label="Decrease Text Size", command=self.decrease_text_size)

        # Add position menu
        self.position_menu = tk.Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label="Position", menu=self.position_menu)
        self.position_menu.add_command(label="Go to Line", command=self.go_to_line)

        # Add highlight menu
        self.highlight_menu = tk.Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label="Highlight", menu=self.highlight_menu)
        self.highlight_menu.add_command(label="Highlight Text", command=self.highlight_text)
        self.highlight_menu.add_command(label="Clear Highlight", command=self.clear_highlight)

        # Add theme menu
        self.theme_menu = tk.Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label="Theme", menu=self.theme_menu)
        self.theme_menu.add_command(label="Light", command=self.set_light_theme)
        self.theme_menu.add_command(label="Dark", command=self.set_dark_theme)

    def new_file(self):
        self.textarea.delete("1.0", tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            try:
                with open(file_path, "r") as file:
                    content = file.read()
                self.textarea.delete("1.0", tk.END)
                self.textarea.insert(tk.END, content)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to open file: {str(e)}")

    def save_file(self):
        if not self.textarea.get("1.0", tk.END).strip():
            messagebox.showwarning("Warning", "No content to save.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            try:
                with open(file_path, "w") as file:
                    file.write(self.textarea.get("1.0", tk.END))
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file: {str(e)}")

    def save_file_as(self):
        if not self.textarea.get("1.0", tk.END).strip():
            messagebox.showwarning("Warning", "No content to save.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            try:
                with open(file_path, "w") as file:
                    file.write(self.textarea.get("1.0", tk.END))
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file: {str(e)}")

    def cut(self):
        self.textarea.event_generate("<<Cut>>")

    def copy(self):
        self.textarea.event_generate("<<Copy>>")

    def paste(self):
        self.textarea.event_generate("<<Paste>>")

    def select_all(self):
        self.textarea.tag_add(tk.SEL, "1.0", tk.END)
        self.textarea.mark_set(tk.INSERT, "1.0")
        self.textarea.see(tk.INSERT)
        return "break"

    def change_font(self):
        font_family = font.families()
        selected_font = font.askfont()
        if selected_font:
            self.textarea.configure(font=selected_font)

    def change_text_color(self):
        color = colorchooser.askcolor(title="Select Text Color")
        if color:
            self.textarea.config(fg=color[1])

    def change_bg_color(self):
        color = colorchooser.askcolor(title="Select Background Color")
        if color:
            self.textarea.config(bg=color[1])

    def toggle_bold(self):
        current_font = font.Font(font=self.textarea["font"])
        is_bold = current_font.actual()["weight"] == "bold"
        font_weight = "normal" if is_bold else "bold"
        self.textarea.configure(font=(current_font.actual()["family"], current_font.actual()["size"], font_weight))

    def increase_text_size(self):
        current_font = font.Font(font=self.textarea["font"])
        font_size = current_font.actual()["size"]
        new_font_size = max(font_size + 2, 8)
        self.textarea.configure(font=(current_font.actual()["family"], new_font_size))

    def decrease_text_size(self):
        current_font = font.Font(font=self.textarea["font"])
        font_size = current_font.actual()["size"]
        new_font_size = max(font_size - 2, 8)
        self.textarea.configure(font=(current_font.actual()["family"], new_font_size))

    def go_to_line(self):
        line_number = simpledialog.askinteger("Go to Line", "Enter line number:")
        if line_number:
            line_index = f"{line_number}.0"
            self.textarea.mark_set(tk.INSERT, line_index)
            self.textarea.see(tk.INSERT)

    def highlight_text(self):
        start_index = self.textarea.index(tk.SEL_FIRST)
        end_index = self.textarea.index(tk.SEL_LAST)
        self.textarea.tag_add(tk.SEL, start_index, end_index)
        self.textarea.tag_config("highlight", background="yellow")

    def clear_highlight(self):
        self.textarea.tag_remove(tk.SEL, "1.0", tk.END)
        self.textarea.tag_remove("highlight", "1.0", tk.END)

    def set_light_theme(self):
        self.textarea.config(bg="white", fg="black")

    def set_dark_theme(self):
        self.textarea.config(bg="black", fg="white")

if __name__ == "__main__":
    root = tk.Tk()
    text_editor = TextEditor(root)
    root.mainloop()
