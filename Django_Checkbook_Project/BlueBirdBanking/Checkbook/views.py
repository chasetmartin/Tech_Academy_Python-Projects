from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm, TransactionForm
from .models import Account, Transaction


# This function will render the Home page when requested
def home(request):
    form = TransactionForm(data=request.POST or None)  # retrieve transaction form
    # Checks if request method is POST
    if request.method == 'POST':
        pk = request.POST['account']  # if the form is submitted, retrieve which account the user wants to view
        return balance(request, pk)  # call balance function to render that account's balance sheet
    content = {'form': form}  # pass content to the template as a dictionary
    # adds content of form to page
    return render(request, 'checkbook/index.html', content)


# This function will render the Create New Account page
def create_account(request):
    form = AccountForm(data=request.POST or None)  # Retrieve the account form
    # Check if requested method is POST
    if request.method == 'POST':
        if form.is_valid():  # Check to see if the submitted form is valid and if so, saves the form
            form.save()
            return redirect('index')  # Returns user back to home page
    content = {'form': form}  # Saves content to the template as a dictionary
    # adds content of form to page
    return render(request, 'checkbook/CreateNewAccount.html', content)


# This function will render the Balance page
def balance(request, pk):
    account = get_object_or_404(Account, pk=pk)  # retrieve the requested account using its primary key
    transactions = Transaction.Transactions.filter(account=pk)  # retrieve all of that account's transactions
    current_total = account.initial_deposit  # create account total variable, starting with initial deposit
    table_contents = {}  # creates a dictionary into which transaction information will be placed
    for t in transactions:  # loop through transactions and determine which is a deposit or withdrawal
        if t.type == 'Deposit':
            current_total += t.amount  # if deposit add amount to balance
            table_contents.update({t: current_total})  # add transaction and total to the dictionary
        else:
            current_total -= t.amount  # if withdrawal subtract amount from balance
            table_contents.update({t: current_total})  # add transaction and total to dictionary
    # pass account, account total balance, and transaction information to the template
    content = {'account': account, 'table_contents': table_contents, 'balance': current_total}
    return render(request, 'checkbook/BalanceSheet.html', content)


# This function will render the Transaction page when requested
def transaction(request):
    form = TransactionForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            pk = request.POST['account']
            form.save()
            return balance(request, pk)  # renders balance sheet for account
    content = {'form': form}
    return render(request, 'checkbook/AddTransaction.html', content)
