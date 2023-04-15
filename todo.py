# github.com/echtr

from tinydb import TinyDB
from tinydb import Query
from rich.console import Console
from rich.table import Table


db = TinyDB("db.json")
c = Query()

def create_table():
	global table
	console.print("")
	table = Table(title = "TODO App")
	table.add_column("ID")
	table.add_column("Mission")
	table.add_column("Is it done?")

console = Console()
console.clear()

while True:
	create_table()

	for i in db.all():
		if i["done"] == "yes": color = "green"
		elif i["done"] == "no": color = "red"
		table.add_row(str(i["id"]), i["mission"], f"[{color}]{i['done']}[/{color}]")

	console.print(table)

	q = console.input("""
0: Quit
1: Add A Row
2: Delete A Row
3: Change A Row (y<->n)
>> """)

	if q == "0": break

	if q == "1":
		mission = console.input("Mission >> ")
		count = 1 if len(db) == 0 else db.all()[-1]["id"] + 1
		db.insert({"id": count, "mission":mission, "done":"no"})

	if q == "2":
		_id = int(console.input("Row ID >> "))
		db.remove(c.id == _id)

	if q == "3":
		_id = int(console.input("Row ID >> "))
		if db.get(c.id == _id)["done"] == "no":db.update({"done":"yes"}, c.id == _id)
		else: db.update({"done":"no"}, c.id == _id)

	console.clear()