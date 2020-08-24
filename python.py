from flask import Flask, render_template, jsonify
import requests
import json
import os

class Obj0(object):
    def __init__(date, obj1):
        self.date = date
        self.obj1 = obj1

    def make_obj0(date, obj1):
        obj0 = Obj0(date, obj1)
        return obj0

    def make_serial0(date, obj1):
        return {"date": date, "obj1": obj1}


class Obj1(object):
    def __init__(type, menus, time, timeList):
        self.type = type
        self.menus = menus
        self.time = time
        self.timeList = timeList

    def make_obj1(type, menus, time, timeList):
        obj1 = Obj1(type, menus, time, timeList)
        return obj1

    def make_serial1(type, menus, time, timeList):
        return {"type": type, "menus": menus, "time": time, "timeList" : timeList}



def api_test():
    # accessing the files
    f = open("menus.json", "r")
    data = json.loads(f.read())
    # dictionary for time open
    timeDictionary = {
        "Monday": {
            "BREAKFAST": "7:15 AM to 9:00 AM",
            "LIGHT BREAKFAST": "10:00 AM to 11:00 AM",
            "LUNCH": "11:30 AM to 1:00 PM",
            "LIGHT LUNCH": "1:30 PM to 5:00 PM",
            "DINNER": "5:30 PM to 7:00 PM",
        },
        "Tuesday": {
            "BREAKFAST": "7:15 AM to 9:00 AM",
            "LIGHT BREAKFAST": "10:00 AM to 11:00 AM",
            "LUNCH": "11:30 AM to 1:00 PM",
            "LIGHT LUNCH": "1:30 PM to 5:00 PM",
            "DINNER": "5:30 PM to 7:00 PM",
        },
        "Wednesday": {
            "BREAKFAST": "7:15 AM to 9:00 AM",
            "LIGHT BREAKFAST": "10:00 AM to 11:00 AM",
            "LUNCH": "11:30 AM to 1:00 PM",
            "LIGHT LUNCH": "1:30 PM to 5:00 PM",
            "DINNER": "5:30 PM to 7:00 PM",
        },
        "Thursday": {
            "BREAKFAST": "7:15 AM to 9:00 AM",
            "LIGHT BREAKFAST": "10:00 AM to 11:00 AM",
            "LUNCH": "11:30 AM to 1:00 PM",
            "LIGHT LUNCH": "1:30 PM to 5:00 PM",
            "DINNER": "5:30 PM to 7:00 PM",
        },
        "Friday": {
            "BREAKFAST": "7:15 AM to 9:00 AM",
            "LIGHT BREAKFAST": "10:00 AM to 11:00 AM",
            "LUNCH": "11:30 AM to 1:00 PM",
            "LIGHT LUNCH": "1:30 PM to 5:00 PM",
            "DINNER": "5:30 PM to 7:00 PM",
        },
        "Saturday": {
            "BREAKFAST": "7:15 AM to 9:00 AM",
            "LIGHT BREAKFAST": "9:00 AM to 10:00 AM",
            "LUNCH": "11:30 AM to 1:00 PM",
            "LIGHT LUNCH": "",
            "DINNER": "5:30 PM to 7:00 PM",
        },
        "Sunday": {
            "BREAKFAST": "",
            "LIGHT BREAKFAST": "",
            "LUNCH": "11:30 AM to 1:00 PM",
            "LIGHT LUNCH": "",
            "DINNER": "5:30 PM to 7:00 PM",
        },
    }
    
    timeDictionary1 = {
        "Monday": {
            "BREAKFAST": [7.25, 9.0],
            "LIGHT BREAKFAST": [0.0, 0.0],
            "LUNCH": [11.5, 13.0],
            "LIGHT LUNCH": [0.0, 0.0],
            "DINNER": [17.5, 19.0]
        },
        "Tuesday": {
            "BREAKFAST": [7.25, 9.0],
            "LIGHT BREAKFAST": [0.0, 0.0],
            "LUNCH": [11.5, 13.0],
            "LIGHT LUNCH": [0.0, 0.0],
            "DINNER": [17.5, 19.0]
        },
        "Wednesday": {
            "BREAKFAST": [7.25, 9.0],
            "LIGHT BREAKFAST": [0.0, 0.0],
            "LUNCH": [11.5, 13.0],
            "LIGHT LUNCH": [0.0, 0.0],
            "DINNER": [17.5, 19.0]
        },
        "Thursday": {
            "BREAKFAST": [7.25, 9.0],
            "LIGHT BREAKFAST": [0.0, 0.0],
            "LUNCH": [11.5, 13.0],
            "LIGHT LUNCH": [0.0, 0.0],
            "DINNER": [17.5, 19.0]
        },
        "Friday": {
            "BREAKFAST": [7.25, 9.0],
            "LIGHT BREAKFAST": [0.0, 0.0],
            "LUNCH": [11.5, 13.0],
            "LIGHT LUNCH": [0.0, 0.0],
            "DINNER": [17.5, 19.0]
        },
        "Saturday": {
           "BREAKFAST": [7.25, 9.0],
           "LIGHT BREAKFAST": [0.0, 0.0],
            "LUNCH": [11.5, 13.0],
            "LIGHT LUNCH": [0.0, 0.0],
            "DINNER": [17.5, 19.0]
        },
        "Sunday": {
            "BREAKFAST": [0.0, 0.0],
            "LIGHT BREAKFAST": [0.0, 0.0],
            "LUNCH": [11.5, 13.0],
            "LIGHT LUNCH": [0.0, 0.0],
            "DINNER": [17.5, 19.0],
        },
    }

    # date I need to create api objects
    day = 0
    week = ""
    type = ""
    setMenu = set()
    arrMenu = []
    openTime = ""
    #to find the missing menus types and set it to null
    listMenuType = ["BREAKFAST", "LIGHT BREAKFAST", "LUNCH","LIGHT LUNCH", "DINNER"]
    

    lst1 = []
    # loops through json
    for i in range(0, len(data["Date"])):
        lst0 = []
        hashmap1 = {}
        timeTypeFood = data["Date"][i]
        date = timeTypeFood["Time"]
        print(date)
        # to get the day only so that phone can compare the clicked day with this day
        wordList = date.split(", ")
        word = wordList[1]
        week = wordList[0]
        day = int(word[-2:])
        typeFood = timeTypeFood["TypeFood"]
        currMenuType = []
        missingTypes = []
        for j in range(0, len(typeFood)):
            hashmap = {}
            setMenu = set()
            arrMenu = []
            typeTableStationMenu = typeFood[j]
            type = typeTableStationMenu["Type"]
            currMenuType.append(type)
            print("hello")
            print(typeTableStationMenu)
            
            menu = typeTableStationMenu["Menus"]
            for k in range(0, len(menu)):
                menuObj = menu[k]
                food = menuObj["Menu"]
                setMenu.add(food)
            
            # remove the duplicates
            arrMenu = list(setMenu)

            object1 = Obj1.make_serial1(type, arrMenu, timeDictionary[week][type], timeDictionary1[week][type])
            lst0.append(object1)
        
        missingTypes = list(set(listMenuType) - set(currMenuType))
        for missing in missingTypes:
            object1 = Obj1.make_serial1(missing, [], "",[])
            lst0.append(object1)
        object0 = Obj0.make_serial0(day, lst0)
        lst1.append(object0)
    return lst1

app = Flask(__name__, template_folder=".")

@app.route("/")
def homepage():
    with open('menus.json', 'r') as f:
    	return render_template("templates/python.html", menus=json.loads(f.read())["Date"])


#a route to return all of the available menus.
@app.route("/api/v1/menus/all", methods = ["GET"])
def api_all():
    return jsonify(api_test())

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 33507))
    app.run(host = '0.0.0.0', port = port, debug = True)
