from datetime import datetime
import os
import csv


class Transaction:
    # __list_transactions: list['Transaction'] = []
    __list_transactions = []

    def __init__(self, category: str, amount: int, description: str) -> None:
        self.id: int = self.get_id()
        self.category: str = category
        self.amount: int = amount
        self.description: str = description
        # self.date: datetime = datetime.now().strftime('%Y-%h-%d %H:%M:%S')
        self.date = datetime.now().strftime('%Y-%h-%d %H:%M:%S')
        self.add_transaction(self)

    @classmethod
    def get_id(cls) -> int:
        if not cls.__list_transactions:
            return 1
        return cls.__list_transactions[-1].id + 1

    @classmethod
    def add_transaction(cls, transaction: 'Transaction') -> None:
        print('transaction: ', transaction.id, transaction.date, transaction.category, transaction.amount,
              transaction.description)
        cls.__list_transactions.append(transaction)
        print('Транзакция добавлена в __list_transactions = []')
        # Передаю на запись в фаил CSV
        # x = Stream()
        # x.write(transaction)
        stream.write(transaction)

    @classmethod
    def get_list_transactions(cls):
        return cls.__list_transactions

    @classmethod
    # def append(cls, transactions: list[dict]) -> None:
    def append(cls, transactions) -> None:
        pass

    @classmethod
    def show_balance(cls) -> dict:
        '''
        тестово получает all_transaction_tuple из метода Stream.read()

        Получает доходы из show_income, расходы из show_expense,
        высчитывает баланс
        :return: Баланс
        '''
        transactions = stream.read()
        incomes = []
        expenses = []
        total = {}
        for rows in transactions:
            # Вычисляю Доход
            if rows[2] == '+':
                incomes.append(int(rows[3]))
            # Вычисляю Расход
            elif rows[2] == '-':
                expenses.append(int(rows[3]))
        # Сформировал словарь total {'incomes ': ?, 'expenses ': ?, 'balance ': ?}
        total['incomes'] = sum(incomes)
        total['expenses'] = sum(expenses)
        total['balance'] = sum(incomes) - sum(expenses)
        return total

    @classmethod
    def show_income(cls) -> int:
        '''
        Я уберу методы show_expense & show_income, зачем несколько раз читать csv
            Вывод расходов.
            Прочитаю сохраненный csv (Stream read),
            отсортирую расходы.
        '''
        pass

    @classmethod
    def show_expense(cls) -> int:
        '''
        Я уберу методы show_expense & show_income, зачем несколько раз читать csv
        '''
        pass

    @classmethod
    def update(cls, pk: int) -> 'Transaction':
        """
            Ищет среди list_transactions экз. класса
            Transaction с переданным id и редактирует его в списке.
            После изменения возаращает этот экз класса
        """
        pass

    @classmethod
    # def search(cls, field: str, condition: str) -> list['Transaction']:
    def search(cls, field: str, condition: str):
        """
        Ищет нужные записи среди list_transactions
        :param field: поле по которому осуществляется поиск
        :param condition: условие
        :return: список с транзакциями, которые удоволетворяют условию
        """

    @classmethod
    # def list(cls, transactions: list['Transaction'] = None) -> None:
    def list(cls, transactions) -> None:
        if not transactions:
            transactions = cls.__list_transactions
        for transaction in transactions:
            print(transaction)

    def __repr__(self):
        return f'{self.id}. {self.amount}'


class Stream:
    path_folder = 'wallet'
    file_name = 'wallet_data.csv'
    # В этот список прочитаю csv и переверну его в tuple all_transaction_tuple
    rows = []
    # кортеж с транзакциями
    all_transaction_tuple = tuple(rows)

    def __init__(self) -> None:
        self.__initialization()

    def __initialization(self):
        """ Содает папку и файл """
        # Проверяю и в случае отсутствия создаю директорию "path_folder"
        if not os.path.exists(self.path_folder):
            os.mkdir(self.path_folder)

    # def read(self) -> list[dict]:
    def read(self):
        '''
            Читаю в переменную transactions
            :return: transactions
        '''
        # Читаю сохраненный csv
        with open(f"{self.path_folder}/{self.file_name}", newline="") as file:
            reader = csv.reader(file)
            transactions = []
            for row in reader:
                transactions.append(row)
            print('[!] read сформировала transactions')
            return transactions


            #     # Подстчитываю сумму дохода +
            #     if row[1] == '+':
            #         self.incomes.append(int(row[2]))
            #         incomes_total = sum(self.incomes)
            #
            #     # Подсчитываю сумму расхода -
            #     else:
            #         self.expenses.append(int(row[2]))
            #         expenses_total = sum(self.expenses)
            # # Баланс получил
            # balance = incomes_total - expenses_total


        pass

    def write(self, transaction: 'Transaction') -> None:
        '''
            Запись в фаил
            :param transaction:
        '''
        # Создание директории
        self.__initialization()

        ALL_DATE_CSV = []

        # Собранные данные сохраняю в переменную ALL_DATE_CSV для  записи в csv
        ALL_DATE_CSV.append(
            [
                transaction.id,
                transaction.date,
                transaction.category,
                transaction.amount,
                transaction.description,
            ]
        )
        # Записываю csv file
        with open(f"{self.path_folder}/{self.file_name}", "a") as file:
            writer = csv.writer(file)
            # # Заголовки
            # writer.writerow(
            #     (
            #         "id"
            #         "datetime",
            #         "category",
            #         "amount",
            #         "description"
            #     )
            # )
            writer.writerows(ALL_DATE_CSV)
        print('Транзакция записана в csv')

        pass

    @staticmethod
    # def change(transactions: list['Transaction']) -> None:
    def change(transactions) -> None:
        """
        Перезапишет файл csv на основе списка transactions
        :param transactions: это list_transactions (нужно будет передать)
        """


stream = Stream()

MENU_LIST = [
    '1. Вывод баланса',
    '2. Добавление транзакции',
    '3. Редактирование транзакции',
    '4. Поиск по транзакции',
    f'5. Выход\n{10 * "-"}\n',
]
FILTER_BY_LIST = [
    '1. По дате',
    '2. По сумме',
    '3. По категории',
]

if __name__ == '__main__':
    # Transaction.append(stream.read())
    while True:
        print('Привет, это программа финансовый кошелек')
        print('Выбери нужный пукт меню:')
        for item in MENU_LIST:
            print(item)
        choice = input('Выберите пункт меню:')
        if choice == '1':
            print('Раздел:', MENU_LIST[int(choice) - 1])
            # Transaction.show_income()
            # Transaction.show_expense()
            total = Transaction.show_balance()
            print(f"\tДоход: {total['incomes']} руб.")
            print(f"\tРасход: {total['expenses']} руб.")
            print(f"Баланс: {total['balance']} руб.")


        # 2. Добавление транзакции
        elif choice == '2':
            print('Раздел:', MENU_LIST[int(choice) - 1])
            category = input('Выбери: \n + если Доход | - если Расход: ')
            amount = int(input('Цифрами впиши сумму НУЖНА ВАЛИДАЦИЯ!'))
            description = input('Добавь описание: ')
            transaction = Transaction(category, amount, description)

        elif choice == '3':
            Transaction.list()
            pk_transaction = int(input("Введите id транзакции, которую хотите изменить: "))
            Transaction.update(pk_transaction)
            Stream.change(Transaction.get_list_transactions())

        # 4. Поиск по транзакции
        elif choice == '4':
            print('Раздел:', MENU_LIST[int(choice) - 1])
            for item in FILTER_BY_LIST:
                print(item)
            filter_by = input("Введите условие поиска: ")
            transactions = []
            # 1. Поиск По дате
            if filter_by == '1':
                print('Раздел Поиск По дате:')
                filter_date = input("Введите дату в формате (день.месяц.год): ")
                transactions = Transaction.search('date', filter_date)
                '''
                Нужно изменить формат написания даты 2024-May-11 01:48:46
                Нумерацию тоже

                '''


            # 2. Поиск По сумме
            elif filter_by == '2':
                filter_amount = input("Введите нужную сумму: ")
                transactions = Transaction.search('amount', filter_amount)
            # 3. Поиск По категории
            elif filter_by == '3':
                filter_category = input("Введите нужную категорию: ")
                transactions = Transaction.search('category', filter_category)
            Transaction.list(transactions)
        elif choice == '5':
            break

# Тестирую приходит хоть что-то в метод write
# x = Transaction().show_income()
# print(x)

