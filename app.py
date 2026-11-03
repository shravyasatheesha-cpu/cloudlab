
import azure.functions as func
import datetime
import json

app = func.FunctionApp()

@app.route(route="datetime", auth_level=func.AuthLevel.ANONYMOUS)
def get_datetime(req: func.HttpRequest) -> func.HttpResponse:

    now = datetime.datetime.now(datetime.timezone.utc)

    result = {
        "message": "Current Date and Time",
        "date": now.strftime("%d-%m-%Y"),
        "time": now.strftime("%H:%M:%S")
    }

    return func.HttpResponse(
        json.dumps(result),
        mimetype="application/json",
        status_code=200
    )
