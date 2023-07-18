import random
import string
random.seed(10)

for_seed = random.randint(1,1000)
random.seed(for_seed)


letters = string.ascii_lowercase
rand_letters = random.choices(letters,k=1) # where k is the number of required rand_letters

print(rand_letters[0])