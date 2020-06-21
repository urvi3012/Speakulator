from flask import Flask, render_template, url_for
#from forms import Reg_Form, Login_Form
import speech_recognition as sr
import re
app = Flask(__name__)


@app.route('/t')
def get_ses():
	return render_template('try.html')


@app.route('/hy')
def done():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source)
		print("Speak:")
		audio = r.record(source, duration=10)

	text = r.recognize_google(audio)
	text2 = re.split(' ', text)
	new_list = [int(item) for item in text2 if item.isdigit()]
	new_list2 = [item for item in text2 if not item.isdigit()]
	print(new_list)
	print(new_list2)
	i = 1
	sum = new_list[0]
	print(type(sum))
	for suv in new_list2:
		if suv == '+':
			sum += new_list[i]
			i = i + 1
		elif suv == '-':
			sum -= new_list[i]
			i = i + 1
		elif suv == 'multiply' or suv == 'multiplied' or suv == '*' or suv == 'into':
			sum *= new_list[i]
			i = i + 1
		elif suv == 'divide' or suv == 'divided' or suv == 'by' or suv == 'dividedby' or suv == '/':
			sum /= new_list[i]
			i = i + 1
		else:
			sum += 0
	print("You said " + text)
	print(" = ")
	return str(sum)
  

if __name__ == '__main__':
	app.run(debug=True)
