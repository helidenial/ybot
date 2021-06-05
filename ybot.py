from weakref import WeakKeyDictionary
from flask import Flask, render_template, request
import threading
from goto import visit

app = Flask(__name__)


@app.route('/',methods =["GET"])
def home():
    print(request.args)
    if len(request.args) == 0:
        pass
    else:
        url = request.args.get('url')
        views = int(request.args.get('noOfViews'))
        threads = int(request.args.get('threads'))
        duration = int(request.args.get('duration'))
        for i in range(0,threads):    
            threading.Thread(target=visit, args=(url, views, duration, )).start()

    return render_template('index.html')

if __name__ =="__main__":
    app.run()





