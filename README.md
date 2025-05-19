# Create and run Virtual Enviroment (Windows):

## Setup venv
To install and run the site from a shell, use the following. Adjust accordingly for platforms other than windows. This assumes that Python 3.X has already been installed.
```shell
python -m venv .venv             # Setup venv (first time only)
.venv\Scripts\Activate           # Activate vnenv
pip install -r requirements.txt  # Install dependencies
mkdocs serve                     # Run the development server
```

## Setup vscode (notes)
Setup vscode
Ctrl + Shift + P (Command Palette)
Python: Select Interpreter
Choose `.venv\Scripts\python.exe``

# Current
Working with languages
https://github.com/squidfunk/mkdocs-material/discussions/2346
https://github.com/squidfunk/mkdocs-material/blob/master/docs/setup/changing-the-language.md
https://jimandreas.github.io/mkdocs-material/setup/changing-the-language/


# TODO
* Hover terms linked to glossary
* Compare versions
* Changelog comments
* Convert to pdf
* Convert to json
* Policy comments on-demand