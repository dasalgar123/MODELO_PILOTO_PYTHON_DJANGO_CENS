import re
import os

def extract_ids_from_html(filepath):
    ids = []
    with open(filepath, 'r', encoding='utf-8') as f:
        html_content = f.read()
        # Find ids for input, select, and textarea elements
        # This regex is more specific to avoid capturing ids from other tags inadvertently
        matches = re.findall(r'<(?:input|select|textarea)[^>]*?id="([^"]*)"', html_content, re.IGNORECASE)
        ids.extend(matches)
    return sorted(list(set(ids))) # Return unique and sorted IDs

if __name__ == "__main__":
    html_file = 'app/templates/subestacion/S30_LA_MIEL/s30_la_miel.html'
    output_file = 'html_ids_s30_la_miel.txt'

    # Ensure the script is run from the correct directory or adjust paths
    # For this example, assuming the script is in the root of the project
    # and html_file is relative to it.
    script_dir = os.path.dirname(__file__)
    html_file_path = os.path.join(script_dir, html_file)
    output_file_path = os.path.join(script_dir, output_file)

    extracted_ids = extract_ids_from_html(html_file_path)

    with open(output_file_path, 'w', encoding='utf-8') as f:
        for element_id in extracted_ids:
            f.write(element_id + '\n')
    print(f"IDs extraídos guardados en '{output_file}'")
