
from sqlalchemy import create_engine
from cubes.tutorial.sql import create_table_from_csv
from cubes import Workspace
from cubes.compat import ConfigParser
# from cubes.compat.ConfigParser import SafeConfigParser as ConfigParser

configg = ConfigParser()

engine = create_engine('sqlite:///data.sqlite')
create_table_from_csv(engine, "irbd_balance_2010.csv", table_name="balance",
                      fields=[("category", "string"),
                              ("line_item", "string"),
                              ("year", "integer"),
                              ("month", "integer"),
                              ("amount", "integer")],
                      create_id=True)

configg.read('slicer.ini')
workspace = Workspace(config=configg)
# workspace.register_default_store("sql", url="sqlite:///data.sqlite")
workspace.import_model("model.json")

browser = workspace.browser("ibrd_balance")
result = browser.aggregate()
print result.summary["record_count"]
print result.summary["amount_sum"]

print "+++++++++++++++"
result = browser.aggregate(drilldown=["year"])
for record in result:
    print record

print "+++++++++++++++"
result = browser.aggregate(drilldown=["item"])
for record in result:
    print record

