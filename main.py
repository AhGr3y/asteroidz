# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

def main():
    print("Starting asteroids!")

# This line ensures the main() function is only called when this file is run directly;
#  it won't run if it's imported as a module.
# It's considered the "pythonic" way to structure an executable program in Python.
# Technically, the program will work fine by just calling main(),
# but you might get an angry letter from Guido van Rossum if you don't.
if __name__ == "__main__":
    main()