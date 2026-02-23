# TypMan

TypMan is a Python utility for managing and compiling Typst documents into PDFs. It reads project configuration from a JSON file, handles fonts, and provides a simple interactive menu for compilation.

## Features

- Load project configuration from a typ_proj_config.json file.
- Compile Typst documents to PDF and possibly more in the future



## Installation and usage

Make sure you have Python 3.8+ installed. Run the python script from the project root. This will open an interactive menu.




## Configuration

Create a typ_proj_config.json file in your project root:
``` json
{
  "documentPath": "path/to/your/document.typ",
  "fonts": "path/to/custom/fonts",
  "name": "theOutputNameOfTheDocument",
  "root": "optional/root/path"
}
```
