#===============================================
#Problem 1 — Student Report Card
#===============================================
print("Problem 1 — Student Report Card")
data = {
    "Hari":{"Math":90,"Physics":85,"Chemistry":80},
    "John":{"Math":75,"Physics":95,"Chemistry":88},
    "Kamal":{"Math":92,"Physics":91,"Chemistry":89}
}
top_std=""
highst_avg=0
for name,marks in data.items():
    print(name)
    print(f"Totoal - {sum(marks.values())}")
    print("Average","-",avg:=sum(marks.values())/len(marks.values()))
    if avg>highst_avg:
        top_std=name
	avg=highst_avg
print(f"Top student is {top_std}")
