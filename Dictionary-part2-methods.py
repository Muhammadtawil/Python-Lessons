# ------------------------# -- Dictionary Methods --# ------------------------# clear()user = {  "name": "Osama"}print(user)user.clear()print(user)print("=" * 50)# update()member = {  "name": "muhammad"}print(member)member["age"] = 27print(member)member.update({"country": "Lebanon"})print(member)print("=" * 50)# copy()main = {  "name": "Muhammad"}b = main.copy()print(b)main.update({"skills": "programming"})print(main)print(b)# keys() + values()print(main.keys())print(main.values())