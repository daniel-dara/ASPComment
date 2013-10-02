# Description

ASPComment is a plugin for SublimeText2 that allows for multi-line commenting with single quotes, a convention used in Classic ASP, VbScript, and Visual Basic. Though SublimeText has a line commenting shortcut built in, it only supports HTML style comments for ASP (HTML) syntax, which do not work for ASP blocks. Furthermore it does not (natively) support VbScript or Visual Basic syntax highlighting and contexts.

ASPComment provides this functionality so that programmers of any language requiring single quote comments can enter comments with ease.

# Installation

1. Use the <a href="https://sublime.wbond.net/installation">SublimeText2 Package Manager</a> to install ASPComment.

2. You can manually install the package by downloading the zip file and extracting it to the location given in the <a href="http://www.sublimetext.com/docs/3/packages.html">documentation</a>.

# Commands

The default keymappings can be viewed by selecting <code>Preferences > Package Settings > ASPComment > Key Bindings - Default</code> from the SublimeText toolmenu. Changes to the keyboard shortcuts should be added to the corresponding "Key Bindings - User" file to override the default mappings rather than erase them.

<b>Note:</b> By default, if no selection is made, any performed action is applied to the line the cursor is currently on.

## Add Comment

    asp_comment_add_comment

Add a single quote (<code>'</code>) to the front of each line in the current selection. Selected lines already starting with a single quote will be ignored. Also note that empty lines are not commented.

## Remove Comment

    asp_comment_remove_comment

Remove a single quote <code>'</code> from each line in the current selection that starts with a single quote (ignores whitespace). Any lines without a leading single quote are unmodified.

## Toggle Comment

    asp_comment_toggle_comment

Toggles comments on the current selection. If there is a single uncommented line, then the entire selection is commented. If all lines are commented, the comments are removed. Also note that empty lines are not commented.

# Configuration

ASPComment has two settings which modify its behavior. These settings can be modified by adding them to the file found at <code>Preferences > Package Settings > ASPComment > Settings - User</code> with the desired value.

    allow_double_comments
  
When this setting is true and the <code>asp_comment_add_comment</code> action is performed, lines already starting with a single quote will still receive an additional single quote.

    comment_empty_lines
  
When this setting is true, empty lines will receive a single quote when <code>asp_comment_add_comment</code> or <code>asp_comment_toggle_comment</code> are performed.
