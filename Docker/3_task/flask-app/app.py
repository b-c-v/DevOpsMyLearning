import random
from flask import Flask, render_template

app = Flask(__name__)

images = [
"https://weldering.com/sites/default/files/neprovar_2.jpg",
"https://weldering.com/sites/default/files/bryzgi.jpg",
"https://weldering.com/sites/default/files/vozobnovlenie.jpg",
"https://weldering.com/sites/default/files/svishch_3.jpg",
"https://weldering.com/sites/default/files/sluchaynaya_duga_1.jpg",
"https://weldering.com/sites/default/files/poverhnostnye_pory_1.jpg",
"https://weldering.com/sites/default/files/neravnomernaya_shirina_shva_1.jpg",
"https://weldering.com/sites/default/files/podrez.jpg",
"https://weldering.com/sites/default/files/neprovar_3.jpg"
]
@app.route('/')
def index():
   url = random.choice(images)
   return render_template('index.html', url=url)
if __name__ == "__main__":
   app.run(host="0.0.0.0")
