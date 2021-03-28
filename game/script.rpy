
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
init:
    if persistent.selected_character is None:
        $selected_character = "varshan"
    if persistent.selected_pronoun is None:
        $selected_pronoun = "they"
        

    define e = Character("Eileen")
    define long = Character("Eileen Long Name")

    $character_name = "Varshan"

    define v = DynamicCharacter("character_name")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    show Solid("#000000")

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    
    scene cg kiana human
    v "You've created a new Ren'Py game."
    
    scene cg mikhail good v

    show eileen happy
    
    jump character_selection_test

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


label character_selection_test:
    
    e "Well hello there."
    
    e "whats you're name?"
    
    "my name?"
    
    python:
        character_name = renpy.input("What is your name?", length=32)
        character_name = character_name.strip()

        if not character_name:
             character_name = "Varshan"
         
    v "My name is [character_name]."
    
    e "And how would you describe yourself?"
    
    call screen character_settings()
    
    v "My pronouns are [persistent.selected_pronoun] and I look like [persistent.selected_character]."
    
    e "And who are you after?"
    
    call screen route_select()
    
    v "I'm aiming for [selected_route]"
    
    e "Thats great!"
    
    return