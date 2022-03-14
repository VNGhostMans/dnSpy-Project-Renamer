import os

OLD_NAME = "dnSpy" # Old Name
NEW_NAME = "NewdnSpyName" # New Name
OLD_NAME_BYTES = OLD_NAME.encode("utf-8")
NEW_NAME_BYTES = NEW_NAME.encode("utf-8")

agenda = ['.'] # Folder Name

while len(agenda) > 0:
	current_path = agenda.pop()
	entries = os.listdir(current_path)
	for entry in entries:
		if entry[0] == '.':
			continue
		next_path = os.path.join(current_path, entry)
		if OLD_NAME in next_path:
			new_path = next_path.replace(OLD_NAME, NEW_NAME)
			print(next_path, "->", new_path)
			os.rename(next_path, new_path)
			next_path = new_path
		if os.path.isdir(next_path):
			agenda.append(next_path)
		elif os.path.isfile(next_path) and ".exe" not in next_path and ".dll" not in next_path:
			try:
				with open(next_path, "rb") as f:
					data = f.read()
					if OLD_NAME_BYTES in data:
						data = data.replace(OLD_NAME_BYTES, NEW_NAME_BYTES)
					else:
						data = None
				if data is not None:
					with open(next_path, "wb") as f:
						f.write(data)
			except:
				print("Could not refactor", next_path)
				passs