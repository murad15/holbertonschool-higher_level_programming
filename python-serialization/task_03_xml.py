#!/usr/bin/env python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.

    :param dictionary: Python dictionary to serialize
    :param filename: Output XML filename
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)

def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    result = {}

    for child in root:
        text = child.text

        if text is not None:
            # Convert to int if possible
            if text.isdigit():
                value = int(text)
            else:
                # Convert to float if possible
                try:
                    value = float(text)
                except ValueError:
                    value = text
        else:
            value = None

        result[child.tag] = value

    return result

