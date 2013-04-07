import sublime, sublime_plugin

class Bracket:
    def __init__(self, bracket, index):
        self.bracket = bracket
        self.index = index

class Stack :
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        return self.items[-1]

class ClojureReindentCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        bracket_stack = Stack()
        result = ""
        for selection in self.view.sel():
            for line in self.view.lines(selection):
                line_text = self.view.substr(line)
                new_line_text = line_text.strip()

                if bracket_stack.is_empty():
                    current_line_indent = 0
                elif bracket_stack.peek().bracket == '(':
                    current_line_indent = bracket_stack.peek().index + 2
                else:
                    current_line_indent = bracket_stack.peek().index + 1

                for column_index, ch in enumerate(new_line_text):
                    if ch in ['{', '(', '[']:
                        bracket_stack.push(Bracket(ch, current_line_indent + column_index))
                    if ch in ['}', ')', ']']:
                        bracket_stack.pop()

                indentation_string = " " * current_line_indent
                result += indentation_string + new_line_text + '\n'
        self.view.replace(edit, sublime.Region(self.view.sel()[0].a, self.view.sel()[0].b), result)
