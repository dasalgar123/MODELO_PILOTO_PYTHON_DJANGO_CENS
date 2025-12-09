import re
import os

def generate_ids_for_html(input_filepath, output_filepath):
    with open(input_filepath, 'r', encoding='utf-8') as f_in:
        content = f_in.read()

    def replace_id(match):
        tag = match.group(1)
        attrs = match.group(2)
        name_attr = match.group(3)

        # Check if 'id' attribute already exists
        if re.search(r'id="[^"]*"', attrs, re.IGNORECASE):
            # If ID exists, replace it with the name if they are different.
            # This part handles cases where IDs were malformed or not matching names.
            updated_attrs = re.sub(r'id="[^"]*"', f'id="{name_attr}"', attrs, flags=re.IGNORECASE)
        else:
            # If no ID exists, add it using the name attribute
            updated_attrs = f'{attrs} id="{name_attr}"'
        
        # Remove any leading/trailing spaces that might have been introduced during attribute manipulation.
        # This also ensures attributes are well-formed.
        updated_attrs = ' '.join(updated_attrs.split())

        return f'<{tag}{updated_attrs}>'

    # Regex to find input, select, and textarea tags with a name attribute.
    # It captures the tag name, all its attributes, and the value of the name attribute.
    # It's made to handle existing id attributes as well for replacement.
    modified_content = re.sub(r'<(input|select|textarea)(\s+[^>]*?)name="([^"]*)"([^>]*?)>', replace_id, content, flags=re.IGNORECASE)

    with open(output_filepath, 'w', encoding='utf-8') as f_out:
        f_out.write(modified_content)

    print(f"Nuevo archivo HTML con IDs generados guardado en: {output_filepath}")

if __name__ == "__main__":
    # Use absolute paths to avoid issues with current working directory
    base_dir = r'C:\Users\ANDRES\Desktop\la miel'
    input_html_file = os.path.join(base_dir, 'app\templates\subestacion\S30_LA_MIEL\s30_la_miel.html')
    output_html_file = os.path.join(base_dir, 'app\templates\subestacion\S30_LA_MIEL\s30_la_miel_with_generated_ids.html')
    
    generate_ids_for_html(input_html_file, output_html_file)
