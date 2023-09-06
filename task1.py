"""
    ---Task 1---
    Задание №6
Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
1. Соберите информацию о содержимом в виде объектов namedtuple.
2. Каждый объект хранит:
	* имя файла без расширения или название каталога,
	* расширение, если это файл,
	* флаг каталога,
	* название родительского каталога.
3. В процессе сбора сохраните данные в текстовый файл используя логирование.
"""

import os
import logging
from collections import namedtuple

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])
logging.basicConfig(filename='file_info.log', level=logging.INFO, format='%(asctime)s - %(message)s')


def collect_directory_info(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            name, extension = os.path.splitext(file)
            parent_dir = os.path.basename(root)
            file_info = FileInfo(name, extension, False, parent_dir)
            logging.info(f'File: {file_info}')

        for directory in dirs:
            parent_dir = os.path.basename(root)
            dir_info = FileInfo(directory, '', True, parent_dir)
            logging.info(f'Directory: {dir_info}')


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Collect directory information')
    parser.add_argument('directory_path', type=str, help='Path to the directory')
    args = parser.parse_args()

    collect_directory_info(args.directory_path)
