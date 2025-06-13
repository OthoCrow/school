file_name = "write experiement"
write_to = "{}.txt".format(file_name)

text_file = open(write_to, "w+")

# String to write to file
heading = "=== MMF Test ===\n"
content = "Some content"
more = "A bit more content"

# List of strings
to_write = [heading, content, more]

# print the output
for item in to_write:
    print(item)

# Write the item ti the file
for item in to_write:
    text_file.write(item)
    text_file.write("\n")