from table import table, tablecsv,join

e=tablecsv("employee.csv")
e.print_table()

# cj=join.cross_join([e,"a"],[e,"b"])
# cj=cj.where("<a.BOSS>==<b.NAME>")
# cj=cj.select(["b.NAME","b.ID","b.DEPT"])
# cj.print_table()

d=tablecsv("dept.csv")
d.print_table()
dj=join.cross_join([e,"a"],[d,"b"])




dj=dj.where("<a.DEPT>==<b.DEPT>")
dj.print_table()