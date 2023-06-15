class Bank():

    client = input('Введите имя клиента: ')

    def open_bank_account(self):
        opened_bank_accounts = self.gather_opened_accounts()
        if opened_bank_accounts:
            s = self.check_if_client_exists(opened_bank_accounts)
            if s:
                print('Клиент уже существует')
                return
            else:
                already_opened_bank_accounts = [s.split("-") for s in opened_bank_accounts]
                new_bank_account_number = int(already_opened_bank_accounts[len(already_opened_bank_accounts) - 1][1]) + 1
        else:
            new_bank_account_number = 1

        money = input('Сколько денег вы хотели положить на новый счет ')
        account_data = f"{self.client}-{new_bank_account_number}-{money}\n"
        opened_bank_accounts.append(account_data)

        self.write_refreshed_data(opened_bank_accounts)

        return account_data

    def check_if_client_exists(self, already_opened_bank_accounts, result = 'check', client=None):
        if not client:
            r = [x for x in already_opened_bank_accounts if x.split("-")[0] == self.client]
        else:
            r = [x for x in already_opened_bank_accounts if x.split("-")[0] == client]
        if result == 'check':
            if r:
                return True
            else:
                return False
        elif result == 'account':
            if r:
                return r[0]

    def gather_opened_accounts(self):
        with open('bank_file.txt', 'r', encoding='utf-8') as bf:
            opened_bank_accounts = bf.readlines()
            bf.close()
        return opened_bank_accounts

    def make_transaction(self):
        opened_bank_accounts = self.gather_opened_accounts()
        if opened_bank_accounts:
            get_my_account = self.check_if_client_exists(opened_bank_accounts, result = 'account')
            if get_my_account:
                my_account_name = get_my_account.split("-")[0]
                money_account = int(get_my_account.split("-")[-1:][0].replace("\n", ""))
                tr_client = input("Введите имя человека, которому переведете деньги")

                transaction_client = self.check_if_client_exists(opened_bank_accounts,
                                                                 result = 'account',
                                                                 client=tr_client)
                if transaction_client:
                    transaction_client_money = int(transaction_client.split("-")[-1:][0].replace("\n", ""))
                    amount = int(input("Сколько денег вы бы хотели перевести "))
                    if amount > money_account:
                        print('Недостаточно средств на вашем счету')
                        return
                    else:
                        money_account -= amount
                        transaction_client_money += amount
                        refreshed_accounts = []
                        for r in opened_bank_accounts:
                            acc_name = r.split('-')[0]
                            if acc_name == tr_client:
                                s = r.split('-')
                                s[-1] = str(transaction_client_money) + '\n'
                                s = "-".join(s)
                                refreshed_accounts.append(s)
                            elif acc_name == my_account_name:
                                s = r.split('-')
                                s[-1] = str(money_account) + '\n'
                                s = "-".join(s)
                                refreshed_accounts.append(s)
                            else:
                                refreshed_accounts.append(r)
                        self.write_refreshed_data(refreshed_accounts)
                else:
                    print("Клиента, котрому вы собираетесь перевести не существует")
                    return
            else:
                print('Такого клиента не существует, сначала создайте счет')

        return

    def write_refreshed_data(self, opened_bank_accounts):
        with open('bank_file.txt', 'w', encoding='utf-8') as r:
            r.writelines(opened_bank_accounts)
            r.close()


Bank().open_bank_account()
Bank().make_transaction()