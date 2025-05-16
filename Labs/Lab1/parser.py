import xmltodict

def parse_xml_to_json(xml_text):
    try:
        return xmltodict.parse(xml_text)
    except Exception as e:
        print(f"Error parsing XML: {e}")
        return None