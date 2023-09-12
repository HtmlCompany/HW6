from pathlib import Path
import sys

CATEGORIES = {'Archives': ['.rar', '.zip', '.gz', '.tar'], 
              'Audio': ['.mp3', '.ogg', '.wav', '.amr'],
              'Video': ['.avi', '.mp4', '.mov', '.mkv'],
              'Documents': ['.doc', '.docx', '.txt', '.pdf', '.xls', '.xlsx', '.pptx', '.odt', '.ods'],
              'Images': ['.jpeg', '.png', '.jpg', '.gif']}


def get_categories(file:Path) -> str:
    ext = file.suffix.lower()
    for cats, exts in CATEGORIES.items():
        if ext in exts:
            return cats
    return "Else"

def move_file(file:Path, category:str, root_dir:Path) -> None:
    target_dir = root_dir.joinpath(category)
    if not target_dir.exists():
        target_dir.mkdir()
    file.replace(target_dir.joinpath(file.name))

def sort_folder(path:Path) -> None:
    for item in path.glob("**/*"):
        if item.is_file():
            category = get_categories(item)
            move_file(item, category, path)

def main() -> str:
    try:
        path = Path(sys.argv[1])
    except IndexError:
        return "This is not a path"
    
    if not path.exists():
        return "No path to folder"
    
    sort_folder(path)
    
    return "All right"

if __name__ == '__main__':
    print(main())