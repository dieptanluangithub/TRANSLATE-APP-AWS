from flask import render_template, Flask, request
import boto3
import json
account_id = "ASIAQTOOB77BE3JMBY4G"
account_key = "DnYcFl5DdSdgAd2kztGvLIBkjkgKiyTbtUSvd7iW"
account_token = "FwoGZXIvYXdzEBwaDKaLP88M7Uhys+mhhiLPAQ0HroVNQCSIO4C8dhPYXlOTlmX/vtTgpZcmczM2aiagIK7G66SFmlY6gfWf79zpl63hGpv8BlAXFuLxfkN2qSMJV6nK2w9MLDbUxzhK38595iAVCP9FFOr/yqHTiyJXt3FLw8rimW6nBFKTYJq0q0p+qkckCJx01zugIrVTCD+cscDRXMzDQvSbqNwEjHWOSGFi7KEPIbP8Q7PjeTMlDfn/C4OgWuQaHrjpOeE+YphSlOB+3jnWJIAOlAOKPYsN/KMx25Q+XAU9hmHacl3E5SiYrruOBjItEc7OewBnLvijZ93plHydRnw1u1SO2pRz1YlhkZte/vVqun8y6fjDwwte13pj"
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