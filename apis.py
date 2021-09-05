from flask import Flask,jsonify, request
app = Flask(__name__)

new_arrivals_data=[
    {
        "type":"anarkali",
        "brand":"shreejee",
        "fabric":"cotton",
        "Number":20
    },
    {
        "type":"dhoti",
        "brand":"N/A",
        "fabric":"neted",
        "Number":20
    }
]

@app.route("/")
def man():
    print("i am creating first api in my life")
    return "manish first api data"

@app.route("/new-arrivals-manish-collection")
def manishdresses():
    return jsonify({
        "data":new_arrivals_data
    })

@app.route("/add-data",methods=['POST'])
def data ():
    data_available={
        "type":"kurta",
        "brand":"manish",
        "fabric":"cotton",
        "Number":1000
        }
    new_arrivals_data.append(data_available)
    return "succesfully"

if (__name__ == "__main__"): 
    app.run(debug=True)