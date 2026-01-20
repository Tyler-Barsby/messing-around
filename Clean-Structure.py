import os

def get_target_folders(md_file):
    targets = []
    if not os.path.exists(md_file):
        return targets

    with open(md_file, 'r') as f:
        for line in f:
            clean_line = line.strip().lstrip('* ').lstrip('- ').strip()
            if clean_line and not clean_line.startswith('#'):
                targets.append(clean_line)
    return targets

def clean_files_in_targets(md_config):
    target_folders = get_target_folders(md_config)
    
    for folder in target_folders:
        if os.path.isdir(folder):
            for root, dirs, files in os.walk(folder):
                for filename in files:
                    old_path = os.path.join(root, filename)
                    name, ext = os.path.splitext(filename)
                    new_name = name.title().replace(" ", "-") + ext
                    new_path = os.path.join(root, new_name)
                    
                    if old_path != new_path:
                        try:
                            os.rename(old_path, new_path)
                        except OSError:
                            pass

if __name__ == "__main__":
    clean_files_in_targets("folders.md")