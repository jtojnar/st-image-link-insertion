# Image Link Insertion for Sublime Text

Simple helper for inserting images into (not only) markdown documents for Sublime Text.

This is a port of my [Atom package](https://github.com/jtojnar/markdown-image-insertion) to Sublime Text 4. It requires at least Sublime Text 4075.

## Usage

1. Click `Tools` → `Insert images as markup`.
2. Select images using the dialogue that will open.

Inserted code can be customized in settings.

## Installation

You can install this package using [Package Control](https://packagecontrol.io/installation) using the name “Image Link Insertion”.

For development, you will want to clone the repository into “Image Link Insertion” directory in the Sublime Text’s `Packages` directory (`Preferences` → `Browse Packages…`):

```
git clone git@github.com:jtojnar/sublime-image-link-insertion.git 'Image Link Insertion'
```

(Or create a symlink with such name from your projects directory.)

## Customization

You can adjust any of the [supported configuration keys](image-link-insertion.sublime-settings) in the editor-wide settings (accessible via `Preferences` → `Package Settings` → `Image Link Insertion` → `Settings`).

You can also override the options for [individual projects](https://www.sublimetext.com/docs/projects.html#settings-key) or [views, based on active syntax](https://www.sublimetext.com/docs/settings.html#syntax-specific-settings) – in those cases, follow the same syntax as the package settings but nest it under `image-link-insertion` key (for projects, also under the `settings` key):

```json
// These settings override both User and Default settings for the LaTeX syntax
{
    "image-link-insertion": {
        "image_code": "\\begin{{figure}}\n\\includegraphics{{{url}}}\n\\end{{figure}}\n"
    }
}
```
