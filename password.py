from flask import Flask, request, render_template
from forms import GeneratorForm
import random
app = Flask(__name__)
app.config.from_object('config')
app.debug = True


@app.route('/')
@app.route('/index')
def index():
	form = GeneratorForm()
	if 'lowerRange' in request.args:
		lowerRange = int(request.args['lowerRange'])
		upperRange = int(request.args['upperRange'])
		wordcut(lowerRange, upperRange)
		words = []
		double = False

		if 'alternating' in request.args:
			if 'double' in request.args:
				double = True
			optimize(double)
		
		j = 0
		while j < 10:
			word = generate()
			if 'myNumber' in request.args:
				word += str(random.randrange(9))
			if 'passLength' in request.args:
				passLength = int(request.args['passLength'])
				if len(word) < passLength:
					words.append(word)
					j += 1
			else:
				words.append(word)
				j += 1
		a = 0
		while a < 10:
			words[a] = substitute(words[a])
			a += 1
		return render_template('results.html', words = words)
	else:
		return render_template('index.html', form=form)

def generate():
	resultstring = ''
	i = 0
	while i < 4:
		wordfile = open('newwords.txt', 'r')
		result = random_line(wordfile)
		if 'capitalOne' in request.args and i == 0:
			result = str.title(result)
		if 'capitalTwo' in request.args and i == 1:
			result = str.title(result)
		if 'capitalThree' in request.args and i == 2:
			result = str.title(result)
		if 'capitalFour' in request.args and i == 3:
			result = str.title(result)
		resultstring += result
		i = i + 1
	wordfile.close()
	return resultstring

def wordcut(low, high):
	searchfile = open("wordlist.txt", "r")
	array = []
	for line in searchfile:
		if len(line) > low and len(line) < high: 
			array.append(line)
	searchfile.close()

	printfile = open("newwords.txt", "w")
	for i in array:
		printfile.write(i)
	printfile.close()

def random_line(afile):
	line = next(afile)
	for num, aline in enumerate(afile):
		if random.randrange(num + 2): continue
		line = aline
	return line

def optimize(double):
	searchfile = open("newwords.txt", "r")
	array = []
	leftList  = ["q","w","e","r","t","a","s","d","f","g","z","x","c","v","b"]
	for line in searchfile:
		k = 0
		points = 0
		left = True
		last = ''
		if k % 2 == 0:
			left = True
		else:
			left = False
		while k < len(line):
			if left:
				if last and double:
					if line[k] == last:
						points += 1
				last = line[k]
				if line[k] in leftList:
					points += 1
					left = False
					k += 1
				else:
					left = True
					k += 1
			else:
				if last and double:
					if line[k] == last:
						points += 1
				last = line[k]
				if line[k] in leftList:
					left = True
					k +=1
				else:
					points += 1
					left = False
					k += 1

		if points > 5:
			array.append(line)


	searchfile.close()

	printfile = open("newwords.txt", "w")
	for i in array:
		printfile.write(i)
	printfile.close()

def substitute(password):
	zero = False
	one = False
	two = False
	three = False
	four = False
	five = False
	six = False
	seven = False
	eight = False
	if 'zero' in request.args:
		zero = True
	if 'one' in request.args:
		one = True
	if 'two' in request.args:
		two = True
	if 'three' in request.args:
		three = True
	if 'four' in request.args:
		four = True
	if 'five' in request.args:
		five = True
	if 'six' in request.args:
		six = True
	if 'seven' in request.args:
		seven = True
	if 'eight' in request.args:
		eight = True

	subList = ["o", "l", "z", "e", "a", "s", "g", "t", "b"]
	i = 0
	while i < len(password):
		if password[i] == "o" and zero:
			password = replace(password, "o", "0", i)
		if password[i] == "l" and one:
			password = replace(password, "l", "1", i)
		if password[i] == "z" and two:
			password = replace(password, "z", "2", i)
		if password[i] == "e" and three:
			password = replace(password, "e", "3", i)
		if password[i] == "a" and four:
			password = replace(password, "a", "4", i)
		if password[i] == "s" and five:
			password = replace(password, "s", "5", i)
		if password[i] == "g" and six:
			password = replace(password, "g", "6", i)
		if password[i] == "t" and seven:
			password = replace(password, "t", "7", i)
		if password[i] == "b" and eight:
			password = replace(password, "b", "8", i)
		i += 1
	return password

def replace(old, letter, number, i):
	new = old[:i] + number + old[i + 1:]
	return new

if __name__ == '__main__':
   app.run()
