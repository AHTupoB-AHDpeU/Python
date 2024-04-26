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

    def withdrawal(self, amount: float):
        if amount <= 0:
            raise ValueError("Введите положительное число")
        if self.balance >= amount:
            self.balance -= amount
            print("Списано {} {}.".format(amount, self.rub))
            print(f"Списано {amount} {self.rub}.(f-string)")  # реализации f-string
        else:
            print("Недостаточно средств. Пополните баланс!")

try:
    wallet = Wallet("Мой кошелек 1.0", "RUB")
    print(wallet.paymentsystem)
    print("")
    wallet.balance_view()
    print("")
    wallet.deposit(100)
    print("")
    wallet.withdrawal(120)
    print("")
    wallet.deposit(50)
    print("")
    wallet.withdrawal(120)
    print("")
    wallet.balance_view()
    print("")
    wallet.delete()
except ValueError as error:
    print(error)
