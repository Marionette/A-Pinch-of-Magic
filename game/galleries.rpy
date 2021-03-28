################################################################################
## Initialization
################################################################################

init offset = -1

################################################################################
## Gallery  ####################################################################
################################################################################
init:
  image cg kiana human = "images/cg/Human Kiana cg.png"
  image cg kiana mermaid = "images/cg/Mermaid Kiana cg.png"
  image cg mikhail good v = "images/cg/Mikhail good cg v 1920.png"
  image cg mikhail sad v = "images/cg/Mikhail sad cg v.png"
  image cg mikhail good vn = "images/cg/Mikhail good cg vn 1920.png"
  image cg mikhail sad vn = "images/cg/Mikhail sad cg vn.png"
  
  image cg_kiana_human_button = "images/cg/Human_Kiana_cg_thumb.png"
  image cg_kiana_mermaid_button = "images/cg/Mermaid_Kiana_cg_thumb.png"
  image cg_mikhail_good_v_button = "images/cg/Mikhail_good_cg_v_thumb.png"
  image cg_mikhail_sad_v_button = "images/cg/Mikhail_sad_cg_v_thumb.png"
  
  image gallerylock_button = "gui/button/gallery_locked.png"

init python:
    g_cg = Gallery()

    g_cg.button("cg kiana human")
    g_cg.image("cg kiana human")
    g_cg.unlock("cg kiana human")

    g_cg.button("cg kiana mermaid")
    g_cg.image("cg kiana mermaid")
    g_cg.unlock("cg kiana mermaid")

    g_cg.button("cg mikhail good v")
    g_cg.unlock_image("cg mikhail good v")
    g_cg.unlock_image("cg mikhail good vn")

    g_cg.button("cg mikhail sad v")
    g_cg.unlock_image("cg mikhail sad v")
    g_cg.unlock_image("cg mikhail sad vn")
    
    g_cg.locked_button = "gallerylock_button"

## CG Gallery screen ##################################################################
screen gallery():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("Gallery"), extra_navigation=True):

        grid 2 2:
            xpos 60
            ypos -60
            xspacing 30
            yspacing 10

            # Call make_button to show a particular button.
            button:
              background "gui/button/gallery_locked.png"
              foreground "gui/button/gallery_foreground_idle.png"
              hover_foreground "gui/button/gallery_foreground_hover.png"
              add g_cg.make_button("cg kiana human", "cg_kiana_human_button", xalign=0.5, yalign=0.55) xoffset -5 yoffset -5
            button:
              background "gui/button/gallery_locked.png"
              foreground "gui/button/gallery_foreground_idle.png"
              hover_foreground "gui/button/gallery_foreground_hover.png"
              add g_cg.make_button("cg kiana mermaid", "cg_kiana_mermaid_button", xalign=0.5, yalign=0.55) xoffset -5 yoffset -5
            button:
              background "gui/button/gallery_locked.png"
              foreground "gui/button/gallery_foreground_idle.png"
              hover_foreground "gui/button/gallery_foreground_hover.png"
              add g_cg.make_button("cg mikhail good v", "cg_mikhail_good_v_button", xalign=0.5, yalign=0.55) xoffset -5 yoffset -5
            button:
              background "gui/button/gallery_locked.png"
              foreground "gui/button/gallery_foreground_idle.png"
              hover_foreground "gui/button/gallery_foreground_hover.png"
              add g_cg.make_button("cg mikhail sad v", "cg_mikhail_sad_v_button", xalign=0.5, yalign=0.55) xoffset -5 yoffset -5
              
################################################################################
init:
  image promo1 = "images/promo/Violora_Varsha_Misha.png"
  image promo2 = "images/promo/APinchOfMagic_VarshaxMikhail.png"
  image promo3 = "images/promo/li2.png"
  image promo4 = "images/promo/Male_love_interest.png"
  image promo5 = "images/promo/VarshaxMikhail.png"
  image promo6 = "images/promo/Varshan_fanart_Silver Hatsuyuki.png"
  image promo7 = "images/promo/(Mustacheskulls).png"
  image promo8 = "images/promo/promoart_keith-1.png"
  
  image promo1_button = "images/promo/Violora_Varsha_Misha_thumb.png"
  image promo2_button = "images/promo/APinchOfMagic_VarshaxMikhail_thumb.png"
  image promo3_button = "images/promo/li2_thumb.png"
  image promo4_button = "images/promo/Male_love_interest__thumb.png"
  image promo5_button = "images/promo/VarshaxMikhail_thumb.png"
  image promo6_button = "images/promo/Varshan_fanart_Silver_Hatsuyuki_thumb.png"
  image promo7_button = "images/promo/(Mustacheskulls)_thumb.png"
  image promo8_button = "images/promo/promoart_keith-1_thumb.png"
  
  
  $promo_image_list = [ 
                        ["promo1", "promo1_button", "Violora"],
                        ["promo2", "promo2_button", "Enyaline"],
                        ["promo3", "promo3_button", "fairiberri"],
                        ["promo4", "promo4_button", "Kelsiy Bean"],
                        ["promo5", "promo5_button", "Ohisashi"],
                        ["promo6", "promo6_button", "Silver Hatsuyuki"],
                        ["promo7", "promo7_button", "Mustacheskulls"],
                        ["promo8", "promo8_button", "GoingGoingKeith"],
                        ]
  $promo_image_count = 0
  $promo_gallery_pages = 0
  $promo_current_page = 0

init python:
    g_promo = Gallery()

    g_promo.button("promo1")
    g_promo.image("promo1")
    g_promo.button("promo2")
    g_promo.image("promo2")
    g_promo.button("promo3")
    g_promo.image("promo3")
    g_promo.button("promo4")
    g_promo.image("promo4")
    g_promo.button("promo5")
    g_promo.image("promo5")
    g_promo.button("promo6")
    g_promo.image("promo6")
    g_promo.button("promo7")
    g_promo.image("promo7")
    g_promo.button("promo8")
    g_promo.image("promo8")
    
    g_promo.locked_button = "gallerylock_button"
    
## Promo Gallery screen ##################################################################
screen promo_gallery():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("Gallery"), extra_navigation=True):
        
        $promo_image_count = len(promo_image_list)
        $promo_gallery_pages = int(len(promo_image_list)/4.0)
        $promo_offset = promo_current_page*4
        
        $ next_promo_page = promo_current_page + 1     
        $ prev_promo_page = promo_current_page - 1          
        if next_promo_page > promo_gallery_pages:
            $ next_promo_page = promo_gallery_pages     
        if prev_promo_page < 0:
            $ prev_promo_page = 0
            
        grid 2 2:
            xpos 60
            ypos -170
            xspacing 30
            yspacing 10

            # Call make_button to show a particular button.

            for i in range(4):
              if promo_offset + i < promo_image_count:
                vbox:
                  button:
                    background "gui/button/gallery_locked.png"
                    foreground "gui/button/gallery_foreground_idle.png"
                    hover_foreground "gui/button/gallery_foreground_hover.png"
                    add g_promo.make_button(promo_image_list[promo_offset+i][0], promo_image_list[promo_offset+i][1], xalign=0.5, yalign=0.55) xoffset -5 yoffset -5
                  $artist_name = promo_image_list[promo_offset+i][2]
                  text "[artist_name]" xalign 0.5
              else:
                   null



        ## Buttons to access other pages.
        hbox:
                style_prefix "page"
                xfill True
                xsize 1200
        
                xalign 0.2
                yalign 1.0
        
                spacing gui.page_spacing
        
                textbutton _("<") action [SetVariable('promo_current_page', prev_promo_page), ShowMenu("promo_gallery")]
                
                for i in range(1, 7):
                  if (i-1 < len(promo_image_list)/float(4)):
                    textbutton "[i]" action [SetVariable('promo_current_page', i-1), ShowMenu("promo_gallery")]    
        
                textbutton _(">") action [SetVariable('promo_current_page', next_promo_page), ShowMenu("promo_gallery")]

################################################################################
## Music Box  ##################################################################
################################################################################

## Music Box setup #############################################################

init python:
    mr = MusicRoom()
    
    ######## ADD MUSIC FILES HERE ##############
    
    # Add music file references here.
    # The format goes:
    # ["path to music file.ogg",'Title', 'Composer']
    
    song_list = [ 
                  ["audio/music/Cafe Theme (final).ogg",'Cafe Theme', 'Juudenki'],
                  ["audio/music/Kiana's Theme (final).ogg",'Kiana\'s Theme', 'Juudenki'],
                  ["audio/music/Mikael's Theme.ogg",'Mikael\'s Theme', 'Juudenki'],
                  ["audio/music/Sad Theme (final).ogg",'Sad Theme', 'Juudenki'],
                  ["audio/music/Title Track (final).ogg",'Title Track', 'Juudenki'],
                ]
    
    # This lists default values for song_name and song_description to prevent errors.
    song_name = ""
    song_description = ""
    
    # This automatically adds an mr.add record for every song in the list.
    # Songs are always unlocked while always_unlocked = True.
    for track in song_list:
        mr.add(track[0], always_unlocked = True, action=[SetVariable('current_track', track[0]), SetVariable("song_name",track[1]),SetVariable("song_description",track[2])])
    
    #default to the first song    
    current_track = song_list[0][0] 
    
## Music Box screen ############################################################

screen musicbox():

    default loopMatch = ""
    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("Music Box"), extra_navigation=True):
    
        if not renpy.music.is_playing():
          add "gui/overlay/main_menu_circle.png" yoffset -50 xalign 0.5 yalign 0.5 at circle_fade_mr()
        else:
          add "gui/overlay/main_menu_circle.png" yoffset -50  xalign 0.5 yalign 0.5 at circle_rotate_mr()

        hbox:
          xfill True
          vbox:
            style_prefix "playlist"
            spacing 20
                  
            $count = 0
            label "Tracks:"
            for track in song_list:
              textbutton "[track[1]]"  xoffset 50 action  mr.Play(track[0])#[SetVariable('current_track', track[0]), mr.Play(track[0])]
              $count +=1
          
        vbox:
            xalign 0.5
            yalign 0.5
            xoffset 10
            xfill True
            vbox:
              xalign 0.5 yalign 0.55
              yoffset -100
              spacing 15
              label song_name:
                  xalign 0.5
                  text_size 85
                  text_outlines [ (5, "#fb81", 0, 0), (3, "#fb82", 0, 0),  (1, "#fb84", 0, 0) ]
              text song_description.upper():
                  xalign 0.5
          
            vbox:
              xalign 0.5 yalign 0.55
              spacing 10
              style_prefix "playback"
              frame:
                background None
                area (0,0, 400, 160)
                hbox:
                  xalign 0.5
                  textbutton "Previous":
                      action [
                              mr.Previous()
                              ]
                  if not renpy.music.is_playing():
                    textbutton "Play":
                        action [
                                SetVariable('current_track', renpy.music.get_playing()), 
                                mr.Play(current_track)
                                ]
                  else:
                    textbutton "Pause":
                        action [
                                SetVariable('current_track', renpy.music.get_playing()),
                                mr.Stop()
                                ]
                  
                  textbutton "Next":
                      action [
                              mr.Next()
                              ]
    
    # Make music change upon entering / exiting room.
    on "replace" action Stop("music")
    on "replaced" action Play("music", config.main_menu_music, fadeout=1.0)
    
style playlist_button is gui_button
style playlist_button_text is gui_button_text
style playback_button is radio_button
style playback_button_text is radio_button_text

style playlist_button:
    right_padding 90
    top_padding 30
    idle_background Frame("gui/button/button_idle.png", Borders(0, 0, 80, 0))
    hover_background Frame("gui/button/button_hover.png", Borders(0, 0, 80, 0))
    selected_background Frame("gui/button/button_hover.png", Borders(0, 0, 80, 0))
    #xsize 550
    ysize 100
    
style playlist_button_text:
    hover_outlines [ (5, "#fb81", 0, 0), (3, "#fb82", 0, 0),  (1, "#fb84", 0, 0) ]
    xalign 0.0

style playback_button:
  xsize 250