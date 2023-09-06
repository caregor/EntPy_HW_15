"""
    ---Task 2_1---
Программа конвертации целого числа в шестнадцатеричную форму. Реализация выолнения программы из командной строки.
"""

import logging
import argparse


logging.basicConfig(filename='task2_1.log', level=logging.INFO, format='%(asctime)s [%(levelname)s]: %(message)s')

def decimal_to_hexadecimal(decimal):
    result = ""
    if int(decimal) == 0:
        result = "0"
    else:
        hex_chars = "0123456789ABCDEF"
        while decimal > 0:
            remainder = decimal % 16
            result = hex_chars[remainder] + result
            decimal = decimal // 16
    return '0x' + result

def main():
    parser = argparse.ArgumentParser(description='Преобразование целого числа в шестнадцатеричное представление.')
    parser.add_argument('number', help='Целое число для преобразования')
    args = parser.parse_args()

    try:
        number = args.number

        hexadecimal = decimal_to_hexadecimal(number)

        print("Шестнадцатеричное представление числа:", hexadecimal)
        print("Проверка: hex =", hex(number))

        logging.info(f"Преобразование числа {number} в шестнадцатеричное: {hexadecimal}")
        logging.info(f"Проверка: hex = {hex(number)}")

    except ValueError as e:
        print("Ошибка: Некорректный ввод. Введите целое число.")
        logging.error(f"Ошибка: {str(e)}")
    except Exception as e:
        print("Произошла ошибка во время выполнения программы.")
        logging.error(f"Ошибка: {str(e)}")

if __name__ == "__main__":
    main()
