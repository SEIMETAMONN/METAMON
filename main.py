def on_gesture_logo_up():
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

def on_button_pressed_b():
    basic.show_icon(IconNames.ASLEEP)
input.on_button_pressed(Button.B, on_button_pressed_b)
