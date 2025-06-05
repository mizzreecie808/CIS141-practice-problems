# Chat 📚 Book Tracker
test_file = "books.txt"

# Add new book
# Update book's status

# Save and load the book data from a .txt file

# List all books grouped by status
def book_status(file_name):
    status = {}

    with open(file_name, "r") as file:
        for line in file:
            if ":" not in line:
                print(f"⚠️ Skipping malformed line: {line.strip()}")
                continue

            book = line.strip().split(":")
            title = book[0]
            state = book[1].strip().lower() # for consistency

            if state in status:
                status[state].append(title)
            else:
                status[state] = [title]


    for state, titles in status.items():
        print()
        print(f"{state.upper():^26}")
        print("🔹"*12)
        emoji = {"read": "📗", "reading": "📖", "to read": "📕"}.get(state, "📘")
        for item in titles:
            print(f"{emoji} {item}")

def update_status(file_name, user_title, user_status):
    catalog = []
    book_found = False
    allowed_statuses = ["read", "reading", "to read"]

    user_title = user_title.strip().lower()
    user_status = user_status.strip().lower()

    if user_status not in allowed_statuses:
        print("⚠️ Invalid status. Must be 'read', 'reading', or 'unread'.")
        return

    with open(file_name, "r") as file:
        catalog = file.read().splitlines()

    for index, item in enumerate(catalog):
        if ":" not in item:
            print(f"⚠️ Skipping invalid entry: {item}")
            continue

        title, status = item.strip().split(":")

        if title.strip().lower() == user_title:
            catalog[index] = f"{user_title.capitalize()}:{user_status}"
            book_found = True

    if book_found:
        with open(file_name, "w") as file:
            for item in catalog:
                file.write(item + "\n")

        print(f"✅ Status updated for '{user_title.title()}' to '{user_status}'.")

    else:
        print(f"❌ Book titled '{user_title.title()}' not found.")

def search_title(file_name, user_title):

    user_title = user_title.strip().lower()
    found = False

    with open(file_name, "r") as file:
        for line in file:
            if ":" not in line:
                continue

            title, status = line.strip().split(":", 1)

            if user_title in title.strip().lower():
                print(f"🔎 Match found → 📚 {title.strip().capitalize()} is marked as {status.strip()}.")
                found = True

    if not found:
        print("❌ No matching books found.")

# update_status(test_file, "Dune", "read")
# book_status(test_file)
# search_title(test_file, "The")
