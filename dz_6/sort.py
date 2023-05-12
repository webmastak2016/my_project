import os
import re
import sys
import shutil
from pathlib import Path

file_name = Path(sys.argv[0])
base_path = Path(file_name.parent.name)
path_folder = Path(file_name.parent)
print(path_folder)


def create_folders(base_path):

    folders = ["images", "documents", "audio", "video", "archives"]
    for folder in folders:
        if os.path.exists(f'{base_path}/{folder}'):
            print("File already exist")
        else:
            (base_path / folder).mkdir(exist_ok=True)


create_folders(base_path)


def sort_files(path_folder):

    def normalize(file_norm):

        replace_values = {"а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e",
                          "ё": "e", "ж": "jz", "з": "z", "и": "i", "й": "j", "к": "k", "л": "l", "м": "m", "н": "n", "о": "o", "п": "p", "р": "r", "с": "s", "т": "t", "у": "u", "ф": "f", "х": "h", "ц": "c", "ч": "ch", "ш": "sh", "щ": "sh", "ь": "", "ъ": "", "ы": "ji", "э": "e", "ю": "ju",
                          "я": "ja", "А": "A", "Б": "B", "В": "V", "Г": "G", "Д": "D", "Е": "E", "Ё": "E", "Ж": "Jz", "З": "Z", "И": "I", "Й": "J", "К": "K", "Л": "L", "М": "M", "Н": "N", "О": "O", "П": "P", "Р": "R", "С": "S", "Т": "T", "У": "U", "Ф": "F", "Х": "H", "Ц": "C", "Ч": "Ch", "Ш": "Sh", "Щ": "Sh", "Ь": "", "Ъ": "", "Ы": "Ji", "Э": "E", "Ю": "Ju", "Я": "Ja"}

        global file_normalized
        file_normalized = re.sub('[^А-Яа-яA-Za-z0-9.]', "_", file_norm)

        for i, j in replace_values.items():
            # меняем все target_str на подставляемое
            file_normalized = file_normalized.replace(i, j)

        return file_normalized

    for el in path_folder.iterdir():

        if el.name in {'images', 'documents', 'audio', 'video', 'archives'}:
            continue

        suf_file = el.suffix
        file = el.name
        global file_norm
        file_norm = os.path.splitext(file)[0]

        if el.is_dir():
            try:
                os.rmdir(el)
            except OSError as error:
                sort_files(el)

        if suf_file in {'.jpeg', '.png', '.jpg', '.svg', '.psd'}:
            normalize(file_norm)
            new_file = file_normalized + suf_file
            os.rename(el, base_path / 'images' / new_file)
        elif suf_file in {'.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx', '.html', '.xml'}:
            normalize(file_norm)
            new_file = file_normalized + suf_file
            os.rename(el, base_path / 'documents' / new_file)
        elif suf_file in {'.mp3', '.ogg', '.wav', '.amr'}:
            normalize(file_norm)
            new_file = file_normalized + suf_file
            os.rename(el, base_path / 'audio' / new_file)
        elif suf_file in {'.avi', '.mp4', '.mov', '.mkv'}:
            normalize(file_norm)
            new_file = file_normalized + suf_file
            os.rename(el, base_path / 'video' / new_file)
        elif suf_file in {'.zip', '.gz', '.tar'}:
            normalize(file_norm)
            (base_path / 'archives' / file_normalized).mkdir(exist_ok=True)
            shutil.unpack_archive(el, base_path / 'archives' / file_normalized)
            os.remove(el)
        else:
            print(f"Unknown - {file}")
            if file == '.DS_Store':
                os.remove(el)
                print('!!!')
            else:
                continue


sort_files(path_folder)
