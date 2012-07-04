import sublime, sublime_plugin

def isFirstCharSingleQuote(line):
	if len(line.lstrip()) > 0:
		if line.lstrip()[0] == "'":
			return 1

	return 0

def addComment(line):
	# lstrip removes any leading whitespace
	# then we check if the first character is a single-quote
	if not(isFirstCharSingleQuote(line)):
		line = "'" + line

	return line

def removeComment(line):
	# lstrip removes any leading whitespace
	# then we check if the first character is a single-quote
	if isFirstCharSingleQuote(line):
		line = line.replace("'", "", 1)

	return line;

class AspCommentAddCommentCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = sublime.active_window().active_view()
		edit = view.begin_edit()

		# loop through lines in selection
		for region in view.sel():
			# add single quote in front of each line
			newtext = '\n'.join(map(lambda line: addComment(line), view.substr(region).splitlines()))
			view.replace(edit, region, newtext)

		view.end_edit(edit)


class AspCommentRemoveCommentCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = sublime.active_window().active_view()
		edit = view.begin_edit()

		# loop through lines in selection
		for region in view.sel():
			newtext = '\n'.join(map(lambda line: removeComment(line), view.substr(region).splitlines()))
			view.replace(edit, region, newtext)

		view.end_edit(edit)


class AspCommentToggleCommentCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = sublime.active_window().active_view()
		edit = view.begin_edit()

		# loop through lines in selection
		for region in view.sel():
			commentList = map(lambda line: isFirstCharSingleQuote(line), view.substr(region).splitlines())
			totalComments = sum(commentList)

			if totalComments >= len(commentList) / 2:
				newRegion = '\n'.join(map(lambda line: removeComment(line), view.substr(region).splitlines()))
			else:
				newRegion = '\n'.join(map(lambda line: addComment(line), view.substr(region).splitlines()))


		view.replace(edit, region, newRegion)
		view.end_edit(edit)