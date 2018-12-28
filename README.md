# Tableau Tools

Small Tableau-related tools and utilities. All are MIT-licensed.

## Thumb Dumper

A small Python script that extracts all the thumbnails from a Tableau workbook in `.twb` or `.twbx` format. Creates a directory named the same as the workbook for the files. The resulting images are PNGs (directly dumped from the workbook), generally 192x192 in size. Some worksheets create smaller and non-square thumbnails, though.

Usage:
```
python thumbdumper.py filename.twbx
```
