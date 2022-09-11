sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:

result = {sentence:len(sentence) for sentence in sentence.split(" ")}

print(result)