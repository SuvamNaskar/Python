# This code gives keywords to the given text.

text = """The analyst usually studies all the available documents regarding the system to be developed before visiting the customer site. Customers usually provide statement of purpose (SoP) document to the developers. Typically these documents might discuss issues such as the context in which the software is required, the basic purpose, the stakeholders, features of any similar software developed elsewhere, etc."""

# Split the text into sentences.
sentences = text.split(".")

# Identify the key points from each sentence.
key_points = []
for sentence in sentences:
  sentence = sentence.strip()
  if sentence:
    key_points.append(sentence.split()[2:])

# Print keywords
print(key_points)