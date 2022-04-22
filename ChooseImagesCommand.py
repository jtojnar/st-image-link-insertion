import os
import sublime
import sublime_plugin


class ImageLinkInsertionChooseImagesCommand(sublime_plugin.TextCommand):
    """
    Opens a file chooser dialogue for selecting a list of files and then calls `image_link_insertion_insert_images` command with the list.
    """

    def run(self, edit):
        path = self.view.file_name()
        sublime.open_dialog(
            callback=self.handle_response,
            file_types=[
                ("Images", ["jpg", "jpeg", "png", "gif", "webp", "svg"]),
            ],
            directory=os.path.dirname(path) if path else None,
            multi_select=True,
        )

    def handle_response(self, files):
        if files is not None:
            self.view.run_command(
                "image_link_insertion_insert_images",
                {
                    "files": files,
                },
            )
