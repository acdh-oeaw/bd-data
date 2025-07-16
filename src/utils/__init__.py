def remove_tei_ns(file: str) -> str:
    """
    Remove TEI namespace declaration from an XML file.

    Reads a TEI XML file, removes the xmlns="http://www.tei-c.org/ns/1.0"
    namespace declaration, and writes the modified content back to the same file.

    Args:
        file (str): Path to the TEI XML file to process.

    Returns:
        str: The path to the processed file (same as input).
    """
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    content = content.replace('xmlns="http://www.tei-c.org/ns/1.0"', "")

    with open(file, "w", encoding="utf-8") as f:
        f.write(content)
    return file
