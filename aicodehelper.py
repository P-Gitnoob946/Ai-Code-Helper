import autogen
import google.generativeai as genai
import os
import json
from dotenv import load_dotenv
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QTextEdit, QPushButton, QComboBox, QLabel, QLineEdit, QMessageBox)
from PyQt6.QtGui import QFont, QPalette, QIcon
from PyQt6.QtCore import Qt, QTimer
import qdarktheme

# Load API Key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

config = {"use_docker": False}

STYLE_DB = "user_coding_style.json"

def load_user_style():
    if os.path.exists(STYLE_DB):
        with open(STYLE_DB, "r") as f:
            return json.load(f)
    return {"naming_convention": "snake_case", "indentation": 4, "docstrings": True, "comments": "descriptive", "language": "Python"}

def save_user_style(style_data):
    with open(STYLE_DB, "w") as f:
        json.dump(style_data, f, indent=4)

def analyze_user_code(user_code, language):
    style_data = load_user_style()
    style_data["language"] = language
    save_user_style(style_data)

def generate_code(prompt, language):
    style = load_user_style()
    model = genai.GenerativeModel("gemini-pro")
    full_prompt = f"""
    Generate code in {language} that follows these rules:
    - Naming convention: {style['naming_convention']}
    - Indentation: {style['indentation']} spaces
    - Use docstrings: {style['docstrings']}
    - Commenting style: {style['comments']}
    Task: {prompt}
    """
    response = model.generate_content(full_prompt)
    return response.text if response and response.text else "Error: No response from API."

def generate_explanation(code):
    model = genai.GenerativeModel("gemini-pro")
    prompt = f"Explain the following code in simple terms:\n\n{code}"
    response = model.generate_content(prompt)
    return response.text if response and response.text else "Error: No explanation generated."

class CodenPookieApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CodenPookie - AI Coding Buddy")
        self.setGeometry(100, 100, 1200, 800)
        self.setWindowIcon(QIcon("icon.png"))
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        self.setup_ui()
    
    def setup_ui(self):
        input_layout = QHBoxLayout()
        self.prompt_input = QLineEdit()
        self.prompt_input.setPlaceholderText("Enter your coding prompt...")
        input_layout.addWidget(self.prompt_input)
        
        self.lang_combo = QComboBox()
        self.lang_combo.addItems(["Python", "C++", "Java"])
        input_layout.addWidget(self.lang_combo)
        
        self.layout.addLayout(input_layout)
        
        self.code_explanation_layout = QHBoxLayout()
        
        self.code_editor = QTextEdit()
        self.code_editor.setFont(QFont("Consolas", 12))
        self.code_explanation_layout.addWidget(self.code_editor)

        self.explanation_editor = QTextEdit()
        self.explanation_editor.setFont(QFont("Consolas", 12))
        self.explanation_editor.setReadOnly(True)
        self.code_explanation_layout.addWidget(self.explanation_editor)
        
        self.layout.addLayout(self.code_explanation_layout)
        
        control_layout = QHBoxLayout()
        
        self.submit_button = QPushButton("Submit Sample Code")
        self.submit_button.clicked.connect(self.submit_code)
        control_layout.addWidget(self.submit_button)
        
        self.generate_button = QPushButton("Generate Code")
        self.generate_button.clicked.connect(self.generate)
        control_layout.addWidget(self.generate_button)
        
        self.theme_button = QPushButton("Toggle Theme")
        self.theme_button.clicked.connect(self.toggle_theme)
        control_layout.addWidget(self.theme_button)
        
        self.layout.addLayout(control_layout)
    
    def submit_code(self):
        user_code = self.code_editor.toPlainText()
        language = self.lang_combo.currentText()
        analyze_user_code(user_code, language)
        explanation = generate_explanation(user_code)
        self.explanation_editor.setPlainText(explanation)
        QMessageBox.information(self, "Success", "Coding style updated!")
    
    def generate(self):
        language = self.lang_combo.currentText()
        prompt = self.prompt_input.text()
        self.statusBar().showMessage("Generating code...")
        QTimer.singleShot(100, lambda: self.do_generate(prompt, language))
    
    def do_generate(self, prompt, language):
        response = generate_code(prompt, language)
        self.code_editor.setPlainText(response)
        explanation = generate_explanation(response)
        self.explanation_editor.setPlainText(explanation)
        self.statusBar().showMessage("Code generated successfully!")
    
    def toggle_theme(self):
        if self.palette().color(QPalette.Window).lightness() > 128:
            self.setStyleSheet(qdarktheme.load_stylesheet("dark"))
        else:
            self.setStyleSheet(qdarktheme.load_stylesheet("light"))

if __name__ == "__main__":
    app = QApplication([])
    app.setStyleSheet(qdarktheme.load_stylesheet("dark"))
    window = CodenPookieApp()
    window.show()
    app.exec()