from flask import render_template, Flask, request
import boto3
import json
account_id = "ASIAQTOOB77BLATEXSMW"
account_key = "RW+oE6+OpZAj3vHFNjrmDFyfctx4OKY0/q0aWeri"
account_token = "FwoGZXIvYXdzENX//////////wEaDGuPU7vl4/v8UPS3KSLPAU174mWlWt8bwfZlAU29bOvI8EXdf0/mc7cBNDX7GjMpDcywAk+HzGtJTHhYPSeTGS0830RMZQFc5SvD0OSn4r9aI3c76oQ2bbGs8hV/VS4yiCf8ygItkurJ1EuhvLLfruuX1DaFqhTOBkKwVLgUHoP4mZqsT7Hh2MNKlI/aTtMT3/tk0xMNQbGFXxsVz+MDa5GIAsm1Dp+91RCs8FgAMiOgu9tjNJBqb69mAG7VgP0INDIZ+9BEtbcApgnAKSBjGRO1vCS9dzWkRSiCr/t45iiY8KuOBjItPxzbEFyqbvqo88F7On7zzjWtEIxnUJRQgz4Vn2LVtU32+fyh0lxj73PD42eH"

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