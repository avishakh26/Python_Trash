import time
import os
import pygame


pygame.mixer.init()
pygame.mixer.music.load("blucut.mp3")  # make sure the file is in the same folder
pygame.mixer.music.play()



lyrics = [
"I could walk you by, and I'll tell without a thought", 
"You'd be mine, would you mind if I took your hand tonight?",
"Know you're all that I want this life",
"",

"I'll imagine we fell in love",
"I'll nap under moonlight skies with you",
"I think I'll picture us, you with the waves",
"The ocean's colors on your face",
"I'll leave my heart with your air",
"So let me fly with you",
"Will you be forever with me?",
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    
def display_lyrics(lyrics):
    clear_screen()
    print("Blue -- yung kai:\n")
    
    for line in lyrics:
       for char in line:
           print(char, end='', flush=True)
           time.sleep(0.09)  
    print()
    time.sleep(1.2)
        
if __name__ == "__main__":
    display_lyrics(lyrics)