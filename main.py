from flask import render_template, Flask, request
import boto3
import json
account_id = "ASIAQTOOB77BALX2LW4R"
account_key = "nnmS57PAawyd6crU6NUcP+vkmEqohiQ081JSqcnK"
account_token = "FwoGZXIvYXdzEMT//////////wEaDIRztvvOdA9fyMsLTyLPAc51rWk1+PCd48ug+wAc6vEafrNv/EsjyurkDDxxrvUkQpmj1HCpkUkJAbXXLJM3u/Cvwkbzi/XFpxmdUvgz00ooPmpLXb7kaXGXFpPlsme4LtAAXG+r9ZAOloSRbblgKx7glbLYUpkpKGAAqq8L+Qd+dkF5iP7exa2EjG9LxAq1d4+gwKoWEjsy3StPzIFo6DWLIF8EfuZ8CIZpTzESygbOQrnn/wV57MDB0PFJhqVG7obGvicTioMs/FssZvmSRcBwkWwzuSw86bb0MDlMpSjQiaiOBjItKC3ayHvdVQr8Qt9HIJOIXfmxUrJ1qd2fMlbHV0/5E5l0SFI+lZ8ZgHYcndj/"

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