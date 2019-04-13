import speech_recognition as sr 
import RPi.GPIO as GPIO

#Remote GPIO libraries
from gpiozero import LED


pin1 = 13
pin2 = 19
pin3 = 26
Redled = LED(pin1)
Blueled = LED(pin2)  
def listener():
    # Record Audio
	r = sr.Recognizer()
	r.energy_threshold = 300
	with sr.Microphone(sample_rate = 44100) as source:
		print("Say something!")
		audio = r.listen(source,None, 4)

		data = ""
		try:
			print("processing")
			data = r.recognize_google(audio)
			print("Google Speech Recognition " + data)
              
		except sr.UnknownValueError:
			print("Google Speech Recognition could not understand your audio")
		except sr.RequestError as e:
			print("Could not request results from Google Speech Recognition service; {0}".format(e))
		return data 
  
def checkspeech(phrase): 

	if "white" in phrase.lower():
		ledcontrol('blue')
	elif "fire" in phrase.lower():
		ledcontrol('red')

	
	return
 
#LED Control
#Resistors needed at GPIO to LED, RED= 330 Ohm, Green=165 ohm, Blue=110 ohm.
def ledcontrol(color):
    print('Turning on LED to ' + color)
    
    if color == 'red':
		Redled.on()
		Blueled.off()
	if color == 'blue':
		Redled.off()
		Blueled.on()
   
while 1:
	# calling main function 
	phrase = listener()
	conversation = checkspeech(phrase)
