from mas import nav_card

for i in nav_card:
    print(i["id"])
    for q in i["mas"]:
        print(q)