from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QSyntaxHighlighter, QTextCharFormat, QColor, QFont

def format(color, style=''):
    _color = QColor()
    _color.setNamedColor(color)
    _format = QTextCharFormat()
    _format.setForeground(_color)
    if 'bold' in style:
        _format.setFontWeight(QFont.Weight.Bold)
    if 'italic' in style:
        _format.setFontItalic(True)
    return _format

class PythonHighlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.highlighting_rules = []

        keyword_format = format('blue')
        keywords = ['and', 'as', 'assert', 'break', 'class', 'continue', 'def',
                    'del', 'elif', 'else', 'except', 'False', 'finally', 'for',
                    'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
                    'None', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
                    'True', 'try', 'while', 'with', 'yield']
        for word in keywords:
            pattern = QRegularExpression(r'\b' + word + r'\b')
            self.highlighting_rules.append((pattern, keyword_format))

        class_format = format('darkMagenta')
        class_pattern = QRegularExpression(r'\bclass\b\s*(\w+)')
        self.highlighting_rules.append((class_pattern, class_format))

        function_format = format('darkCyan')
        function_pattern = QRegularExpression(r'\bdef\b\s*(\w+)')
        self.highlighting_rules.append((function_pattern, function_format))

        comment_format = format('darkGreen', 'italic')
        comment_pattern = QRegularExpression(r'#[^\n]*')
        self.highlighting_rules.append((comment_pattern, comment_format))

        string_format = format('darkYellow')
        string_pattern = QRegularExpression(r'(\'\'\'.*?\'\'\'|\"\"\".*?\"\"\"|\'.*?\'|".*?")')
        self.highlighting_rules.append((string_pattern, string_format))

    def highlightBlock(self, text):
        for pattern, format in self.highlighting_rules:
            expression = QRegularExpression(pattern)
            match = expression.match(text)
            while match.hasMatch():
                start = match.capturedStart()
                length = match.capturedLength()
                self.setFormat(start, length, format)
                match = expression.match(text, start + length)

class CppHighlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.highlighting_rules = []

        keyword_format = format('blue')
        keywords = ['asm', 'auto', 'bool', 'break', 'case', 'catch', 'char',
                    'class', 'const', 'continue', 'default', 'delete', 'do',
                    'double', 'else', 'enum', 'explicit', 'export', 'extern',
                    'false', 'float', 'for', 'friend', 'goto', 'if', 'inline',
                    'int', 'long', 'mutable', 'namespace', 'new', 'operator',
                    'private', 'protected', 'public', 'register', 'return',
                    'short', 'signed', 'sizeof', 'static', 'struct', 'switch',
                    'template', 'this', 'throw', 'true', 'try', 'typedef',
                    'typeid', 'typename', 'union', 'unsigned', 'using',
                    'virtual', 'void', 'volatile', 'while']
        for word in keywords:
            pattern = QRegularExpression(r'\b' + word + r'\b')
            self.highlighting_rules.append((pattern, keyword_format))

        class_format = format('darkMagenta')
        class_pattern = QRegularExpression(r'\bclass\b\s*(\w+)')
        self.highlighting_rules.append((class_pattern, class_format))

        function_format = format('darkCyan')
        function_pattern = QRegularExpression(r'\b[A-Za-z0-9_]+(?=\()')
        self.highlighting_rules.append((function_pattern, function_format))

        comment_format = format('darkGreen', 'italic')
        comment_pattern = QRegularExpression(r'//[^\n]*')
        self.highlighting_rules.append((comment_pattern, comment_format))

        string_format = format('darkYellow')
        string_pattern = QRegularExpression(r'".*?"')
        self.highlighting_rules.append((string_pattern, string_format))

    def highlightBlock(self, text):
        for pattern, format in self.highlighting_rules:
            expression = QRegularExpression(pattern)
            match = expression.match(text)
            while match.hasMatch():
                start = match.capturedStart()
                length = match.capturedLength()
                self.setFormat(start, length, format)
                match = expression.match(text, start + length)

class JavaHighlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.highlighting_rules = []

        keyword_format = format('blue')
        keywords = ['abstract', 'assert', 'boolean', 'break', 'byte', 'case',
                    'catch', 'char', 'class', 'const', 'continue', 'default',
                    'do', 'double', 'else', 'enum', 'extends', 'final',
                    'finally', 'float', 'for', 'goto', 'if', 'implements',
                    'import', 'instanceof', 'int', 'interface', 'long',
                    'native', 'new', 'package', 'private', 'protected',
                    'public', 'return', 'short', 'static', 'strictfp', 'super',
                    'switch', 'synchronized', 'this', 'throw', 'throws',
                    'transient', 'try', 'void', 'volatile', 'while']
        for word in keywords:
            pattern = QRegularExpression(r'\b' + word + r'\b')
            self.highlighting_rules.append((pattern, keyword_format))

        class_format = format('darkMagenta')
        class_pattern = QRegularExpression(r'\bclass\b\s*(\w+)')
        self.highlighting_rules.append((class_pattern, class_format))

        function_format = format('darkCyan')
        function_pattern = QRegularExpression(r'\b[A-Za-z0-9_]+(?=\()')
        self.highlighting_rules.append((function_pattern, function_format))

        comment_format = format('darkGreen', 'italic')
        comment_pattern = QRegularExpression(r'//[^\n]*')
        self.highlighting_rules.append((comment_pattern, comment_format))

        string_format = format('darkYellow')
        string_pattern = QRegularExpression(r'".*?"')
        self.highlighting_rules.append((string_pattern, string_format))

    def highlightBlock(self, text):
        for pattern, format in self.highlighting_rules:
            expression = QRegularExpression(pattern)
            match = expression.match(text)
            while match.hasMatch():
                start = match.capturedStart()
                length = match.capturedLength()
                self.setFormat(start, length, format)
                match = expression.match(text, start + length)
