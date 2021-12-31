from flask import render_template, Flask, request
import boto3
import json
account_id = "ASIAQTOOB77BECKAZCW4"
account_key = "xgBc28bfyNLm37zzYY1uSNsXtiKVVG7PsttnNr5v"
account_token = "FwoGZXIvYXdzEBYaDFV5nSvotgcS4L51BCLPAdE70b43Nlu6kP9k+u+BeJVbSqrHYo7PlG+ozl7gM4XOsa9Szw2kp8lz617nHJvK1cnLrpqspO6gLkSE5ygQeBUI1PJd0woDBxXzBaQu9T2W8eG8OOcXvz5TY4mCvIVx2dJIRFbdx6b3mVj2FhnFNTaIRZQSuhLTJrFsN2+TL6Lrx5Yq4oKEmSqBhPDeV7E2mvtsXwNjutRMO4dWLc3/vaF/2lWs1HJ0XVIkah+G0Ds7A+P4ORoxj7OugJMrH+78YUHamkDUEcJWHx95tYECRCianrqOBjIt9Fq4Bgd7E5vYnXeA+VO++Ph6Uy2Lu92mSchwFILOlDntZ6t1V4Df39jjPCu+"
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