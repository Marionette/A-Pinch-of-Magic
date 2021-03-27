﻿################################################################################
## Initialization
################################################################################

init offset = -1

transform circle_rotate(_xpos=0, _ypos=0):
    xpos _xpos 
    ypos _ypos
    parallel:
      alpha 0.2
      linear 5.0 alpha 1.0
      linear 5.0 alpha 0.2
      repeat
    parallel:
      rotate 0
      linear 30.0 rotate 360
      repeat
 #at menu_item_move(-500, timeOffset+2.1)
 
transform fire_fade(_timeStart=0.6):
    alpha 1.0
    time _timeStart
    block:
      linear 5.0 alpha 0.2
      linear 5.0 alpha 1.0
      repeat
 
transform slide_appear(_timeStart=0.6, _xpos=0):
    alpha 0.0
    xpos 2000
    time _timeStart
    parallel:
      linear 5.0 alpha 1.0
    parallel:
      easein 2.0 xpos _xpos
 
transform slide(_timeStart=0.6, _xpos=0):
    xpos 2000
    time _timeStart
    easein 2.0 xpos _xpos
 

transform menu_item_move(_ystart=-1000, _timeStart=0.6):
    subpixel True
    yoffset _ystart
    time _timeStart
    easein_bounce 2.2 yoffset 0
    #ease .2 yoffset 0
    
transform open:
    ypos -50
    on hover:
        linear 0.5 rotate 20
        linear 0.5 rotate -20
        repeat
    on idle:
        easein_bounce 0.5 rotate 0
    on selected_idle:
        linear 0.5 rotate 0
        
################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding


style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5
    outlines [ (5, "#fb81", 0, 0), (3, "#fb82", 0, 0),  (1, "#fb84", 0, 0) ]

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu and not renpy.get_screen('choice'):     
        imagebutton auto "gui/button/button_history_%s.png":
            xalign 1.0
            hovered [Show("qm_tooltip",ttcontent="Log",ttxpos=1880,ttypos=97)]
            unhovered Hide("qm_tooltip")
            action [Hide("qm_tooltip"), ShowMenu('history')]
            
        imagebutton auto "gui/button/button_quick_hide_%s.png":
            xpos 1820 ypos 753
            hovered [Show("qm_tooltip",ttcontent="Hide UI",ttxpos=1830,ttypos=827)]
            unhovered Hide("qm_tooltip")
            action [Hide("qm_tooltip"), HideInterface()]
            
        vbox:
          xpos 1605 ypos 850
          spacing -5
          hbox:    
            spacing -5
            imagebutton auto "gui/button/button_quick_auto_%s.png":
                hovered [Show("qm_tooltip",ttcontent="Auto",ttxpos=1625,ttypos=840)]
                unhovered Hide("qm_tooltip")
                action [Hide("qm_tooltip"), Preference("auto-forward", "toggle")]
        
            imagebutton auto "gui/button/button_quick_save_%s.png":
                hovered [Show("qm_tooltip",ttcontent="Save",ttxpos=1710,ttypos=840)]
                unhovered Hide("qm_tooltip")
                action [Hide("qm_tooltip"), ShowMenu('save')]
        
            imagebutton auto "gui/button/button_quick_options_%s.png":
                hovered [Show("qm_tooltip",ttcontent="Options",ttxpos=1790,ttypos=840)]
                unhovered Hide("qm_tooltip")
                action [Hide("qm_tooltip"), ShowMenu('preferences')]
          hbox:    
            spacing -5
            imagebutton auto "gui/button/button_quick_skip_%s.png":
                hovered [Show("qm_tooltip",ttcontent="Skip",ttxpos=1625,ttypos=1007)]
                unhovered Hide("qm_tooltip")
                action [Hide("qm_tooltip"), Skip()] alternate [Hide("qm_tooltip"), Skip(fast=True, confirm=True)]
        
            imagebutton auto "gui/button/button_quick_load_%s.png":
                hovered [Show("qm_tooltip",ttcontent="Load",ttxpos=1710,ttypos=1007)]
                unhovered Hide("qm_tooltip")
                action [Hide("qm_tooltip"), ShowMenu('load')]
        
            imagebutton auto "gui/button/button_quick_home_%s.png":
                hovered [Show("qm_tooltip",ttcontent="Home",ttxpos=1795,ttypos=1007)]
                unhovered Hide("qm_tooltip")
                action [Hide("qm_tooltip"), MainMenu()]
            


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
#init python:
#    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")

    
style caption_med:
    #font gui.adv_font_face
    size 34 * 0.6
    bold True
    color "#ffffff"
    
screen qm_tooltip(ttcontent,ttxpos,ttypos):
    zorder 9999
    text ttcontent:
        style "caption_med"
        xpos ttxpos ypos ttypos
        #at gui_fade_inout(0.0,0.3)

################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():
    add "gui/overlay/menu_circle_small.png" at circle_rotate(1600, 250)

    vbox:
        style_prefix "navigation"

        #xpos gui.navigation_xpos
        xalign 1.0
        yalign 0.5
        yoffset 100

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start() xoffset 130 at slide(0.1, 0)

        else:

            #textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save") xoffset 130  at slide(0.2, 0)

        textbutton _("Load") action ShowMenu("load") xoffset 30  at slide(0.3, 0)

        textbutton _("Options") action ShowMenu("preferences") xoffset -10 at slide(0.4, 0)

        #if _in_replay:

        #    textbutton _("End Replay") action EndReplay(confirm=True)

        #elif not main_menu:

        #    textbutton _("Main Menu") action MainMenu()

        #textbutton _("About") action ShowMenu("about")

        #if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
        #    textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") action Quit(confirm=not main_menu) xoffset 30  at slide(0.5, 0)
            

        textbutton _("Return") action Return() xoffset 150  at slide(0.6, 0)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    idle_background Frame("gui/button/button_navi_idle.png", Borders(24, 24, 15, 24))
    hover_background Frame("gui/button/button_navi_hover.png", Borders(24, 24, 15, 24))
    selected_idle_background Frame("gui/button/button_navi_selected_idle.png", Borders(24, 24, 15, 24))
    selected_hover_background Frame("gui/button/button_navi_selected_hover.png", Borders(24, 24, 15, 24))
    ysize 119
    xsize 298
    xalign 0.5

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    xalign 0.5
    yalign 0.5


screen extra_navigation():
    add "gui/overlay/menu_circle_small.png" at circle_rotate(1600, 250)

    vbox:
        style_prefix "navigation"

        #xpos gui.navigation_xpos
        xalign 1.0
        yalign 0.5
        yoffset 100

        spacing gui.navigation_spacing

        textbutton _("Promo Art") action ShowMenu("extras") xoffset 130  at slide(0.2, 0)
        textbutton _("CG") action ShowMenu("extras") xoffset 30  at slide(0.3, 0)
        textbutton _("Music") action ShowMenu("extras") xoffset -10 at slide(0.4, 0)
        textbutton _("About") action ShowMenu("about") xoffset 30  at slide(0.5, 0)
        textbutton _("Return") action Return() xoffset 150  at slide(0.6, 0)
        textbutton _("Character") action ShowMenu("character_settings") xoffset 150  at slide(0.6, 0)


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    add gui.main_menu_background

    ## This empty frame darkens the main menu.
    frame:
        pass
    add "gui/overlay/main_menu_fire_left.png" at fire_fade(0.4)
    add "gui/overlay/main_menu_fire_right.png" at fire_fade(0.7)
    add "gui/overlay/main_menu_circle.png" at circle_rotate(800, -300)
    add "gui/overlay/main_menu_logo.png" at slide_appear(0.2, 0)


    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    #use navigation
    vbox:
        style_prefix "main_menu_nav"
        xpos 1480
        ypos 300
        spacing 60
        textbutton _("Start") action Start() xoffset -35 at slide(0.5, 0)
        textbutton _("Load") action ShowMenu("load") xoffset -205 at  slide(0.7, 0)
        textbutton _("Options") action ShowMenu("preferences") xoffset -405 at slide(0.9, 0)
        textbutton _("Gallery") action ShowMenu("extras") xoffset -400 at slide(1.1, 0)
        textbutton _("Quit") action Quit(confirm=not main_menu) xoffset -250 at slide(1.3, 0)
    
    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text
style main_menu_nav_vbox is vbox
style main_menu_nav_button is gui_button
style main_menu_nav_button_text is gui_button_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30
    
style main_menu_nav_button:
    properties gui.button_properties("navigation_button")
    right_padding 90
    top_padding 30
    idle_background Frame("gui/button/button_idle.png", Borders(0, 0, 80, 0))
    hover_background Frame("gui/button/button_hover.png", Borders(0, 0, 80, 0))
    ysize 89
    
style main_menu_nav_button_text:
    size gui.title_text_size
    color "#fff"
    font gui.name_text_font
    hover_outlines [ (5, "#fb81", 0, 0), (3, "#fb82", 0, 0),  (1, "#fb84", 0, 0) ]

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0, extra_navigation=False, return_only=False):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
        
    add "gui/overlay/game_menu.png" 
    add "gui/overlay/menu_fire_left.png" at fire_fade(0.4)
    add "gui/overlay/menu_fire_right.png" at fire_fade(0.7)
    add "gui/overlay/menu_fire_right2.png" at fire_fade(0.1)
    
    frame:
        style "game_menu_outer_frame"

        hbox:

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"
    
    #Change navigation depending on what type of screen is showing
    if return_only:
      textbutton _("Return"):
          style "return_button"
          action Return()
    else:
      if extra_navigation:
          use extra_navigation
      else:
          use navigation

    label title:
      style "game_menu_title_label"

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background None #"gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    #xpos 75
    ysize 180
    xalign 1.0

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5
    
style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45

style game_menu_title_label is game_menu_label
style game_menu_title_label_text is game_menu_label_text

style game_menu_title_label:
  xoffset -100
  yoffset 50
  
style game_menu_title_label_text:
    font gui.name_text_font
    outlines [ (5, "#fb81", 0, 0), (3, "#fb82", 0, 0),  (1, "#fb84", 0, 0) ]


screen game_menu_simple(title, scroll=None, yinitial=0.0, useBoxOverlay=True):

    style_prefix "game_menu_simple"

    if main_menu:
        add gui.main_menu_background
        
    add "gui/overlay/game_menu_simple.png" 
    if useBoxOverlay:
        add "gui/overlay/menu_frame_box.png"
    add "gui/overlay/menu_fire_left.png" at fire_fade(0.4)
    add "gui/overlay/menu_fire_right.png" at fire_fade(0.7)
    add "gui/overlay/menu_fire_right2.png" at fire_fade(0.1)
    
    frame:
        style "game_menu_simple_outer_frame"

        hbox:

            frame:
                style "game_menu_simple_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

            ## Reserve space for the navigation section.
            #frame:
            #    style "game_menu_navigation_frame"
                
    textbutton _("Return"):
        style "return_button"
        xalign 0.5
        yoffset 0
        action Return()

    label title:
      style "game_menu_title_label"

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")
        
style game_menu_simple_outer_frame is game_menu_outer_frame
style game_menu_simple_navigation_frame is game_menu_navigation_frame
style game_menu_simple_side is game_menu_side
style game_menu_simple_scrollbar is game_menu_scrollbar

style game_menu_simple_content_frame is game_menu_content_frame
style game_menu_simple_viewport is game_menu_viewport

style game_menu_simple_content_frame:
    left_margin 320
    right_margin 30
    top_margin 15
    bottom_margin 120
    
style game_menu_simple_viewport:
    xsize 1260

## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu_simple(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.name_text_size
    font gui.name_text_font

style about_text:
    size gui.text_size
    color gui.idle_color

## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.1
                yalign 0.1

                xspacing gui.slot_spacing*3
                yspacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        foreground "gui/button/slot_foreground.png"     
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) #xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"
                xfill True
                xsize 1200

                xalign 0.2
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                #if config.has_autosave:
                #    textbutton _("{#auto_page}A") action FilePage("auto")

                #if config.has_quicksave:
                #    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 6):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5
    xalign 0.25
    yoffset -150
    xoffset 120

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color
    size 85
    font gui.name_text_font
    hover_outlines [ (5, "#fb81", 0, 0), (3, "#fb82", 0, 0),  (1, "#fb84", 0, 0) ]

style page_button:
    properties gui.button_properties("page_button")
    xsize 50
    ysize 50

style page_button_text:
    properties gui.button_text_properties("page_button")
    selected_color "#ec81a8"
    hover_outlines [ (5, "#cfd1", 0, 0), (3, "#cfd2", 0, 0),  (1, "#cfd4", 0, 0) ]

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            vbox:
                style_prefix "slider"
                box_wrap True

                hbox:
                    vbox:
                      xminimum 350
                      label _("Text Speed")
                    null width (1 * gui.pref_spacing)+21

                    bar value Preference("text speed")
                    
                hbox:

                    vbox:
                      xminimum 350
                      label _("Auto Time")
                    null width (1 * gui.pref_spacing)+21

                    bar value Preference("auto-forward time")
            
                null height (2 * gui.pref_spacing)

                vbox:

                    if config.has_music:
                      hbox:
                        vbox:
                          xminimum 350
                          label _("Music Volume")
                        null width (1 * gui.pref_spacing)+21

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:
                      hbox:

                        vbox:
                          xminimum 350
                          label _("SFX Volume")
                        null width (1 * gui.pref_spacing)+21

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)

                        if config.has_music or config.has_sound or config.has_voice:
                            null width gui.pref_spacing

                            textbutton _("Mute All"):
                                action Preference("all mute", "toggle")
                                style "mute_all_button"


                    if config.has_voice:
                      hbox:
                        vbox:
                          xminimum 350
                          label _("Voice Volume")
                        null width (1 * gui.pref_spacing)

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

            null height (2 * gui.pref_spacing)

            vbox:
                box_wrap True

                hbox:
                    style_prefix "check"
                    vbox:
                      xminimum 350
                      label _("Skip Mode")
                    null width (1 * gui.pref_spacing)
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                if renpy.variant("pc") or renpy.variant("web"):

                    hbox:
                        style_prefix "radio"
                        vbox:
                          xminimum 350
                          label _("Display")
                        null width (1 * gui.pref_spacing)
                        textbutton _("Windowed") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                #hbox:
                #    style_prefix "radio"
                #    label _("Rollback Side")
                #    textbutton _("Disable") action Preference("rollback side", "disable")
                #    textbutton _("Left") action Preference("rollback side", "left")
                #    textbutton _("Right") action Preference("rollback side", "right")

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3
    xalign 1.0

style pref_label_text:
    yalign 1.0
    xalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    #foreground "gui/button/radio_[prefix_]foreground.png"
    idle_background Frame("gui/button/button_option_idle.png", Borders(24, 24, 15, 24))
    hover_background Frame("gui/button/button_option_hover.png", Borders(24, 24, 15, 24))
    selected_idle_background Frame("gui/button/button_option_selected_idle.png", Borders(24, 24, 15, 24))
    selected_hover_background Frame("gui/button/button_option_selected_hover.png", Borders(24, 24, 15, 24))
    xsize 314
    ysize 96
    yoffset 25

style radio_button_text:
    properties gui.button_text_properties("radio_button")
    size 36

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    #foreground "gui/button/check_[prefix_]foreground.png"
    idle_background Frame("gui/button/button_option_idle.png", Borders(24, 24, 15, 24))
    hover_background Frame("gui/button/button_option_hover.png", Borders(24, 24, 15, 24))
    selected_idle_background Frame("gui/button/button_option_selected_idle.png", Borders(24, 24, 15, 24))
    selected_hover_background Frame("gui/button/button_option_selected_hover.png", Borders(24, 24, 15, 24))
    xsize 314
    ysize 96
    yoffset 25

style check_button_text:
    properties gui.button_text_properties("check_button")
    size 36

style slider_slider:
    xsize 479
    ysize 69
    left_bar "gui/slider/bar_full.png"
    right_bar "gui/slider/bar_empty.png"
    thumb None
    yoffset 20

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu_simple(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")
    size gui.text_size
    color gui.idle_color

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:
        vbox:
            xalign .5
            yalign .1
            #spacing 125

            label _(message):
                style "confirm_prompt"
                xalign 0.5
                yalign 0.5

        hbox:
                xalign 0.5
                yalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background None #Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .1

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"
    color gui.idle_color
    size 50

style confirm_button:
    properties gui.button_properties("confirm_button")
    xsize 200
    ysize 200

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")
    font gui.name_text_font
    size 100
    hover_outlines [ (5, "#fb81", 0, 0), (3, "#fb82", 0, 0),  (1, "#fb84", 0, 0) ]


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 900


## Character Settings screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.
         
init -1 python:      
      
    def SetPronoun(pronoun):
        return [ SetField(persistent, "selected_pronoun", pronoun), If(not main_menu, RestartStatement()) ]

    #variables set with this dont update when persistent changes unless re-called
    def PronounPicker2(he, she, they):
            if persistent.pronoun == "he":
                return he
            elif persistent.pronoun == "she":
                return she
            else:
                return they
                
    class PronounPicker(store.object):
        def __init__(self, he, she, they):
            self.he = he
            self.she = she
            self.they = they
            

        #This should work and i've no idea why it doesnt. D;
        def __unicode__(self):
            if persistent.pronoun == "he":
                return str(self.he)
            elif persistent.pronoun == "she":
                return str(self.she)
            else:
                return str(self.they)

        def Get(self):
            if persistent.pronoun == "he":
                return str(self.he)
            elif persistent.pronoun == "she":
                return str(self.she)
            else:
                return str(self.they)

screen character_settings():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu_simple(_("Character Settings"), useBoxOverlay=False):

        style_prefix "about"
        
        hbox:
          xoffset -150
          imagebutton auto "gui/button/char_varsha_%s.png":
            selected_idle "gui/button/char_varsha_hover.png"
            action SetField(persistent, "selected_character", "varsha")
          
          vbox:
            xoffset 10
            style_prefix "radio"
            label _("Pronouns") xoffset -10 xalign 0.5
            null width (1 * gui.pref_spacing)
            textbutton _("He/Him") action SetPronoun("he")
            textbutton _("She/Her") action SetPronoun("she")
            textbutton _("They/Them") action SetPronoun("they")
            
          imagebutton auto "gui/button/char_varshan_%s.png":
            selected_idle "gui/button/char_varshan_hover.png"
            action SetField(persistent, "selected_character", "varshan")
                        
    add "gui/overlay/menu_circle_small.png" at circle_rotate(-360, 700)
    add "gui/overlay/menu_circle_small.png" at circle_rotate(1500, 700)


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.name_text_size
    font gui.name_text_font

style about_text:
    size gui.text_size
    color gui.idle_color
    
    
screen extras():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("Extras"), scroll="viewport", extra_navigation=True):
      text " "