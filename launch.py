from flask import Flask
from flask import request
from flask import render_template
import spellD
import time
import os
app = Flask(__name__)


@app.route('/spell/')
def my_formSpell():
	return render_template("/spell/index.html")
@app.route('/spell/add')
def addSpellMenuS():
	return render_template("/spell/add.html")
@app.route('/spell/data')
def showDataSpell(names = None, des = None, seen = None):
	names = []
	des = []
	seen = []
	names = spellD.getNames()
	des = spellD.getDes()
	seen = spellD.getSeen()
	return render_template("/spell/data.html",names = names, des = des, seen = seen)

@app.route('/spell/addSpell',methods=['POST'])
def addSpelSpelll(name = None, des = None, seen = None, c = 0, conf = None):
	try:
		print "Be"
		c = 0
		conf = ""
		name = ""
		des = ""
		seen = ""
		print "a"
		name = request.form['name']
		des = request.form['des']
		seen = request.form['seen']
		print "c"
		c = spellD.addToData(name,des,seen)
		print str(c)
		if c == -1:
			conf = "Erorr Occured :("
			return render_template("/spell/add.html",conf =conf, color = color)
		else:
			conf = str(c)
			return render_template("/spell/conf.html",conf =conf,name = name, des = des, seen = seen)
	except Exception as e: print str(e)

@app.route('/spell/search',methods=['POST'])
def searchSpell(search = None,names = None, des = None, seen = None, count = 0):
	count = 0
	names= []
	des = []
	seen = []
	search = ""
	search = request.form['name']
	names = spellD.searchSpellData(search)
	for name in names:
		des.append(spellD.getDesByName(name))
		seen.append(spellD.getSeenByName(name))
	count = len(names)
	
	return render_template('/spell/results.html',names = names, des = des, seen = seen,count = count)





if __name__ == '__main__':
    app.run()


