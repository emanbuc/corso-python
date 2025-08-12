acronyms=["LOL", "BRB", "GTG", "TTYL", "IMO", "FYI", "IDK", "BFF", "TMI", "ROFL"]
acronyms.append("OMG")

print("Acronyms list updated:", acronyms)
print("Total acronyms:", len(acronyms))
print("First acronym:", acronyms[0])
print("Last acronym:", acronyms[-1])

acronyms.remove("TMI")
print("Acronyms after removal:", acronyms)
print("Acronyms list length after removal:", len(acronyms))
acronyms.remove(acronyms[0])
print("Acronyms list after removing first element:", acronyms)

del acronyms[0]
print("Acronyms list after deleting first element:", acronyms)

if "LOL" in acronyms:
    print("LOL is in the acronyms list.")
else:
    print("LOL is not in the acronyms list.")

for acronym in acronyms:
    print("Acronym:", acronym)
