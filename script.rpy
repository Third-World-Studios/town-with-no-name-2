#characters.

define j = Character("Jim", what_font="kremlin.ttf",color="FFE920")
#character pictures
image jim = "jim.png"

#backgrounds

image town = "town.png"
image black = "black.jpg"
image main_menu = Movie(channel="main_menu", play="retard.webm")



label start:
    scene black
    with Dissolve(3.0)
    $ renpy.movie_cutscene("brutalbang.webm")

    scene town


    show jim


    j "Hello there fren"

    j "How can help?"

    j "Sorry for bad englis."

    return
