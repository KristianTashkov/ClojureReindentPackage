ClojureReindentPackage
======================

A Sublime Text 2 package that includes a command which reindents your selection according to clojure guidelines
You can bind the command to a keybinding by putting a line of some sort in the user keybindings:
<code>{ "keys": ["f12"], "command": "clojure_reindent"}</code>

Usage:
 - Select the whole file and run the command to autoindent everthing
 - Select a block of code reperesenting a top-level function and run the command

Disclaimer:
This package doesn't change or break the lines themselves to fix your indentation. It just puts the correct amount of indentation before each line. This isn't a tool to fix your bad structured code.
