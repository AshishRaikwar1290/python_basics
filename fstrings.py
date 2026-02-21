# letter = "Hey  {} {}"
letter = "Hey  {1} {0}"
name = "ashish"
country = "india"
print(letter.format(name, country))

print(f"Hey {name} {country}")

txt = "For only {price: .2f}"
print(txt.format(price = 49.09999))

print(f"Hey {{name}} {{country}}")

# output

# Hey  india ashish
# Hey ashish india
# For only  49.10
# Hey {name} {country}
