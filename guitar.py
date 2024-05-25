#!/usr/bin/env python3

from guitarstring import GuitarString
from stdaudio import play_sample
import stdkeys
import pygame

keyboard = "q2we4r5ty7u8i9op-[=]"
note_strings = []

for i in range(len(keyboard)):
    freq = 440.0 * (1.059463 ** (i - 12))
    note_strings.append(GuitarString(freq))

if __name__ == '__main__':
    # Initialize window
    stdkeys.create_window()
 
    n_iters = 0
    play = set()
    location = 0
    while True:
        # It turns out that the bottleneck is in polling for key events
        # for every iteration, so we'll do it less often, say every 
        # 1000 or so iterations
        if n_iters == 1000:
            stdkeys.poll()
            n_iters = 0
        n_iters += 1

        #maybe make a set of plucked string
        # check if the user has typed a key; if so, process it
        if stdkeys.has_next_key_typed():
            key = stdkeys.next_key_typed().lower()

            if key == 'z':
                break
            if key in keyboard and key != '':
                location = keyboard.index(key)
                played = note_strings[location]
                played.pluck()
                play.add(played)
                
        sample = 0 # compute the superposition of samples

        for note in play:
            sample += note.sample()
            note.tick()

            if(note.buffer.is_empty()):
                play.remove(note)

        play_sample(sample) # play the sample on standard audio
       # advance the simulation of each guitar string by one step
        
    pygame.quit()
