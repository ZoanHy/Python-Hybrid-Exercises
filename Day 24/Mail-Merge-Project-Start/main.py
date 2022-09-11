# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
arr_names = []

PLACEHOLDER = "[name]"

with open("Input/Names/invited_names.txt") as file:
    # end = False
    # while not end:
    #     line = file.readline()
    #     if not line:
    #         end = True
    #     else:
    #         arr_names.append(line.split("\n")[0])
    arr_names = file.readlines()

with open("Input/Letters/starting_letter.txt") as file_in:
    for person_name in arr_names:
        strip_name = person_name.strip()
        s = file_in.read().replace(PLACEHOLDER, strip_name)
        with open(f"Output/ReadyToSend/letter_for_{strip_name}", mode="w") as file_out:
            file_out.write(s)
