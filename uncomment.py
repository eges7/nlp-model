def remove_comments_from_file(input_file_path, output_file_path):
    with open(input_file_path, 'r') as file:
        lines = file.readlines()
    
    cleaned_lines = []
    for line in lines:
        stripped_line = line.strip()
        if not stripped_line.startswith('#') and not stripped_line.startswith('"""') and not stripped_line.startswith("'''"):
            cleaned_lines.append(line)
        elif stripped_line.startswith('"""') or stripped_line.startswith("'''"):
            # Skip multi-line comment blocks
            if stripped_line.count('"""') == 2 or stripped_line.count("'''") == 2:
                continue
            else:
                while True:
                    line = next(lines)
                    if '"""' in line or "'''" in line:
                        break
    
    with open(output_file_path, 'w') as file:
        file.writelines(cleaned_lines)

# Kullanım örneği:
input_file_path = 'main copy.py'  # Yorumları kaldırmak istediğiniz dosya
output_file_path = 'output.py'  # Temizlenmiş içeriği yazmak istediğiniz dosya

remove_comments_from_file(input_file_path, output_file_path)