Instructions for Books Manager program

* Ledger table info:

  The main table of the ledger features 5 columns:
   - Date
   - Description
   - Debit
   - Credit
   - Balance
  
  "Date" and "Description" have no mandatory formatting and are purely visual. They can also be left blank if you choose.
  "Debit" and "Credit" must be integer or decimal values, as they will deduct and add to the balance column respectively. 
  The Balance column does not need to be written in, it will be filled automatically. 
  
  By default there are 50 rows in the ledger, but this number can be adjusted with the "Add Row" and "Remove Row"
  buttons. Saving your ledger will save the amount of rows, as well as the contents of your ledger. 
  That said, I recommend starting a new ledger after a while to prevent the list from getting too unwieldy.

* Saving and loading your ledgers:
  
  You can save a ledger for later use with the "Save" button. It will bring up the Windows file explorer. 
  You can save a new ledger or overwrite an existing one this way. I recommend giving your ledger meaningful names so it's
  easy to know what they contain at a quick glance. 
  For example, "Jan 2023" or "2023 Q1"
  
  To open a previously saved ledger, click the "Load" button and find the file for the ledger you wish to view.

* Updating the balance column:
  
  To update the numbers in the Balance column click the "Update Balance" button. Each row will deduct anything written in
  the "Debit" column, and add anything written in the "Credit" column to a value that is then written in each row of the
  "Balance" column. 

* Loading the balance of an old ledger into a new one:
  
  If you've started a new ledger but want the balance total to continue from a previous ledger, adjust the value
  to the right of the "Update Balance" button. This number starts as 0 by default but can be overwritten.
  Saving your ledger also saves this value.

* "How does the program save my ledger for later?"
  
  When you save your ledger it is written to a text file. These text files can be accessed anytime from the Books Manager
  "ledgers" folder. The program also reads the text file to load the data back into the ledger table. If you decide to edit the
  contents of these text files you'll notice that the values change when you load them back into the Books Manager program. 
  As a result, be cautious when doing so, as it's fairly easy to ruin your ledger this way.
