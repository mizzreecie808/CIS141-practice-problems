# Problem 5: Social Media Character Counter
# Prompt the user for a social media post.
# Let's say the social media platform has a 280 character limit for posts.
# If the user's post's length is greater than 280,
# print how many characters must be trimmed to get to 280 characters.
# Otherwise, state how many characters they can add still.

post = input("Character Counter - enter the post here: ")
char_count = len(post)

if char_count > 280:
	print(f"You must trim {char_count - 280} characters.")
else:
	print(f"You can add {280 - char_count} characters to your post.")
