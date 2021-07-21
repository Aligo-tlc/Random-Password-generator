import random, string

print('Random Password Generator by Aligo using Python')
length = int(input('\nEnter password legnth'))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
punc = string.punctuation

all = lower + upper + num + punc
temp = random.sample(all,length)
password = "".join(temp)
print(password)
