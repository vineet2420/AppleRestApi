from flask import make_response

from Main import *


@app.route('/updateData', methods=(['GET', 'PUT']))
def update_data():
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

    i = 0
    for idx, row in enumerate(fileContents):
        if (row['Date'] == startDate):
            row = {'Date': startDate, 'Open': openPrice, 'High': highPrice, 'Low': lowPrice,
                   'Close': closePrice, 'Adj Close': adjClosePrice, 'Volume': volume}
            i = idx
            print("Here " + str(row) + "index: " + str(idx))

            fileContents[i] = row
            with open('Data/AAPL.csv', 'w') as csvfile:
                fieldnames = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(fileContents)

            return make_response("{\"Entry Updated\": \"Success.\"}", 200)

    return make_response("{\"Method Not Allowed\": \"Could not find date to update entry.\"}", 405)