# Description

ASPComment is a plugin for SublimeText2 that enables programmers in ASP (or VbScript, Visual Basic, etc.) to comment out a selection of text.

Currently, Sublime's built in 'Toggle Comment' function treats ASP blocks like an html block and uses the html comment to comment out the selection. This is hard on ASP programmers as they do not have any means of a block comment. In ASP, lines must be commented out one by one, prefixing with a single quote.

ASPComment provides this functionality so that programmers of any language using single quote comments can comment out entire selections with ease.

# Installation

1. If you have SublimeText2 Package Manager installed (recommended), press Ctrl + Shift + P, type "install" and press Enter, type "ASPComment" and press Enter.

2. Download the Zip file, unzip the folder and copy it to your <code>C:\Users\Daniel\AppData\Roaming\Sublime Text 2\Packages</code> directory. (Google the directory if your OSX or Linux)

Once installed, you can edit the keyboard shortcuts in the following files:

<ul>
    <li>Default (Linux).sublime-keymap</li>
    <li>Default (OSX).sublime-keymap</li>
    <li>Default (Windows).sublime-keymap</li>
</ul>

# Commands

You can run commands by using the keyboard shortcuts, or through the command menu by pressing Ctrl/Cmd+P and typing "ASPComment".

The Toggle command is defaulted to Ctrl + ' (Cmd + ' for OSX) and the Add and Remove commands have entries in the Defaults files but are commented out.

All commands require one or more active selections of text in your editor to have any effect.

Lastly, it should be noted that all of the following commands employ the following logic for user-friendliness:

<ul>
  <li>Whenever performing line operations/conditions, the whitespace at the front of the line is negligibles.</li>
  <li>When adding a comment, lines that already start with a single quote will not be double commented.</li>
</ul>

## Add Comment

    asp_comment_add_comment

This command adds a single quote <code>'</code> to the front of each line in the current selection. As mentioned previously, lines will not be double commented. Any selection spanning a mix of commented lines will simply comment any lines that were not already commented.

## Remove Comment

    asp_comment_remove_comment

This command removes the first single quote <code>'</code> from the line if it is the first non-whitespace character. Any lines without a leading single quote are ignored.

## Toggle Comment

    asp_comment_toggle_comment

This command toggles comments on the current selection. The toggle performs the operation that compliments whichever line type, commented or uncommented, has the most occurences. In otherwords, if more lines are commented in the current selection, they are all uncmomented. If more lines are uncommented, the selection is commented.

If you wanted the opposite action from toggle, simply toggling twice will have the desired effect.