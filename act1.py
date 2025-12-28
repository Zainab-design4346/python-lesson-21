info={
    "id1":{"name":"zainab", "roll":"28" },
    "id2":{"name":"musa", "roll":"18" },
    "id3":{"name":"max", "roll":"21" },
    "id4":{"name":"ava", "roll":"13" },
    "id1":{"name":"zainab", "roll":"28" }
}
result={}
for key,value in info.items():
    if value not in result.values():
        result[key]=value

print(result)