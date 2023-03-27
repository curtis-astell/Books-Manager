import sys
from PyQt5.QtWidgets import (QApplication,
                             QLabel,
                             QLineEdit,
                             QTableWidget,
                             QPushButton,
                             QTableWidgetItem,
                             QFileDialog,
                             QMainWindow)

from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Window Properties
        self.setWindowTitle('Books Manager')
        self.move(100, 100)
        self.setFixedSize(690, 750)
        self.setWindowIcon(QIcon('icons/booksmanagericon'))

        # Main Ledger Properties
        self.ledger_list = QTableWidget(self)
        self.ledger_list.setRowCount(50)  # Number of rows is 50 by default, can be adjusted by user
        self.ledger_list.setColumnCount(5)  # Number of columns is always 5
        self.ledger_list.move(10, 40)
        self.ledger_list.horizontalHeader().setDefaultSectionSize(123)
        self.ledger_list.setHorizontalHeaderLabels(["Date", "Description", "Debit", "Credit", "Balance"])
        self.ledger_list.setFixedSize(670, 700)

        # Add Row Button
        self.ledger_add = QPushButton(self)
        self.ledger_add.move(10, 10)
        self.ledger_add.setText("Add Row")
        self.ledger_add.setToolTip("Add more rows to the ledger")
        self.ledger_add.clicked.connect(self.add_clicked)

        # Remove Row Button
        self.ledger_del = QPushButton(self)
        self.ledger_del.move(110, 10)
        self.ledger_del.setText("Remove Row")
        self.ledger_del.setToolTip("Remove rows from the ledger")
        self.ledger_del.clicked.connect(self.del_clicked)

        # Save Ledger Button
        self.save_button = QPushButton(self)
        self.save_button.move(210, 10)
        self.save_button.setText("Save")
        self.save_button.setToolTip("Save your ledger for later")
        self.save_button.clicked.connect(self.save_clicked)

        # Load Ledger Button
        self.load_button = QPushButton(self)
        self.load_button.move(310, 10)
        self.load_button.setText("Load")
        self.load_button.setToolTip("Load a previously saved ledger")
        self.load_button.clicked.connect(self.load_clicked)

        # Update Balance Button
        self.update_button = QPushButton(self)
        self.update_button.move(410, 10)
        self.update_button.setText("Update Balance")
        self.update_button.setToolTip("Update the balance column")
        self.update_button.clicked.connect(self.update_clicked)

        # Previous Balance Label & Text Edit
        # This is used for keeping the balance total of an old ledger
        # User enters the final balance total of a previous ledger under the "Previous Balance" entry
        self.balance_label = QLabel(self)
        self.balance_label.setText("Previous Balance:")
        self.balance_label.move(520, 10)
        self.balance_label.setToolTip("Enter previous balance total from an old ledger")
        self.previous_balance = QLineEdit(self)
        self.previous_balance.setGeometry(620, 10, 60, 30)
        self.previous_balance.setToolTip("Enter previous balance total from an old ledger")
        self.previous_balance.setText("0")  # Previous balance is set to 0 by default

    # Function adds rows to ledger QTableWidget when Add Row Button is clicked
    def add_clicked(self):
        self.ledger_list.insertRow(self.ledger_list.rowCount())

    # Function deletes rows from ledger QTableWidget when Remove Row Button is clicked
    def del_clicked(self):
        self.ledger_list.removeRow(self.ledger_list.rowCount() - 1)

    # Saves ledger contents as a plain text file when Save Button is clicked
    def save_clicked(self):
        # Quick count of the rows in the ledger
        row_count = 0
        for i in range(self.ledger_list.rowCount()):
            row_count += 1
        # Brings up file dialog to save file
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "ledgers", "All Files (*);;Text Files (*.txt)",
                                                   options=options)
        # If user clicks cancel, closes file dialog window
        if not file_name:
            return
        with open("{}".format(file_name), "w") as f:
            # Saves row count to text file
            f.write("# Ledger Row Count:\n{}\n".format(row_count))
            # Saves previous balance entry to text file
            f.write("# Previous Balance:\n{}\n".format(self.previous_balance.text()))
            # Saves ledger contents to text file
            f.write("# Ledger Contents (Date,Description,Debit,Credit,Balance):\n")
            for i in range(self.ledger_list.rowCount()):
                row = []
                for j in range(self.ledger_list.columnCount()):
                    item = self.ledger_list.item(i, j)
                    # If item in cell isn't blank, write it to the text file. Otherwise, don't.
                    if item is not None:
                        row.append(item.text())
                    else:
                        row.append("")
                # Separates each item with a comma
                f.write(",".join(row) + "\n")

    # Loads a previously saved ledger.
    def load_clicked(self):
        # Brings up file dialog to load file
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "ledgers", "All Files (*);;Text Files (*.txt)",
                                                   options=options)
        # If user clicks cancel, closes file dialog window
        if not file_name:
            return
        with open(file_name, "r") as f:
            lines = f.readlines()
            # Reads second line of file and assigns new number of rows based on the value written
            self.ledger_list.setRowCount(int(lines[1]))
            # Reads fourth line of file for the previous balance value
            self.previous_balance.setText(lines[3].strip())
            # Loads rest of text file to fill contents of ledger
            # Columns are separated by commas
            for i, line in enumerate(lines[5:]):
                row = line.strip().split(",")
                for j, item in enumerate(row):
                    self.ledger_list.setItem(i, j, QTableWidgetItem(item))

    # Function updates items in balance column
    def update_clicked(self):
        row_pop = 0
        # Sets balance variable to whatever is written under "Previous Balance" as a starting point
        balance = float(self.previous_balance.text())
        # For loop determines value of row_pop variable
        for row in range(self.ledger_list.rowCount()):
            debit_item = self.ledger_list.item(row, 2)
            credit_item = self.ledger_list.item(row, 3)
            # If debit or credit column is populated in current row, row_pop variable increases by 1
            if debit_item is not None and debit_item.text() != "" or \
                    credit_item is not None and credit_item.text() != "":
                row_pop += 1
            # Row is empty, loop breaks, determining how many rows are populated
            else:
                break
        # For loop adds balance total for each populated row
        for row in range(row_pop):
            try:
                debit = float(self.ledger_list.item(row, 2).text())
            except ValueError:
                debit = 0
            except AttributeError:
                debit = 0
            try:
                credit = float(self.ledger_list.item(row, 3).text())
            except ValueError:
                credit = 0
            except AttributeError:
                credit = 0
            balance = (balance + credit - debit)
            format_balance = QTableWidgetItem(str("%.2f" % balance))
            self.ledger_list.setItem(row, 4, format_balance)
            row += 1
        return balance


if __name__ == '__main__':
    app = QApplication(sys.argv)
    booksManager = MainWindow()
    booksManager.show()
    sys.exit(app.exec_())
