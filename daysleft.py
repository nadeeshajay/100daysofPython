age = int(input('What is your current age ? '))
expect = int(input('How old are you expecting to live ? '))
days_left = (expect - age)*365
weeks_left = int(days_left / 7)
months_left = int(days_left/30)
print(f"You\'ve {days_left} days or {weeks_left} weeks or {months_left} months left.")
