from flask import make_response

from Main import *


@app.route('/deleteData', methods=(['GET', 'PUT']))
def delete_data():
    if request.args.get("StartDate") is None:
        return make_response("{\"Bad Request\": \"Please check the arguments provided.\"}", 400)

    startDate = request.args.get("StartDate")

    for row in fileContents:
        if (row['Date'] == startDate):

            fileContents.remove(row)
            with open('Data/AAPL.csv', 'w') as csvfile:
                fieldnames = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(fileContents)

            return make_response("{\"Entry Deleted\": \"Success.\"}", 200)

    return make_response("{\"Method Not Allowed\": \"Could not find entry to delete, please check the date.\"}", 405)