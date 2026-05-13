import os

def build_theme():
    # File Paths
    base_path = "src/base.xml"
    output_dir = "dist"
    output_file = os.path.join(output_dir, "theme.xml")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Read the core skeleton
    with open(base_path, "r", encoding="utf-8") as f:
        theme_content = f.read()

    # Advanced Component Mapping
    # These placeholders must exist in your src/base.xml
    components = {
        "{{VARIABLES}}": "src/variables.xml",
        "{{CSS}}": "src/assets/style.css",
        "{{JS}}": "src/assets/script.js",
        "{{COMP_HEADER}}": "src/components/header.xml",
        "{{COMP_FOOTER}}": "src/components/footer.xml",
        "{{COMP_SEO}}": "src/components/seo.xml",
        "{{COMP_BREADCRUMBS}}": "src/components/breadcrumbs.xml",
        "{{COMP_LOOP}}": "src/components/post-loop.xml",
        "{{COMP_POST_BODY}}": "src/components/post-body.xml",
        "{{COMP_RELATED}}": "src/components/related-posts.xml",
        "{{COMP_STATIC}}": "src/components/static-page.xml"
    }

    print("Starting build process...")

    for placeholder, file_path in components.items():
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                comp_data = f.read()
                theme_content = theme_content.replace(placeholder, comp_data)
            print(f"[OK] Injected: {placeholder}")
        else:
            # Replaces missing components with empty strings to avoid errors in Blogger
            theme_content = theme_content.replace(placeholder, "")
            print(f"[SKIP] Missing file: {file_path}")

    # Write final production file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(theme_content)
    
    print(f"\nSuccess! Final theme generated at: {output_file}")

if __name__ == "__main__":
    build_theme()
