from flask import make_response
from Main import *


@app.route('/addData', methods=(['GET', 'POST']))
def add_data():
    # if request.method == 'POST':
    if request.args.get("StartDate") is None or request.args.get("Open") is None \
            or request.args.get("High") is None or request.args.get("Low") is None or \
            request.args.get("Close") is None or request.args.get("Adj Close") is None \
            or request.args.get("Volume") is None:
        return make_response("{\"Bad Request\": \"Please check the arguments provided.\"}", 400)

    startDate = request.args.get("StartDate")
    openPrice = request.args.get("Open")
    highPrice = request.args.get("High")
    lowPrice = request.args.get("Low")
    closePrice = request.args.get("Close")
    adjClosePrice = request.args.get("Adj Close")
    volume = request.args.get("Volume")

    for row in fileContents:
        if (row['Date'] == startDate):
            print(row)
            return make_response("{\"Method Not Allowed\": \"Date already exists, make a request to /updateData"
                                 " if the data should be updated. This route is only for creating a new entry.\"}", 405)

    with open('Data/AAPL.csv', 'a', newline='') as csvfile:
        fieldnames = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writerow({'Date': startDate, 'Open': openPrice, 'High': highPrice, 'Low': lowPrice,
                         'Close': closePrice, 'Adj Close': adjClosePrice, 'Volume': volume})
        fileContents.append({'Date': startDate, 'Open': openPrice, 'High': highPrice, 'Low': lowPrice,
                             'Close': closePrice, 'Adj Close': adjClosePrice, 'Volume': volume})

    return make_response("{\"Entry Added\": \"Success.\"}", 200)
