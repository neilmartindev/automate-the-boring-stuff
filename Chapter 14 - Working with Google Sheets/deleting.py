import ezsheets

ss = ezsheets.createSpreadsheet('Delete me')

ezsheets.listSpreadsheets()

ss.delete()

ezsheets.listSpreadsheets()