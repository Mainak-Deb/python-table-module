from table import table, tablecsv,join

t=tablecsv("Tech Fest.csv")

# b=t.where("(<STREAM> == 'APM') and (<YEAR> == '1st year'  )")
b=t.where("'DRAMA' in <CULTURAL PROGRAM ( You can select multiple options)>")
b=b.select(['NAME','STREAM','YEAR','Email address'])
b.order_by("STREAM");b.order_by("YEAR")

b.print_table()


g1=b.group_by_count("YEAR")
g1.print_table()

g2=b.group_by_count("STREAM")
g2.print_table()





# b.delete_where("<YEAR> != '2nd year'" )
# b.print_table()


cj=join.cross_join([b,"a"],[g1,"b"])
cj.print_table()

cj=cj.where("(<a.YEAR>==<b.YEAR>)")
cj.order_by("a.YEAR")
cj.print_table()