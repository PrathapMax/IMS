import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    text = input("New data: ")
    print("Now Place your Tag to write")
    reader.write(text)
    print("Written")

finally:
    GPIO.cleanup()