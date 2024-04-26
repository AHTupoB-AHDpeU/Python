class Wallet:
    paymentsystem = "Мой Кошелёк 1.0"
    def __init__(self, name: str, rub: str):
        self.name = name

        if rub not in ["RUB"]:
            raise ValueError("Доступна только валюта RUB")

        self.rub = rub
        self.balance = 0

    def balance_view(self):
        print("Баланс: {} {}".format(self.balance, self.rub))

    def delete(self):
        print("Кошелёк {} закрыт!".format(self.name))
        del self

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Введите положительное число")
        self.balance += amount

        print("Кошелёк пополнен на {} {}.".format(amount, self.rub))
        print(f"Кошелёк пополнен на {amount} {self.rub}.(f-string)")  # реализации f-string
        self.balance_view()

    def withdrawal(self, amount: float):
        while self.balance < amount:
            print("Недостаточно средств. Пополните баланс!")
            self.deposit(float(input("На какую сумму хотите пополнить: ")))

        self.balance -= amount

        print("Списано {} {}.".format(amount, self.rub))
        print(f"Списано {amount} {self.rub}.(f-string)")  # реализации f-string

try:
    wallet = Wallet("Мой кошелек 1.0", "RUB")
    print(wallet.paymentsystem)
    print("")
    wallet.balance_view()
    print("")
    wallet.withdrawal(int(input("Цена товара: ")))
    print("")
    wallet.balance_view()
    print("")
    wallet.delete()
except ValueError as error:
    print(error)
