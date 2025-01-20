import shutil, os
from blockutils import markdown_to_blocks, block_to_block_type, strip_markdown
from blockutils import markdown_to_html_node 

# Wrappers for external interaction so that Mocks/Fakes can be injected
# E.g., in your test class define a fake_file_copy and then in your test function do: 
#    global file_copy = fake_file_copy
# before calling copy_clean
path_exists = os.path.exists
listdir = os.listdir
path_isfile = os.path.isfile
mkdir = os.mkdir
file_copy = shutil.copy
rm_tree = shutil.rmtree

def copy_clean(source_folder, target_folder, verbose = True):
    if path_exists(target_folder):
        if(verbose):
            print(f"Deleting old folder {target_entry}")
        rm_tree(target_folder)
    if(verbose):
        print(f"Creating folder {target_entry}")
    mkdir(target_folder)
    for entry in listdir(source_folder):
        source_entry = os.path.join(source_folder, entry)
        target_entry = os.path.join(target_folder, entry)
        if path_isfile(source_entry):
            if(verbose):
                print(f"Copying file {source_entry} to {target_entry}")
            file_copy(source_entry, target_entry)
        else:
            if(verbose):
                print(f"Copying dir {source_entry} to {target_entry}")
            copy_clean(source_entry, target_entry)

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        if("h1" == block_type):
            return strip_markdown(block, block_type)
    raise Exception("Page Title (h1) not found")

def recursive_mkdir(dest_path):
    if(path_exists(dest_path)) or ("" == dest_path):
            return
    if path_exists(os.path.dirname(dest_path)):
        mkdir(dest_path)
    else:
        if dest_path == os.path.dirname(dest_path):
            raise Exception(f"path '{dest_path}' cannot be created") # E.g., on Windows the path is on a drive that doesn't exist
        recursive_mkdir(os.path.dirname(dest_path))

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as file:
        markdown = file.read()
    with open(template_path) as file:
        template = file.read()
    content = (markdown_to_html_node(markdown)).to_html
    title = extract_title(markdown)
    generated = (template.replace("\{\{ Title \}\}", title)).replace("\{\{ Content \}\}", content)
    recursive_mkdir(os.path.dirname(dest_path))
    with open(dest_path) as file:
        file.write(generated)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, verbose = True):
    recursive_mkdir(dest_dir_path)
    for entry in listdir(dir_path_content):
        source_entry = os.path.join(dir_path_content, entry)
        target_entry = os.path.join(dest_dir_path, entry)
        if path_isfile(source_entry):
            if(verbose):
                print(f"Generating {target_entry} from {source_entry} and {template_path}")
            generate_page(source_entry, template_path, target_entry)
        else:
            if(verbose):
                print(f"Generating dir {source_entry}")
            generate_pages_recursive(source_entry, template_path, target_entry)

        

