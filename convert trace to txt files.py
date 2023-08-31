
input_filename = 'vegas.tr'
output_filename = 'vegas.txt'

with open(input_filename, 'r') as infile:
    contents = infile.read()

with open(output_filename, 'w') as outfile:
    outfile.write(contents)

print(f"Contents of {input_filename} have been written to {output_filename}")
