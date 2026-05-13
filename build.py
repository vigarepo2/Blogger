import os

def build_template():
    base_path = "src/base.xml"
    output_path = "dist/theme.xml"
    
    if not os.path.exists("dist"):
        os.makedirs("dist")

    with open(base_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Mapping placeholders to files
    mappings = {
        "{{VARIABLES}}": "src/variables.xml",
        "{{CSS}}": "src/assets/style.css",
        "{{JS}}": "src/assets/script.js",
        "{{COMP_HEADER}}": "src/components/header.xml",
        "{{COMP_FOOTER}}": "src/components/footer.xml",
        "{{COMP_LOOP}}": "src/components/post-loop.xml"
    }

    for placeholder, file_path in mappings.items():
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                content = content.replace(placeholder, f.read())

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Build Successful: dist/theme.xml created.")

if __name__ == "__main__":
    build_template()
