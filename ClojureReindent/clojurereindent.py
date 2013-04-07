import sublime, sublime_plugin

class Bracket :
  def __init__(self, bracket, index) :
    self.bracket = bracket
    self.index = index

class Stack :
  def __init__(self) :
    self.items = []

  def push(self, item) :
    self.items.append(item)

  def pop(self) :
    return self.items.pop()

  def isEmpty(self) :
    return (self.items == [])

  def peek(self) :
    return self.items[len(self.items)-1]

class ClojureReindentCommand(sublime_plugin.TextCommand):
   def run(self, edit):
      bracketStack = Stack()
      result = ""
      for selection in self.view.sel():
        for line in self.view.lines(selection):
          lineText = self.view.substr(line)
          newLineText = lineText.strip()

          if bracketStack.isEmpty():
            currentLineIndent = 0
          else:
            currentLineIndent = bracketStack.peek().index
            if bracketStack.peek().bracket == '(':
              currentLineIndent+=2
            else:
              currentLineIndent+=1

          columnIndex = 0
          for ch in newLineText:
            if ch == '{' or ch =='(' or ch == '[':
              bracketStack.push(Bracket(ch, currentLineIndent + columnIndex))
            if ch == '}' or ch ==')' or ch == ']':
              bracketStack.pop()
            columnIndex+=1
          indentationString = ""
          for i in range(currentLineIndent):
            indentationString+=" "
          result+=indentationString + newLineText+'\n'
      self.view.replace(edit, sublime.Region(self.view.sel()[0].a, self.view.sel()[0].b), result)