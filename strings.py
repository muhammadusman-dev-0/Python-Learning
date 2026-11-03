# Topic: Strings
text = input("Enter a sentence: ")

print("\n======= TEXT ANALYZER =======")
print("Original text:", text)
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Character count:", len(text))
print("Word count:", len(text.split()))
print("Starts with Python:", text.lower().startswith("python"))
