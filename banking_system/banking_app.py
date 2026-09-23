class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def create_account(self, account):
        self.accounts.append(account)

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account

        return None

    def delete_account(self, account_number):
        account = self.find_account(account_number)

        if account:
            self.accounts.remove(account)
            return True

        return False

    def display_accounts(self):
        for account in self.accounts:
            print(account)