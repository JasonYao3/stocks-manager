from flask_table import Table, Col

class ItemTable(Table):
    name = Col('Name')
    description = Col('Description')