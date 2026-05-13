import os

def build_template():
    base_path = "src/base.xml"
    output_path = "dist/theme.xml"
    
    if not os.path.exists("dist"): os.makedirs("dist")

    with open(base_path, "r", encoding="utf-8") as f:
        content = f.read()

    mappings = {
        "{{VARIABLES}}": "src/variables.xml",
        "{{CSS}}": "src/assets/style.css",
        "{{JS}}": "src/assets/script.js",
        "{{COMP_HEADER}}": "src/components/header.xml",
        "{{COMP_FOOTER}}": "src/components/footer.xml",
        "{{COMP_LOOP}}": "src/components/post-loop.xml",
        "{{COMP_POST_BODY}}": "src/components/post-body.xml", # New: For Article Content
        "{{COMP_STATIC}}": "src/components/static-page.xml"   # New: For About/Contact
    }

    for placeholder, file_path in mappings.items():
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                content = content.replace(placeholder, f.read())

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Build Successful.")

if __name__ == "__main__":
    build_template()
