chai_type = "Ginger Chai"
customer_name = "Ravi"

print(f"Oredr for {customer_name} : {chai_type} please")

chai_description = "Aromatic and Bold"

# In python last word is exclusive
print(f"First word: {chai_description[0:7]}")
print(f"Last word: {chai_description[12:]}")
print(f"Last word: {chai_description[::-1]}")

label_text = "Chai Spécial"
ecoded_label = label_text.encode("utf-8")
print(f"Non Encoded label: {label_text}")
print(f"Encoded text: {ecoded_label}")

decoded_label = ecoded_label.decode("utf-8")
print(f"Decoded text: {decoded_label}")