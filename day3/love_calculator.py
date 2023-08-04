print("Welcome to the Love Calculator")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_string = name1 + name2
lower_case_string = combined_string.lower()

t_count = lower_case_string.count("t")
r_count = lower_case_string.count("r")
u_count = lower_case_string.count("u")
e_count = lower_case_string.count("e")

true = t_count + r_count + u_count + e_count

l_count = lower_case_string.count("l")
o_count = lower_case_string.count("o")
v_count = lower_case_string.count("v")
e_count = lower_case_string.count("e")

love = l_count + o_count + v_count + e_count

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
    print(f"Your score is{love_score}, you go together like coke and mentos")
elif (love_score > 40) and (love <= 50):
    print(f"Your score is{love_score}, you are alright together")
else:
    print(f"Your score is {love_score}")

print(love_score)
