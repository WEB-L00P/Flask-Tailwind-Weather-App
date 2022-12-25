from flask import Flask,render_template,jsonify,request
import requests

# api key =60ee4d21d7994bde90b94446222412


app=Flask(__name__)

key = '60ee4d21d7994bde90b94446222412'


@app.route('/',methods=['GET','POST'])
def home():
    if request.method == "POST":
        q=request.form.get("city")
        url = f"http://api.weatherapi.com/v1/current.json?key={key}&q={q}"
        response = requests.request("GET",url).json()
    # <p>City : </p>
    #     <p>Country : </p>
    #     <p>Longitude : </p>
    #     <p>Latitude : </p>
    #     <p>Local Time : </p>
    #     <p>Temperature : </p>
    #     <p>Updated at : </p>
        data = {
     
        "city": response["location"]["name"],
        "country": response["location"]["country"],
        "lat": response["location"]["lat"],
        "lon": response["location"]["lon"],
        "time": response["location"]["localtime"],
        "temp": response["current"]["temp_c"],
        "updated": response["current"]["last_updated"],
        "icon": response["current"]["condition"]["icon"],
        }
        print(data["icon"])

    # print(response)
        return render_template('index.html',data=data)
    else:
        return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)