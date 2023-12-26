def validate_sentence(sentence):
    words = sentence.split()
    print(words)
    # Define the structure of the sentence
    expected_structure = ["I", "am", "bananas"]
    # Check if the sentence matches the expected structure
    return words == expected_structure

# Example sentence
sentence = "I am bananas"
result = validate_sentence(sentence)
print(f"Is the sentence valid? {'Yes' if result else 'No'}")
