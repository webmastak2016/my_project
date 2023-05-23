import os
import re
import sys
import shutil
from pathlib import Path


def create_folders(base_path):
    folders = ["images", "documents", "audio", "video", "archives"]
    for folder in folders:
        folder_path = base_path / folder
        folder_path.mkdir(exist_ok=True)
        print(f"Created folder: {folder_path}")


def normalize_filename(filename):
    replace_values = {
        "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "ё": "e", "ж": "jz", "з": "z",
        "и": "i", "й": "j", "к": "k", "л": "l", "м": "m", "н": "n", "о": "o", "п": "p", "р": "r",
        "с": "s", "т": "t", "у": "u", "ф": "f", "х": "h", "ц": "c", "ч": "ch", "ш": "sh", "щ": "sh",
        "ь": "", "ъ": "", "ы": "ji", "э": "e", "ю": "ju", "я": "ja",
        "А": "A", "Б": "B", "В": "V", "Г": "G", "Д": "D", "Е": "E", "Ё": "E", "Ж": "Jz", "З": "Z",
        "И": "I", "Й": "J", "К": "K", "Л": "L", "М": "M", "Н": "N", "О": "O", "П": "P", "Р": "R",
        "С": "S", "Т": "T", "У": "U", "Ф": "F", "Х": "H", "Ц": "C", "Ч": "Ch", "Ш": "Sh", "Щ": "Sh",
        "Ь": "", "Ъ": "", "Ы": "Ji", "Э": "E", "Ю": "Ju", "Я": "Ja"
    }

    normalized = re.sub(r'[^А-Яа-яA-Za-z0-9.]', "_", filename)

    for target_str, replace_str in replace_values.items():
        normalized = normalized.replace(target_str, replace_str)

    return normalized


def sort_files(path_folder):
    for item in path_folder.iterdir():
        if item.name in {'images', 'documents', 'audio', 'video', 'archives'}:
            continue

        if item.is_dir():
            try:
                os.rmdir(item)
                print(f"Removed empty folder: {item}")
            except OSError:
                sort_files(item)
        else:
            filename = item.name
            suffix = item.suffix.lower()

            if suffix in {'.jpeg', '.png', '.jpg', '.svg', '.psd'}:
                folder = 'images'
            elif suffix in {'.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx', '.html', '.xml'}:
                folder = 'documents'
            elif suffix in {'.mp3', '.ogg', '.wav', '.amr'}:
                folder = 'audio'
            elif suffix in {'.avi', '.mp4', '.mov', '.mkv'}:
                folder = 'video'
            elif suffix in {'.zip', '.gz', '.tar'}:
                folder = 'archives'
                (path_folder / folder / filename).mkdir(exist_ok=True)
                shutil.unpack_archive(item, path_folder / folder / filename)
                os.remove(item)
                print(f"Extracted archive: {item}")
                continue
            else:
                print(f"Unknown file: {filename}")
                if filename == '.DS_Store':
                    os.remove(item)
                    print(f"Removed file: {item}")
                continue

            normalized_filename = normalize_filename(
                os.path.splitext(filename)[0])
            new_file = normalized_filename + suffix
            new_path = path_folder / folder / new_file
            os.rename(item, new_path)
            print(f"Moved file to {folder}: {item} -> {new_path}")


def main():
    if len(sys.argv) != 2:
        print("Usage: clean-folder <folder_path>")
        sys.exit(1)

    folder_path = Path(sys.argv[1])
    create_folders(folder_path)
    sort_files(folder_path)


if __name__ == '__main__':
    main()
