from flask import Flask, request
import random
app = Flask(__name__)
app.debug = True   # need this for autoreload as and stack trace


@app.route('/')
def password():
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
		return sendPage(words)
	else:
		return sendForm()

def sendForm():
	return '''
	<html>
		<body>
			<form method='get'>
				<label for="lowerRange">Minimum Characters</label>
				<input id="lowerRange" type="number" name="lowerRange" min="4" max="15" value="4"/>
				<label for="upperRange">Maximum Characters</label>
				<input id="upperRange" type="number" name="upperRange" min="4" max="15" value="15"/><br>

				<label for="passLength">Password Maximum Length</label>
				<input id="passLength" type="number" name="passLength" min="30" max="55" value="55" /><br>

				<label for="alternating">Optimize Typing Speed</label>
				<input id="alternating" type="checkbox" name="alternating" />
				<label for="double">Include Double Letters in Speed</label>
				<input id="double" type ="checkbox" name="double" /><br>

				<label for="zero">0 = O</label>
				<input id="zero" type="checkbox" name="zero" />

				<label for="one">1 = L</label>
				<input id="one" type="checkbox" name="one" />

				<label for="two">2 = Z</label>
				<input id="two" type="checkbox" name="two" /><br>

				<label for="three">3 = E</label>
				<input id="three" type="checkbox" name="three

				<label for="four">4 = A</label>
				<input id="four" type="checkbox" name="four" />

				<label for="five">5 = S</label>
				<input id="five" type="checkbox" name="five" /><br>

				<label for="six">6 = G</label>
				<input id="six" type="checkbox" name="six" />

				<label for="seven">7 = T</label>
				<input id="seven" type="checkbox" name="seven" />

				<label for="eight">8 = B</label>
				<input id="eight" type="checkbox" name="eight" /><br>

				<label for="capitalOne">Capitalize First Word</label>
				<input id="capitalOne" type="checkbox" name="capitalOne" />

				<label for="capitalTwo">Capitalize Second Word</label>
				<input id="capitalTwo" type="checkbox" name="capitalTwo" />

				<label for="capitalThree">Capitalize Third Word</label>
				<input id="capitalThree" type="checkbox" name="capitalThree" />

				<label for="capitalFour">Capitalize Fourth Word</label>
				<input id="capitalFour" type="checkbox" name="capitalFour" /><br>

				<input type="submit" value="Generate"/>
			</form>
		</body>
	</html>
	'''

def sendPage(words):
	return '''
		<html>
		<body>
			<ul id='passwordList'>
				<li>{0}</li>
				<li>{1}</li>
				<li>{2}</li>
				<li>{3}</li>
				<li>{4}</li>
				<li>{5}</li>
				<li>{6}</li>
				<li>{7}</li>
				<li>{8}</li>
				<li>{9}</li>
			</ul>
		</body>
	</html>
	'''.format(words[0], words[1], words[2], words[3], words[4], words[5], words[6], words[7], words[8], words[9])

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

		if points > 4:
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
