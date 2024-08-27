rama=input("Enter the birthdate: ")
shyam=input("Enter the birthdate: ")
components1=rama.split("-")
components2=shyam.split("-")
Rama={
"Date" :components1[0],
"Month":components1[1],
"Year":components1[2],
}
Shyam={
"Date" :components2[0],
"Month":components2[1],
"Year":components2[2],
}
print("Rama is born on ",rama," shyam is born on ",shyam)
print("Rama turns ",2024-int(Rama["Year"])," years on the date",Rama["Date"],Rama["Month"],2024)
print("Shyam turns ",2024-int(Shyam["Year"])," years on the date",Shyam["Date"],Shyam["Month"],2024)