init python:
    import common

# Calling scenes goes like this
label start:
    call test_scene from _call_test_scene
    # call another_scene from _call_another_scene

    return

label splashscreen:

    play sound 'movie/splash.mp4'
    show splash at top with dissolve
    with Pause(11.0)
    hide movie_cutscene with dissolve
    return