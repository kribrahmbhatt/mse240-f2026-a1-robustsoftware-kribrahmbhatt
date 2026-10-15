import shlex

from bankaccount.BankAccount import BankAccount


def main():
	"""Main function for Bank Simulation"""

	# Keep each account in a dictionary so its ID can be used to find it.
	accounts = {}

	# Print commands so that the user knows how to interact
	print("Commands: create <id>, delete <id>, deposit <id> <amount>, ")
	print("withdraw <id> <amount>, transfer <from_id> <to_id> <amount>, balance, quit")

	# Main command loop - infinitely seek input and respond to commands until the user quits
	while True:
		# Parse the input
		try:
			# Read input as a whitespace-separated list (parsing quotes)
			parts = shlex.split(input("bank> "))
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
		# Create <account_id>
		elif command == "create" and len(parts) == 2:
			# Extract the account ID and check if it exists
			account_id = parts[1]
			if account_id in accounts:
				print(f"Account '{account_id}' already exists.")
			else:
				# If the account doesn't exist, create it
				accounts[account_id] = BankAccount(account_id)
				print(f"Created account '{account_id}'.")
		# Delete <account_id>
		elif command == "delete" and len(parts) == 2:
			account_id = parts[1]
			if account_id not in accounts:
				print(f"Account '{account_id}' not found.")
			else:
				del accounts[account_id]
				print(f"Deleted account '{account_id}'.")
		# Handle deposit/withdraw commands
		elif command in ("deposit", "withdraw") and len(parts) == 3:
			# Get account
			account_id = parts[1]
			account = accounts.get(account_id)

            # Make sure account exists
			if account is None:
				print(f"Account '{account_id}' not found.")
				continue
			try:
				# Get amount
				amount = float(parts[2])
				# TODO: Implement deposit/withdraw commands here
				# account.deposit(amount)
				# account.withdraw(amount)
			except ValueError as error:
				print(f"Invalid {command}: {error}")
			else:
				print(f"{command.capitalize()} complete for {account_id}: ${amount:.2f}.")
		elif command == "transfer" and len(parts) == 4:
			# A transfer names the source account, destination account, and amount.
			source_id, destination_id = parts[1:3]

            # Check both account ids
			if source_id not in accounts:
				print(f"Account '{source_id}' not found.")
				continue
			if destination_id not in accounts:
				print(f"Account '{destination_id}' not found.")
				continue
			try:
				#attempt transfer
				amount = float(parts[3])
				# TODO: Implement transfer logic with transfer method
			except ValueError as error:
				print(f"Invalid transfer: {error}")
			else:
				print(f"Transferred ${amount:.2f} from {source_id} to {destination_id}.")
		elif command == "balance" and len(parts) == 1:
			# Show every account using the accessor methods from BankAccount.
			for account in accounts.values():
				print("TODO: Implement this command")
				#TODO: implement get_balance() 
				# print(f"{account.getId()} has ${account.get_balance():.2f}")
		else:
			print("Invalid command or arguments.")


if __name__ == "__main__":
	main()
