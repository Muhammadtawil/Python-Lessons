# ------------------------
# -- Dictionary Methods --
# ------------------------

# setdefault()

user = {
  "name": "Muhammad"
}
print(user)
print(user.setdefault("age", 27))
print(user)

print("=" * 40)

# popitem()

member = {
  "name": "Muhammad",
  "skill": "PS4"
}
print(member)
member.update({"age": 27})
print(member.popitem())

print("=" * 40)

# items()

view = {
  "name": "Muhammad",
  "skill": "XBox"
}

allItems = view.items()
print(view)
view["age"] = 27

print(allItems)

print("=" * 40)

# fromkeys()

a = ('MyKeyOne', 'MyKeyTwo', 'MyKeyThree')
b = "X","Y"

print(dict.fromkeys(a, b))