from flask import render_template, Flask, request
import boto3
import json
account_id = "ASIAQTOOB77BLFQDDLF7"
account_key = "tpMq7GQ5f3swcvJKf9lxdd7acOUTTzSTq7i8JFRH"
account_token = "FwoGZXIvYXdzEOr//////////wEaDEtqabDoO33/tSwXYiLPAdjFo8NrQ5NygO1ylgI3RkIOfALkGWRX5e6/K8H4sneuOrQa/RGY+ZeJruXOzBRiY2UlE53BR8ME0r3HwyREWfwJZiyinmIWkY3xCdqJy5AMsAQ1MX5vs1tX5md5fJj2c6TyTBsVQpX2EGHzoQRDvcxU+1J6HbEYnvOY83g4DnUH4bmbvU1/8ZnuhVGat7LQyswJKjPMSGAnRw0OsMEJmbiLyoSbyi4dQ9/vJOiNdFuDIqGOnXw1zXuF61w5ijxnw4OeDz3s5Br/LAKNoCoEBCiYt7COBjItXWDTULIIvXGi/Y3xWMTfH30gS3PLFVlUyWNA7igwgGp06CUlG3wqMAm0rv6h"

def client():
    global account_id
    global account_key
    global account_token
    print(account_id, account_key, account_token)
    client = boto3.client("textract", aws_access_key_id=account_id,
                          aws_secret_access_key=account_key,
                          aws_session_token=account_token,
                          region_name='us-east-1')
    return client
app = Flask(__name__)

@ app.route("/", methods=["GET"])
def main():
    extractedText = ""
    responseJson = {

        "text": extractedText
    }
    return render_template("index.html", jsonData=json.dumps(responseJson))

@ app.route("/extracttext", methods=["POST"])
def extractImage():
    file = request.files.get("filename")
    binaryFile = file.read()
    textractclient = client()
    response = textractclient.detect_document_text(
        Document={
            'Bytes': binaryFile
        }
    )
    extractedText = ""
    for block in response['Blocks']:
        if block["BlockType"] == "LINE":
            extractedText = extractedText+block["Text"]+" "

    responseJson = {

        "text": extractedText
    }
    print(responseJson)
    return render_template("index.html", jsonData=json.dumps(responseJson))

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)