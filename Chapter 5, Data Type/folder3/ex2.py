# Consider this fragment of code:

#	import turtle

#	tess = turtle.Turtle()
#	alex = tess
#	alex.color("hotpink")


# Does this fragment create one or two turtle instances?
# Does setting the color of alex also change the color of tess?
# Explain in detail.


# ANSWER:

# The fragment creates one turtle, "tess", and sets an alias to it, "alex".
# Once that alex color changes to hotpink it will also affect "tess" because "alex" it's tess's alias.
# So any changes will cause the original object to be modifiyed by the alias
