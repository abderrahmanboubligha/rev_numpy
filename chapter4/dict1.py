#create lis of dictionaires person age names
person1 = {"name": "Alice", "age": 30}
person2 = {"name": "Bob", "age": 25}
people = [person1, person2]

list=list(sorted(people, key=lambda x: x["age"]))