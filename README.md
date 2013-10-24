vsc
===

A very basic syntax checker for Vimscript

Since Vimscript consists of 519 different commands, each with numerous parameters, it’s hardly possible to create the complete syntax tree of a file.
Therefore, this script will check only for a few things I run very often into:
	1. check if every code line starts with a command name
	2. check the existence and correct nesting of control structures, that is, :function, :while, :for, :if, :else, :endif, :try, :end* ...
	3. check if a function argument is actually used inside the function. If you’re like me and constantly forget to put a a: in front of a variable, this wil help you.

But note that because of the many quirks, tricks and abbreviations Vimscript offers the developer, this program will produce many false positives on every moderately complex script file, for example in the following cases:
	- when a line starts with a command defined by the script developer
	- when function arguments appear only inside a string, for example in a map() function. That’s because VSC removes every string it finds to not be fooled by things within them.
	- when a pipe | appears inside a command, e.g. in a regexp, the line will be split and may look like illegal lines for VSC
