# SVG Parser

A Python script that parses SVG strings and displays all elements in a hierarchical structure.

## Features

- Accepts raw SVG strings as command-line arguments
- Uses `xml.etree.ElementTree` for XML parsing
- Displays all SVG elements with their attributes
- Handles XML namespaces properly
- Provides clear error messages for invalid input

## Usage

### Method 1: Command-line Argument (Unix/Linux/Mac)

```bash
python svgparse.py '<svg_string>'
```

Or make it executable and run directly:

```bash
chmod +x svgparse.py
./svgparse.py '<svg_string>'
```

### Method 2: Stdin Input (Recommended for Windows)

Due to Windows Command Prompt limitations with `<` and `>` characters, using stdin is recommended:

**From a file:**
```bash
python svgparse.py < input.svg
```

**From piped input (simple SVG only):**
```bash
echo ^<svg^>^<rect width="100" height="100"/^>^</svg^> | python svgparse.py
```
Note: Echo with escaped characters only works reliably for simple SVG. For complex SVG with many attributes or special characters, use file redirection instead.

**Using the Windows batch file:**
```cmd
svgparse.bat input.svg
```

## Examples

### Simple Circle (Unix/Linux/Mac)

```bash
python svgparse.py '<svg xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="40"/></svg>'
```

### Simple Circle (Windows)

```cmd
echo ^<svg xmlns="http://www.w3.org/2000/svg"^>^<circle cx="50" cy="50" r="40"/^>^</svg^> | python svgparse.py
```

Or save to a file and use:
```cmd
python svgparse.py < circle.svg
```

Output:
```
SVG Elements Found:
==================================================
<svg>
  <circle>
    cx="50"
    cy="50"
    r="40"
==================================================

Successfully parsed SVG with root element: svg
```

### Nested Elements

```bash
python svgparse.py '<svg><g id="group1"><rect x="10" y="10" width="30" height="30"/></g></svg>'
```

Output:
```
SVG Elements Found:
==================================================
<svg>
  <g>
    id="group1"
    <rect>
      x="10"
      y="10"
      width="30"
      height="30"
==================================================

Successfully parsed SVG with root element: svg
```

### Path Element

```bash
python svgparse.py '<svg><path d="M10 10 L90 90" stroke="black"/></svg>'
```

Output:
```
SVG Elements Found:
==================================================
<svg>
  <path>
    d="M10 10 L90 90"
    stroke="black"
==================================================

Successfully parsed SVG with root element: svg
```

## Error Handling

The script provides clear error messages for invalid input:

```bash
python svgparse.py '<svg><invalid'
```

Or on Windows:
```cmd
echo ^<svg^>^<invalid | python svgparse.py
```

Output:
```
Error: Failed to parse SVG: unclosed token: line 1, column 5
```

## Windows Command Prompt Note

Windows CMD interprets `<` and `>` as redirect operators, which can cause errors like:
```
< was unexpected at this time.
```

**Solutions:**
1. **Use stdin with file redirection (Recommended):** `python svgparse.py < file.svg`
2. **Use piped input with escaped characters:** `echo ^<svg^>...^</svg^> | python svgparse.py` (Note: This only works for simple SVG strings)
3. **Use the provided batch file with a file:** `svgparse.bat file.svg`
4. **Use PowerShell (Better quote handling):**
   ```powershell
   python svgparse.py '<svg xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="40"/></svg>'
   ```
   PowerShell handles quoted strings with `<` and `>` characters more reliably than CMD.

## Requirements

- Python 3.x
- No external dependencies (uses only standard library)

## License

This project is open source and available for use.
