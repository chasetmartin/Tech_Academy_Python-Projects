from django.db import models


# Create the account model
class Account(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    initial_deposit = models.DecimalField(max_digits=15, decimal_places=2)

    # define the model manager for accounts
    Accounts = models.Manager()

    # allow references to a specific account be returned as the owners name and not primary key
    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


# choices for a transaction
TransactionTypes = [('Deposit', 'Deposit'), ('Withdrawal', 'Withdrawal')]


# create the transaction model
class Transaction(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=10, choices=TransactionTypes)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.CharField(max_length=100)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    # define the model manager for transactions
    Transactions = models.Manager()
