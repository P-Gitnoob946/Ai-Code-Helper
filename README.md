AI Coding Buddy
This is a desktop application that serves as your intelligent coding assistant. It leverages Google Gemini AI to generate code, explain code snippets, and adapt to your personal coding style across Python, C++, and Java. The app features a modern PyQt6 GUI with theme toggling and syntax highlighting for a seamless developer experience.
 
Features
•	AI-Powered Code Generation: Generate code in Python, C++, or Java based on your prompt and preferred style.
•	Code Explanation: Get simple explanations for any code snippet.
•	Personalized Coding Style: The app learns and adapts to your naming conventions, indentation, docstring usage, and commenting preferences.
•	Syntax Highlighting: Built-in syntax highlighters for Python, C++, and Java for improved code readability.
•	Dark/Light Theme Support: Easily switch between dark and light modes.
•	Intuitive GUI: User-friendly interface built with PyQt6 and qdarktheme.

 
Installation
Prerequisites
•	Python 3.9+
•	Google Generative AI Python SDK (google-generativeai)
•	PyQt6
•	qdarktheme
•	python-dotenv
Install Dependencies
pip install google-generativeai PyQt6 qdarktheme python-dotenv

Clone the Repository
git clone https://github.com/yourusername/codenpookie.git
cd codenpookie

 
Setup
1.	Google Gemini API Key:
o	Obtain an API key from Google Generative AI.
o	Create a .env file in the project root with:
GEMINI_API_KEY=your-api-key-here

2.	Icons:
o	Place an icon.png file in the project directory for the app window icon.
 
Usage
Run the main application:
python aicodehelper.py

•	Enter your coding prompt and select the desired language.
•	Submit code samples to teach the AI your coding style.
•	Click "Generate Code" to produce code following your style.
•	View code explanations in the right panel.
•	Toggle between dark and light themes as needed.
 
File Structure
File	Purpose
aicodehelper.py	Main application and GUI logic
syntax_highlighter.py	Syntax highlighters for Python, C++, and Java
user_coding_style.json	Stores your personalized coding style preferences
test_gemini.py	Simple script to test Gemini API integration

 
Customization
•	Coding Style:
The app stores your style in user_coding_style.json. You can update your style by submitting code samples.
•	Adding Languages:
Extend syntax_highlighter.py and update the UI in aicodehelper.py to support more languages.
 
Contributing
Pull requests are welcome! Please open an issue to discuss your ideas or report bugs.


Acknowledgements
•	Google Generative AI
•	PyQt6
•	qdarktheme
 
Disclaimer
This project is for educational and personal productivity purposes. Always review generated code before using it in production.
 
Contact
For questions or feedback, open an issue or contact pkpraveen987654321@gmail.com
 
