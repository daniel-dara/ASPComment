import sublime, sublime_plugin

s = sublime.load_settings('ASPComment.sublime-settings')

def isLineUncommented(line):
	if (checkFirstChar(line, "'") or (len(line.lstrip()) == 0 and
		s.get("comment_empty_lines") == False)):
		return 0

	return 1

def checkFirstChar(line, char, isToggle = False):
	line = line.lstrip()

	if len(line) > 0:
		if line[0] == char:
			return 1

	return 0

def addComment(line):
	# IF the first character isn't a single quote OR double quotes are allowed
	# AND the line is not empty or empty line are allowed
	# THEN coment the line.
	if ((not checkFirstChar(line, "'") or s.get("allow_double_comments")) and
		(len(line.lstrip()) > 0 or s.get("comment_empty_lines"))):
		if s.get("comment_after_indent"):
			# preserve indentation by adding quote between leading whitespace
			# and rest of line
			line = line[:len(line)-len(line.lstrip())] + "'" + line.lstrip()
		else:
			line = "'" + line

	return line

def removeComment(line):
	# IF the first character is a single quote
	# THEN remove it
	if checkFirstChar(line, "'"):
		line = line.replace("'", "", 1)

	return line;

class AspCommentAddCommentCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = sublime.active_window().active_view()
		edit = view.begin_edit()

		# Loop through each line in the selection
		for region in view.sel():
			# Add a single quote in front of each line
			newtext = '\n'.join(map(lambda line: addComment(line), view.substr(region).splitlines()))
			view.replace(edit, region, newtext)

		view.end_edit(edit)


class AspCommentRemoveCommentCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = sublime.active_window().active_view()
		edit = view.begin_edit()

		# Loop through each line in the selection
		for region in view.sel():
			# Remove the first character in front of each line if it is a single quote
			newtext = '\n'.join(map(lambda line: removeComment(line), view.substr(region).splitlines()))
			view.replace(edit, region, newtext)

		view.end_edit(edit)


class AspCommentToggleCommentCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = sublime.active_window().active_view()
		#edit = view.begin_edit()

		# loop through each line in the selection
		for region in view.sel():
			if region.empty():
				# Toggle the current line
				line = view.substr(view.line(region))
				view.replace(edit, view.line(region), (addComment if isLineUncommented(line) else removeComment)(line))
			else:
				# Toggle the current selection
				lines = view.substr(region).split('\n')

				uncommentedLines = map(lambda line: int(isLineUncommented(line)), lines)

				newRegion = ('\n'.join(map(addComment if sum(uncommentedLines) > 0 else removeComment,
							lines)))
				view.replace(edit, region, newRegion)

		#view.end_edit(edit)
