# Positional, Keyword, and Default Arguments
# https://www.youtube.com/watch?v=tkJ6E_u5mZo

# Positional: order of arguments matters
# def madLibs(noun, verb, adjective):
#     mad_string = (
#         f"A {adjective} student at Olympic College start at their {noun}"
#         f"in confusion as the professor told them to {verb} their " +
#         "first line of code."
#         )
#     return mad_string
#print(madLibs("hamburger", "walk", "shiny"))


# Default: argument has a preset value
def madLibs(noun, verb, adjective="spunky"):
    mad_string = (
        f"A {adjective} student at Olympic College start at their {noun}"
        f"in confusion as the professor told them to {verb} their " +
        "first line of code."
        )
    return mad_string

# Keyword: explicitly name your parameters
print(madLibs(adjective="shiny", verb="walk", noun="hamburger"))
