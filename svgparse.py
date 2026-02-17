#!/usr/bin/env python3
"""
SVG Parser Script

This script accepts a raw SVG string as a command-line argument,
parses it using xml.etree.ElementTree, and finds all SVG elements.
"""

import sys
import xml.etree.ElementTree as ET


def strip_namespace(tag):
    """
    Remove XML namespace from tag name.
    
    Args:
        tag (str): Tag name possibly containing namespace
        
    Returns:
        str: Tag name without namespace
    """
    if '}' in tag:
        return tag.split('}')[1]
    return tag


def parse_svg(svg_string):
    """
    Parse an SVG string and find all elements.
    
    Args:
        svg_string (str): Raw SVG string to parse
        
    Returns:
        ET.Element: Root element of the parsed SVG
        
    Raises:
        ET.ParseError: If the SVG string is invalid XML
    """
    try:
        root = ET.fromstring(svg_string)
        return root
    except ET.ParseError as e:
        raise ET.ParseError(f"Failed to parse SVG: {e}") from e


def display_element_tree(root, prefix=""):
    """
    Recursively display all elements in the SVG tree.
    
    Args:
        root (ET.Element): Root or current element to process
        prefix (str): Indentation prefix for hierarchical display
    """
    # Get the tag name, removing namespace if present
    tag = strip_namespace(root.tag)
    
    # Display the element
    print(f"{prefix}<{tag}>")
    
    # Display attributes if any
    if root.attrib:
        for key, value in root.attrib.items():
            attr_key = strip_namespace(key)
            print(f"{prefix}  {attr_key}=\"{value}\"")
    
    # Recursively process children
    for child in root:
        display_element_tree(child, prefix + "  ")


def main():
    """Main function to handle command-line argument and parse SVG."""
    if len(sys.argv) < 2:
        print("Usage: python svgparse.py '<svg_string>'", file=sys.stderr)
        print("\nExample:", file=sys.stderr)
        print('  python svgparse.py \'<svg xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="40"/></svg>\'', file=sys.stderr)
        sys.exit(1)
    
    svg_string = sys.argv[1]
    
    try:
        root = parse_svg(svg_string)
        print("SVG Elements Found:")
        print("=" * 50)
        display_element_tree(root)
        print("=" * 50)
        # Extract tag name without namespace for clearer output
        tag_name = strip_namespace(root.tag)
        print(f"\nSuccessfully parsed SVG with root element: {tag_name}")
    except ET.ParseError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
