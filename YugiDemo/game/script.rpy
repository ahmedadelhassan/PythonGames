# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

init:
    $ e = Character('Eileen', color="#c8ffc8")

    image eileen happy = "eileen_happy.png"
    image bg table = "table.png"
    image dim = "#0008"
    image bg stars = "battle_field.jpg"
    image active card = "#0008"

    # Some styles for show text.
    $ style.centered_text.drop_shadow = (2, 2)
    $ style.centered_text.drop_shadow_color = "#000b"

label start:

    scene bg stars
#    show bg table at truecenter

    python:
        y = YugiDemo(1)
        y.set_sensitive(False)
        y.show()
#        y.show_hand()


label continue:

    hide dim
    hide eileen
    with dissolve

label quick_continue:
    
    while True:

        python:
            
            y.set_sensitive(True)
            y.draw_card(ui.interact())
            c = y.active_card(ui.interact())
            print c
#            active_card = "card/Deck_1.jpg" % c

        image active card = "card/Active_1.jpg"
        show dim
        show active card at truecenter
        $ renpy.pause()
        hide active card
        hide dim

            


    return
