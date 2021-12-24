# import boto3
#
# translate = boto3.client(service_name='translate', region_name='us-east-1', use_ssl=True)
#
# test = input("Mời bạn nhập: ")
# lang_flag_pairs = [("he", "🇮🇱"), ("fr", "🇫🇷"), ("de", "🇩🇪"),
#                    ("es", "🇪🇸"), ("pt", "🇵🇹"), ("zh", "🇨🇳"),
#                    ("ja", "🇯🇵"), ("ru", "🇷🇺"), ("it", "🇮🇹"),
#                    ("zh-TW", "🇹🇼"), ("tr", "🇹🇷"), ("cs", "🇨🇿"), ("th", "Thái Lan"), ("vi", "Việt Nam")]
# for lang, flag in lang_flag_pairs:
#     print(flag)
#     print(translate.translate_text(
#         Text=test,
#         SourceLanguageCode="en",
#         TargetLanguageCode=lang
#     )['TranslatedText'])
#
#
# result = translate.translate_text(Text=test,
#             SourceLanguageCode="en", TargetLanguageCode="vi")
# print('TranslatedText: ' + result.get('TranslatedText'))
# print('SourceLanguageCode: ' + result.get('SourceLanguageCode'))
# print('TargetLanguageCode: ' + result.get('TargetLanguageCode'))

from flask import render_template, Flask

app = Flask(__name__)

@app.route("/")
def test():
    return render_template("index.html")
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)