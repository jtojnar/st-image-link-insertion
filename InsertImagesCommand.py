import os
import sublime
import sublime_plugin


class ImageLinkInsertionInsertImagesCommand(sublime_plugin.TextCommand):
    """
    Insert relative links to the given files into the current view.
    """

    def run(self, edit, files):
        edited_file = self.view.file_name()

        if len(files) > 0:
            settings = sublime.load_settings("image-link-insertion.sublime-settings")
            image_code = settings.get("image_code")

            if edited_file is not None:
                edited_file_location = os.path.dirname(edited_file)
                files = [
                    os.path.relpath(absolute_path, edited_file_location)
                    for absolute_path in files
                ]

            text = ""

            for file in files:
                text += image_code.format(url=file)

            self.view.insert(edit, self.view.sel()[0].begin(), text)
