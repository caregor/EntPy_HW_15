"""
    ---Task 2---
 Программа банкомат.
Возьмите любые 1-3 задания из прошлых домашних заданий. Добавьте к ним логирование
ошибок и полезной информации. Также реализуйте возможность запуска из командной
строки с передачей параметров.
"""

import logging

logging.basicConfig(filename='task2.log', level=logging.INFO, format='%(asctime)s [%(levelname)s]: %(message)s')


def calculate_withdrawal_fee(amount):
    fee = amount * 0.015
    fee = max(fee, 30)
    fee = min(fee, 600)
    return fee


def calculate_tax(amount):
    tax = amount * 0.1
    return tax


balance = 0
operations_count = 0

while True:
    print("Текущий баланс:", balance)

    action = input("Выберите действие:\n - 1 -- пополнить;\n - 2 -- снять;\n - 3 -- выйти;\n")

    if action == '1':
        deposit = int(input("Введите сумму для пополнения (кратно 50): "))
        if deposit % 50 == 0:
            balance += deposit
            operations_count += 1
            if operations_count % 3 == 0:
                interest = balance * 0.03
                balance += interest
                logging.info(f"Начисление процентов за лояльность: {interest}")
        else:
            print("Ошибка: Сумма пополнения должна быть кратна 50.")
            logging.error("Ошибка: Сумма пополнения должна быть кратна 50.")

    elif action == '2':
        withdrawal = int(input("Введите сумму для снятия (кратно 50): "))
        if withdrawal % 50 == 0:
            if withdrawal <= balance:
                fee = calculate_withdrawal_fee(withdrawal)
                print("Комиссия за операцию:", fee)
                balance -= withdrawal
                balance -= fee
                operations_count += 1
                if operations_count % 3 == 0:
                    interest = balance * 0.03
                    print("Начисление за лояльность к банку:", interest)
                    balance += interest
                    logging.info(f"Начисление процентов за лояльность: {interest}")
            else:
                print("Ошибка: Недостаточно средств на счете.")
                logging.error("Ошибка: Недостаточно средств на счете.")
        else:
            print("Ошибка: Сумма снятия должна быть кратна 50.")
            logging.error("Ошибка: Сумма снятия должна быть кратна 50.")

    elif action == '3':
        if balance > 5000000:
            tax = calculate_tax(balance)
            balance -= tax
            print("Удержан налог на богатство 10%")
            logging.info(f"Удержан налог на богатство: {tax}")
        break

    else:
        print("Ошибка: Неверное действие.")
        logging.error("Ошибка: Неверное действие.")

print("Баланс:", balance)
