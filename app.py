from flask import Flask
from flask import jsonify
import numpy as np
import pandas as pd
app = Flask(__name__)
list_ = []
@app.route('/Predict', methods=['GET'])
def pred():
    recom=[]
    if(list_!=[]):
        try:
            for mov in list_:
                output = best_movies_by_genre(mov,3)
                recom_movies = recom_movies + output            
            return jsonify({'movies':recom_movies})
        except Exception as e:
            return "No recommendations" + str(e.args)
    else:
        return "No recommendations"  
