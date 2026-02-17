# SVG Parser

A Python script that parses SVG strings and displays all elements in a hierarchical structure.

## Features

- Accepts raw SVG strings as command-line arguments
- Uses `xml.etree.ElementTree` for XML parsing
- Displays all SVG elements with their attributes
- Handles XML namespaces properly
- Provides clear error messages for invalid input

## Usage

```bash
python svgparse.py '<svg_string>'
```

Or make it executable and run directly:

```bash
chmod +x svgparse.py
./svgparse.py '<svg_string>'
```

## Examples

### Simple Circle

```bash
python svgparse.py '<svg xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="40"/></svg>'
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

Output:
```
Error: Failed to parse SVG: unclosed token: line 1, column 5
```

## Requirements

- Python 3.x
- No external dependencies (uses only standard library)

## License

This project is open source and available for use.
