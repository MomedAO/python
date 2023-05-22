# Adding whitespace to string with tabs or newlines
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"

print(full_name)
print(f"Hello, {full_name.title()}")
message = f"Hello, {full_name.title()}!"
print(message)

print("Python")
print("\tPython")  # tab \t
print("\nPython")  # newlinne \n

print("Linguages:\nPython\nC++\nJavaScript")
print("Linguages:\n\tPython\n\tC++\n\tJavaScript")
under = "Variable in string"
linguages = "\n\tPython\n\tC++\n\tJavaScript"
print(f"{under}\n{linguages}")
