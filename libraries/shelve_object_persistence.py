import shelve

d = shelve.open('cache_file')

#d["1"] = "one"      # store data at key
#d["2,3"] = ["two", "three"]
#d["4"] = { 1, 2, 3, 4 }
#del d["1"]          # delete data stored at key

for key in d.keys(): # a list of all existing keys (slow!)
    print(d[key])

d.close()
