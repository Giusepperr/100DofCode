from prettytable import PrettyTable

table = PrettyTable()
table.add_column('Pokemon',['pica','charme','squirt'])
table.add_column('Type',['electric','fire','water'])
table.align = "c"
print(table)

