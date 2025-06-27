#include <iostream>
#include <vector>
#include <string>
#include <limits>

using namespace std;

class Account {
private:
    int accountNumber;
    string name;
    double balance;

public:
    Account(int accNo, const string& accName, double initialDeposit)
        : accountNumber(accNo), name(accName), balance(initialDeposit) {}

    int getAccountNumber() const {
        return accountNumber;
    }

    string getName() const {
        return name;
    }

    double getBalance() const {
        return balance;
    }

    void deposit(double amount) {
        if (amount > 0)
            balance += amount;
        else
            cout << "Invalid deposit amount.\n";
    }

    void withdraw(double amount) {
        if (amount > 0 && amount <= balance)
            balance -= amount;
        else
            cout << "Invalid or insufficient balance for withdrawal.\n";
    }

    void display() const {
        cout << "Account Number: " << accountNumber << "\n";
        cout << "Name: " << name << "\n";
        cout << "Balance: $" << balance << "\n";
    }
};

class BankSystem {
private:
    vector<Account> accounts;
    int nextAccountNumber = 1001;

    Account* findAccount(int accNo) {
        for (auto& acc : accounts) {
            if (acc.getAccountNumber() == accNo)
                return &acc;
        }
        return nullptr;
    }

public:
    void createAccount() {
        string name;
        double deposit;

        cout << "Enter your name: ";
        cin.ignore();
        getline(cin, name);

        cout << "Enter initial deposit: ";
        cin >> deposit;

        if (deposit < 0) {
            cout << "Initial deposit cannot be negative.\n";
            return;
        }

        Account newAcc(nextAccountNumber++, name, deposit);
        accounts.push_back(newAcc);

        cout << "Account created successfully. Your account number is: "
             << newAcc.getAccountNumber() << "\n";
    }

    void depositFunds() {
        int accNo;
        double amount;

        cout << "Enter account number: ";
        cin >> accNo;

        Account* acc = findAccount(accNo);
        if (!acc) {
            cout << "Account not found.\n";
            return;
        }

        cout << "Enter amount to deposit: ";
        cin >> amount;
        acc->deposit(amount);
        cout << "Deposit successful.\n";
    }

    void withdrawFunds() {
        int accNo;
        double amount;

        cout << "Enter account number: ";
        cin >> accNo;

        Account* acc = findAccount(accNo);
        if (!acc) {
            cout << "Account not found.\n";
            return;
        }

        cout << "Enter amount to withdraw: ";
        cin >> amount;
        acc->withdraw(amount);
        cout << "Withdrawal attempted.\n";
    }

    void transferFunds() {
        int fromAccNo, toAccNo;
        double amount;

        cout << "Enter sender account number: ";
        cin >> fromAccNo;
        cout << "Enter recipient account number: ";
        cin >> toAccNo;

        Account* fromAcc = findAccount(fromAccNo);
        Account* toAcc = findAccount(toAccNo);

        if (!fromAcc || !toAcc) {
            cout << "One or both accounts not found.\n";
            return;
        }

        cout << "Enter amount to transfer: ";
        cin >> amount;

        if (amount > 0 && fromAcc->getBalance() >= amount) {
            fromAcc->withdraw(amount);
            toAcc->deposit(amount);
            cout << "Transfer successful.\n";
        } else {
            cout << "Transfer failed. Check amount and balance.\n";
        }
    }

    void viewAccount() {
        int accNo;
        cout << "Enter account number: ";
        cin >> accNo;

        Account* acc = findAccount(accNo);
        if (acc) {
            acc->display();
        } else {
            cout << "Account not found.\n";
        }
    }

    void showMenu() {
        int choice;
        do {
            cout << "\n--- Online Banking System ---\n";
            cout << "1. Create Account\n";
            cout << "2. Deposit Funds\n";
            cout << "3. Withdraw Funds\n";
            cout << "4. Transfer Funds\n";
            cout << "5. View Account Details\n";
            cout << "0. Exit\n";
            cout << "Enter your choice: ";
            cin >> choice;

            switch (choice) {
                case 1: createAccount(); break;
                case 2: depositFunds(); break;
                case 3: withdrawFunds(); break;
                case 4: transferFunds(); break;
                case 5: viewAccount(); break;
                case 0: cout << "Thank you for using our banking system!\n"; break;
                default: cout << "Invalid choice.\n";
            }

        } while (choice != 0);
    }
};

int main() {
    BankSystem system;
    system.showMenu();
    return 0;
}