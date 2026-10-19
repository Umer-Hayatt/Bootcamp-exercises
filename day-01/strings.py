# Practice copy for Umer Hayatt. Adapted from the bootcamp sources in ATTRIBUTION.md.
message = "hello im Umer Hayatt"

print(message[2])
print(message[-1])

print(message[0:5])

print(message)

# string_name[start : stop]

# methods
print(message.upper())
print(message.title())

st = "   a    "
print(st.strip())
print(st.lstrip())
print(st.rstrip())

print(message.replace("hello", "Hey!"))

s = "a,b,c"
print(s.split(","))
