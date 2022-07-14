from collections import ChainMap
from sublime_lib import NamedSettingsDict
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
            settings = ChainMap(
                self.view.settings().get('image-link-insertion', {}),
                self.view.window().settings().get('image-link-insertion', {}),
                NamedSettingsDict('image-link-insertion')
            )
            image_code = settings.get("image_code")
            fix_slashes = settings.get("fix_slashes")
            wrapping_mode = settings.get("wrapping_mode")
            wrapping_prologue = settings.get("wrapping_prologue")
            wrapping_epilogue = settings.get("wrapping_epilogue")
            wrapping_enabled = wrapping_mode == "zero" or (wrapping_mode == "multiple" and len(files) > 1)

            if edited_file is not None:
                edited_file_location = os.path.dirname(edited_file)
                files = [
                    os.path.relpath(absolute_path, edited_file_location)
                    for absolute_path in files
                ]

            if fix_slashes:
                files = [
                    path.replace(os.path.sep, '/')
                    for path in files
                ]

            text = wrapping_prologue if wrapping_enabled else ""

            for file in files:
                text += image_code.format(url=file)

            text += wrapping_epilogue if wrapping_enabled else ""

            self.view.insert(edit, self.view.sel()[0].begin(), text)
