# Rename
Rename photos and screenshots to `YYMMDD_HHMMSS.ext`.

## Usage
```
pip install git+ssh://github.com/adamormondroyd/rename
```
This will install two commands:
- `rename_picture` will use the picture data to create the new name, 
use this at the end of the year on camera roll. Acts on `.jpg`, `.jpeg`,
`.png`, `.gif`, `.tiff`, and `.webp`.
- `rename_screenshots` renames macOS screenshots on the desktop, using their existing name.
Acts on all files beginning "Screenshot".
