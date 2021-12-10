from flask import make_response
from Main import *

@app.route('/getData', methods=('GET',))
def get_data():
    if request.args.get("Date") is not None and request.args.get("EndDate") is not None:
        startDate = request.args.get("StartDate")
        endDate = request.args.get("EndDate")
        rangedDate = []

        try:
            datetime.datetime.strptime(startDate, '%Y-%m-%d')
            datetime.datetime.strptime(endDate, '%Y-%m-%d')

            for row in fileContents:
                if time.strptime(startDate, "%Y-%m-%d") <= time.strptime(row['Date'], "%Y-%m-%d") <= time.strptime(endDate, "%Y-%m-%d"):
                    rangedDate.append(row)
            return make_response("{\"Data in range (" + startDate + " - " + endDate + ")\":" + str(rangedDate).replace("\'", "\"") + "}", 200)

        except ValueError as e:
            return make_response("{\"Method Not Allowed\": \"Please check date format.\"}", 405)

    elif request.args.get("Date") is not None:
        providedDate = request.args.get("Date")
        try:
            datetime.datetime.strptime(providedDate, '%Y-%m-%d')
            for row in fileContents:
                if (row['Date'] == providedDate):
                    return str(row).replace("\'", "\"")

            return make_response("{\"Method Not Allowed\": \"Date not found.\"}", 405)
        except ValueError as e:
            return make_response("{\"Method Not Allowed\": \"Please check date format.\"}", 405)

    else:
        return make_response("{\"AllData\":" + str(fileContents).replace("\'", "\"") + "}", 200)


@app.route('/calculate10DayAverage', methods=('GET',))
def calculate_ten_day_avg():
    sum = 0.0
    for row in fileContents[-10:]:
        sum = sum + float(row['Adj Close'])
    avg = sum / 10
    return make_response("{\"Ten Day Avg\": \"" + str(avg) + "\"}", 200)
