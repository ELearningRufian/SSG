from websiteutils import copy_clean, generate_pages_recursive

def main():
    copy_clean("static", "public")
    generate_pages_recursive("content", "template.html", "public")

if __name__ == "__main__":
    main()
