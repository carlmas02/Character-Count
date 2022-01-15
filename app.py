from flask import Flask,render_template,request,redirect,url_for
import test


app = Flask(__name__)


@app.route("/",methods = ["GET","POST"])
def home():

	if request.method == "POST":
		text = request.form.get('name')

		data = test.count_text(text)
		#return data

		word_data = data['words']
		# return word_data
		return render_template("index.html",data = data,word_data=word_data)



	return render_template("index.html")




if __name__ == '__main__':
	app.run(debug= True)


