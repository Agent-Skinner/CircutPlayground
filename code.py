import audioio
import board
import digitalio
import neopixel
import touchio

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.01)




# enable the speaker
spkrenable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
spkrenable.direction = digitalio.Direction.OUTPUT
spkrenable.value = True

# make the 2 input buttons
buttonA = digitalio.DigitalInOut(board.BUTTON_A)
buttonA.direction = digitalio.Direction.INPUT
buttonA.pull = digitalio.Pull.DOWN

buttonB = digitalio.DigitalInOut(board.BUTTON_B)
buttonB.direction = digitalio.Direction.INPUT
buttonB.pull = digitalio.Pull.DOWN

# The two files assigned to buttons A & B
audiofiles = ["rimshot.wav", "laugh.wav", "sad_trombone.wav","air_horn.wav"]

capPins = (board.A1, board.A2, board.A3, board.A4, board.A5,
           board.A6, board.A7)

touchPad = []
for i in range(7):
    touchPad.append(touchio.TouchIn(capPins[i]))

def play_file(filename):
    print("Playing file: " + filename)
    wave_file = open(filename, "rb")
    with audioio.WaveFile(wave_file) as wave:
        with audioio.AudioOut(board.A0) as audio:
            audio.play(wave)
            while audio.playing:
                pass
    print("Finished")


while True:
    if buttonA.value:
        pixels[0]= pixels[1]=pixels[2]=pixels[3]=pixels[4]=(255,0, 0)
        play_file(audiofiles[0])
        pixels[0]= pixels[1]=pixels[2]=pixels[3]=pixels[4]=(0,0, 0)
    if buttonB.value:
        pixels[5]= pixels[6]=pixels[7]=pixels[8]=pixels[9]=(0,255, 0)
        play_file(audiofiles[1])
        pixels[5]= pixels[6]=pixels[7]=pixels[8]=pixels[9]=(0,0, 0)
    # Trombone
    if touchPad[0].value:
        pixels[5]= pixels[6]=pixels[7]=pixels[8]=pixels[9]=(0,0, 255)
        play_file(audiofiles[2])
        pixels[5]= pixels[6]=pixels[7]=pixels[8]=pixels[9]=(0,0, 0)
    # Air Horn
    if touchPad[1].value:
        pixels[5]= pixels[6]=pixels[7]=pixels[8]=pixels[9]=(255,255, 0)
        play_file(audiofiles[3])
        pixels[5]= pixels[6]=pixels[7]=pixels[8]=pixels[9]=(0,0, 0)
