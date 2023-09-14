lang = {"python", "javascript", "C++", "java", "CSS", "Typescript"}
lang1 = {"c#", "C++", "javascript", "PHP", "Ruby", "Swift"}

lang.remove("java")
print(lang)

print("Is Python present :", "python" in lang)

common = lang.intersection(lang1)
print(common)

