
"""
Problem 3: Mini Contact Manager
Build a simple contact manager using lists and dictionaries.
Practice combining data structures and writing functions.
"""


def create_contact(name, phone, email=""):
    """
    Create a contact dictionary.
    """
    return {'name': name, 'phone': phone, 'email': email}


def add_contact(contact_list, name, phone, email=""):
    """
    Add a new contact to the contacts list.
    """
    new_contact = create_contact(name, phone, email)
    contact_list.append(new_contact)
    return new_contact


def find_contact_by_name(contact_list, name):
    """
    Find a contact by name (case-insensitive).
    """
    target = name.lower()
    for c in contact_list:
        if c.get('name', '').lower() == target:
            return c
    return None


def search_contacts(contact_list, search_term):
    """
    Search for contacts by name or phone (partial match, case-insensitive on name).
    """
    term_lower = str(search_term).lower()
    matches = []
    for c in contact_list:
        name_match = term_lower in c.get('name', '').lower()
        phone_match = term_lower in c.get('phone', '')
        if name_match or phone_match:
            matches.append(c)
    return matches


def delete_contact(contact_list, name):
    """
    Delete a contact by name. Case-insensitive.
    """
    target = name.lower()
    for idx, c in enumerate(contact_list):
        if c.get('name', '').lower() == target:
            contact_list.pop(idx)
            return True
    return False


def count_contacts_with_email(contact_list):
    """
    Count how many contacts have an email address (non-empty string).
    """
    return sum(1 for c in contact_list if c.get('email', '') != '')


def get_all_phone_numbers(contact_list):
    """
    Extract all phone numbers from contacts.
    """
    return [c.get('phone', '') for c in contact_list]


def sort_contacts_by_name(contact_list):
    """
    Return a new list of contacts sorted alphabetically by name (case-insensitive).
    """
    return sorted(contact_list, key=lambda c: c.get('name', '').casefold())


def contact_exists(contact_list, name):
    """
    Check if a contact with the given name exists.
    """
    return find_contact_by_name(contact_list, name) is not None


# Test cases
if __name__ == "__main__":
    print("Testing Mini Contact Manager...")
    print("-" * 50)

    # Create test contacts list
    contacts = []

    # Test 1: create_contact
    print("Test 1: create_contact")
    contact = create_contact("Alice", "555-0001", "alice@email.com")
    print(f"Created: {contact}")
    assert contact == {'name': 'Alice', 'phone': '555-0001', 'email': 'alice@email.com'}
    print("✓ Passed\n")

    # Test 2: add_contact
    print("Test 2: add_contact")
    add_contact(contacts, "Alice", "555-0001", "alice@email.com")
    add_contact(contacts, "Bob", "555-0002")
    add_contact(contacts, "Charlie", "555-0003", "charlie@email.com")
    print(f"Added 3 contacts. Total: {len(contacts)}")
    assert len(contacts) == 3
    print("✓ Passed\n")

    # Test 3: find_contact_by_name
    print("Test 3: find_contact_by_name")
    found = find_contact_by_name(contacts, "alice")  # Case-insensitive
    print(f"Found: {found}")
    assert found is not None and found['name'] == 'Alice'
    print("✓ Passed\n")

    # Test 4: search_contacts
    print("Test 4: search_contacts")
    results = search_contacts(contacts, "555-000")
    print(f"Search '555-000' found {len(results)} contacts")
    assert len(results) == 3  # All have 555-000 in phone
    print("✓ Passed\n")

    # Test 5: count_contacts_with_email
    print("Test 5: count_contacts_with_email")
    count = count_contacts_with_email(contacts)
    print(f"Contacts with email: {count}")
    assert count == 2  # Alice and Charlie have emails
    print("✓ Passed\n")

    # Test 6: get_all_phone_numbers
    print("Test 6: get_all_phone_numbers")
    phones = get_all_phone_numbers(contacts)
    print(f"Phone numbers: {phones}")
    assert phones == ['555-0001', '555-0002', '555-0003']
    print("✓ Passed\n")

    # Test 7: sort_contacts_by_name
    print("Test 7: sort_contacts_by_name")
    sorted_contacts = sort_contacts_by_name(contacts)
    names = [c['name'] for c in sorted_contacts]
    print(f"Sorted names: {names}")
    assert names == ['Alice', 'Bob', 'Charlie']
    print("✓ Passed\n")

    # Test 8: contact_exists
    print("Test 8: contact_exists")
    assert contact_exists(contacts, "Alice") == True # pylint: disable=singleton-comparison
    assert contact_exists(contacts, "David") == False # pylint: disable=singleton-comparison
    print("✓ Passed\n")

    # Test 9: delete_contact
    print("Test 9: delete_contact")
    deleted = delete_contact(contacts, "Bob") # pylint: disable=invalid-name
    print(f"Deleted Bob: {deleted}, Remaining: {len(contacts)}") # pylint: disable=singleton-comparison
    assert deleted == True and len(contacts) == 2 # pylint: disable=singleton-comparison
    print("✓ Passed\n")

    print("=" * 50)
    print("All tests passed! Great work on the contact manager!")
