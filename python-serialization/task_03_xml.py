#!/usr/bin/env python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into an XML file.
    """
    # Create the root element <data>
    root = ET.Element("data")

    # Iterate through dictionary items and create child elements
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)  # Ensure value is a string for XML

    # Create the tree and write to the file
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)

def deserialize_from_xml(filename):
    """
    Reads an XML file and reconstructs it into a Python dictionary.
    """
    try:
        # Parse the XML file
        tree = ET.parse(filename)
        root = tree.getroot()

        # Reconstruct the dictionary
        # Note: All values will be returned as strings
        deserialized_dict = {}
        for child in root:
            deserialized_dict[child.tag] = child.text
            
        return deserialized_dict

    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return None
    except ET.ParseError:
        print(f"Error: Failed to parse {filename}.")
        return None
