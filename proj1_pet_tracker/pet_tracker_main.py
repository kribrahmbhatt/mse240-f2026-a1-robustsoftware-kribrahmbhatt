import shlex

from dog.Dog import Dog


def print_dog(dog):
	"""Print every known fact about a dog using the accessor methods from Dog."""
	issues = ", ".join(dog.get_potential_health_issues()) or "none"
	print(f"{dog.get_name()}: {dog.get_breed()}, {dog.get_gender()}, {dog.get_colour()}, "
		  f"{dog.get_weight():.1f} lbs, age {dog.get_age()}, health issues: {issues}")


def main():
	"""Main function for Pet Tracker"""

	# Keep each dog in a dictionary so its name can be used to find it.
	dogs = {}

	# Print commands so that the user knows how to interact
	print("Commands: add <name> <breed> <gender> <weight> <colour> <birth_year>, remove <name>,")
	print("rename <name> <new_name>, weigh <name> <weight>, issue <name> <health_issue>,")
	print("info <name>, list, quit")
	print("(Use quotes for values with spaces, e.g. issue Waffle \"geriatric hips\")")

	# Main command loop - infinitely seek input and respond to commands until the user quits
	while True:
		# Parse the input
		try:
			# Read input as a whitespace-separated list (parsing quotes)
			parts = shlex.split(input("pet_tracker> "))
		# Encountered an end of file (from redirected input from a file -or- ctrl-d from real-time input)
		except EOFError:
			break
		# Catch any exceptions to keep looping; notify user
		except ValueError as error:
			print(f"Invalid command: {error}")
			continue

		# Empty input
		if not parts:
			continue

		# Map command to lower case to be non-case sensitive
		command = parts[0].lower()

		# Quit
		if command == "quit" and len(parts) == 1:
			break
		# Add <name> <breed> <gender> <weight> <colour> <birth_year>
		elif command == "add" and len(parts) == 7:
			# Extract the dog's name and check if it exists
			name, breed, gender = parts[1:4]
			colour = parts[5]
			if name in dogs:
				print(f"Dog '{name}' already exists.")
				continue
			try:
				# Convert numeric arguments, then let the Dog constructor validate everything
				weight = float(parts[4])
				birth_year = int(parts[6])
				dog = Dog(name, breed, gender, weight, colour, [], birth_year)
			except (TypeError, ValueError) as error:
				print(f"Invalid add: {error}")
			else:
				dogs[name] = dog
				print(f"Added dog '{name}'.")
		# Remove <name>
		elif command == "remove" and len(parts) == 2:
			name = parts[1]
			if name not in dogs:
				print(f"Dog '{name}' not found.")
			else:
				del dogs[name]
				print(f"Removed dog '{name}'.")
		# Rename <name> <new_name>
		elif command == "rename" and len(parts) == 3:
			name, new_name = parts[1:3]

			# Make sure the dog exists and the new name isn't taken
			if name not in dogs:
				print(f"Dog '{name}' not found.")
				continue
			if new_name in dogs:
				print(f"Dog '{new_name}' already exists.")
				continue
			try:
				dogs[name].set_name(new_name)
			except (TypeError, ValueError) as error:
				print(f"Invalid rename: {error}")
			else:
				# Re-file the dog under its new name
				dogs[new_name] = dogs.pop(name)
				print(f"Renamed '{name}' to '{new_name}'.")
		# Weigh <name> <weight>
		elif command == "weigh" and len(parts) == 3:
			# Get dog
			name = parts[1]
			dog = dogs.get(name)

			# Make sure dog exists
			if dog is None:
				print(f"Dog '{name}' not found.")
				continue
			try:
				# Get weight
				weight = float(parts[2])
				dog.set_weight(weight)
			except (TypeError, ValueError) as error:
				print(f"Invalid weigh: {error}")
			else:
				print(f"Recorded weight for {name}: {dog.get_weight():.1f} lbs.")
		# Issue <name> <health_issue>
		elif command == "issue" and len(parts) == 3:
			name, health_issue = parts[1:3]
			dog = dogs.get(name)

			# Make sure dog exists
			if dog is None:
				print(f"Dog '{name}' not found.")
				continue
			try:
				dog.add_potential_health_issue(health_issue)
			except (TypeError, ValueError) as error:
				print(f"Invalid issue: {error}")
			else:
				print(f"Added health issue for {name}: {health_issue}.")
		# Info <name>
		elif command == "info" and len(parts) == 2:
			name = parts[1]
			dog = dogs.get(name)
			if dog is None:
				print(f"Dog '{name}' not found.")
			else:
				print_dog(dog)
		# List
		elif command == "list" and len(parts) == 1:
			# Show every dog using the accessor methods from Dog.
			if not dogs:
				print("No dogs tracked yet.")
			for dog in dogs.values():
				print_dog(dog)
		else:
			print("Invalid command or arguments.")


if __name__ == "__main__":
	main()
