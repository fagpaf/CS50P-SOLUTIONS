def emoji(reaction):
    reaction = reaction.replace(":)", "🙂")
    reaction = reaction.replace(":(", "🙁")
    return reaction

string = input()

text = emoji(string)
print(text)
