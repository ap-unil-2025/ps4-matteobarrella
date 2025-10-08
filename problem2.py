"""
Problem 2: Dictionary Operations and Nested Structures
Practice working with Python dictionaries - creating, accessing, modifying, and nesting them.
"""

import string
def create_student_record(name, age, major, gpa):
    """Create a student record as a dictionary."""
    return {'name': name, 'age': age, 'major': major, 'gpa': gpa}


def get_value_safely(dictionary, key, default=None):
    """Get a value from a dictionary safely, returning default if key doesn't exist."""
    return dictionary.get(key, default)


def merge_dictionaries(dict1, dict2):
    """Merge two dictionaries. If keys conflict, dict2's values take precedence."""
    merged = dict1.copy()
    merged.update(dict2)
    return merged

def count_word_frequency(text):
    """
    Count the frequency of each word in a text string.
    Convert to lowercase and ignore punctuation.
    """
    if not text:
        return {}
    lowered = text.lower()
    translator = str.maketrans('', '', string.punctuation)
    cleaned = lowered.translate(translator)
    words = cleaned.split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq


def invert_dictionary(dictionary):
    """Invert a dictionary (swap keys and values). Assume all values are unique."""
    return {v: k for k, v in dictionary.items()}


def filter_dictionary(dictionary, keys_to_keep):
    """Create a new dictionary with only the specified keys."""
    return {k: dictionary[k] for k in keys_to_keep if k in dictionary}


def group_by_first_letter(words):
    """
    Group words by their first letter.
    Keys are lowercase first letters; words are preserved as given.
    """
    grouped = {}
    for w in words:
        if not w:
            continue
        first = w[0].lower()
        grouped.setdefault(first, []).append(w)
    return grouped


def calculate_grades_average(students):
    """Calculate the average grade for each student (rounded to 2 decimals)."""
    averages = {}
    for name, grades in students.items():
        if not grades:
            averages[name] = 0.0
        else:
            averages[name] = round(sum(grades) / len(grades), 2)
    return averages


def nested_dict_access(av_data, keys):
    """Access a nested dictionary using a list of keys. Return None if any key doesn't exist."""
    current = av_data
    for k in keys:
        if not isinstance(current, dict) or k not in current:
            return None
        current = current[k]
    return current


# Test cases
if __name__ == "__main__":
    print("Testing Dictionary Operations...")
    print("-" * 50)

    # Test create_student_record
    print("Test 1: create_student_record")
    result = create_student_record("Alice", 20, "CS", 3.8)
    print(f"Result: {result}")
    assert result == {'name': 'Alice', 'age': 20, 'major': 'CS', 'gpa': 3.8}
    print("✓ Passed\n")

    # Test get_value_safely
    print("Test 2: get_value_safely")
    d = {'a': 1, 'b': 2}
    assert get_value_safely(d, 'a') == 1
    assert get_value_safely(d, 'c', 'Not found') == 'Not found'
    print("✓ Passed\n")

    # Test merge_dictionaries
    print("Test 3: merge_dictionaries")
    result = merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
    print(f"Result: {result}")
    assert result == {'a': 1, 'b': 3, 'c': 4}
    print("✓ Passed\n")

    # Test count_word_frequency
    print("Test 4: count_word_frequency")
    result = count_word_frequency("hello world hello")
    print(f"Result: {result}")
    assert result == {'hello': 2, 'world': 1}
    print("✓ Passed\n")

    # Test invert_dictionary
    print("Test 5: invert_dictionary")
    result = invert_dictionary({'a': 1, 'b': 2, 'c': 3})
    print(f"Result: {result}")
    assert result == {1: 'a', 2: 'b', 3: 'c'}
    print("✓ Passed\n")

    # Test filter_dictionary
    print("Test 6: filter_dictionary")
    result = filter_dictionary({'a': 1, 'b': 2, 'c': 3, 'd': 4}, ['a', 'c'])
    print(f"Result: {result}")
    assert result == {'a': 1, 'c': 3}
    print("✓ Passed\n")

    # Test group_by_first_letter
    print("Test 7: group_by_first_letter")
    result = group_by_first_letter(['apple', 'banana', 'apricot', 'blueberry'])
    print(f"Result: {result}")
    assert result == {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry']}
    print("✓ Passed\n")

    # Test calculate_grades_average
    print("Test 8: calculate_grades_average")
    result = calculate_grades_average({
        'Alice': [90, 85, 88],
        'Bob': [75, 80, 78]
    })
    print(f"Result: {result}")
    assert result == {'Alice': 87.67, 'Bob': 77.67}
    print("✓ Passed\n")

    # Test nested_dict_access
    print("Test 9: nested_dict_access")
    data = {'a': {'b': {'c': 123}}}
    assert nested_dict_access(data, ['a', 'b', 'c']) == 123
    assert nested_dict_access(data, ['a', 'x']) is None
    print("✓ Passed\n")

    print("=" * 50)
    print("All tests passed! Excellent work!")
