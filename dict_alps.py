def p(emps):
    for i in emps:
        for o in i["children"]:
            if o ["age"]>=18:
                print (i["name"])


ivan = {
    "name": "ivan",
    "age": 34,
    "children": [{
        "name": "vasja",
        "age": 12,
    }, {
        "name": "petja",
        "age": 10,
    }],
}

darja = {
    "name": "darja",
    "age": 41,
    "children": [{
        "name": "kirill",
        "age": 21,
    }, {
        "name": "pavel",
        "age": 15,
    }],
}
emps = [ivan, darja]

p(emps)


