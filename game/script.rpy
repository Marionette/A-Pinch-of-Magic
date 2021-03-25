# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define v = Character("Varshan")
define long = Character("Eileen Long Name")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    show Solid("#000000")

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    v "You've created a new Ren'Py game."

    v "Once you add a story, pictures, and music, you can release it to the world!"

    e "Once you add a story, pictures, and music, you can release it to the world!"

    long "Once you add a story, pictures, and music, you can release it to the world!"
    
    v "Rgerg th rthrt rt htfh rhrhfh  t rgerg th rthrt rt htfh rhrhfh  t rgerg th rthrt rt jkljkljlhtfh rhrhfh  tkljkljkl rgerg th rtjklhrt rt htfh rhrhfh  t rgerg th rjkljñkl."
    
    menu:
      "Option 1":
        pass
      "Rgerg th rthrt rt htfh rhrhfh  t rgerg th rthrt rt htfh rhrhfh":
        pass

    e "And again..."
    
    menu:
      "Menu Question"
      "Option 1":
        pass
      "Option 2":
        pass
      "Option 3":
        pass
      "Option 4":
        pass

    e "All done"
    # This ends the game.

    return
