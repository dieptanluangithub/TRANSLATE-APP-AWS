# QUY TRÌNH TRIỂN KHAI ỨNG DỤNG "DTL TRANSLATE APP"
Demo sản phẩm: 
## Công nghệ sử dụng:
1. Amazon Translate
2. Amazon Polly
3. Amazon Textract
4. Python 3.8
5. Flask Frameword
6. Thư viện boto3
7. Bootstrap 4
8. HTML/CSS
9. AWS CLI (AWS Command Line Interface)
## Yêu cầu cần có để cài đặt:
1. Tài khoản AWS
2. IAM User: ghi nhớ aws_access_key_id, aws_secret_access_key và aws_region
3. Thư viện boto3, flask bằng lệnh pip install boto3, pip install flask. 
4. Cài đặt thư viện giao diện dòng lệnh AWS CLI MSI bản dành cho Windowns(64-bit): https://awscli.amazonaws.com/AWSCLIV2.msi
5. Cài đặt cấu hình người dùng với các AWS Access Key ID, AWS Secret Access Key, Default region name, Default output format tương ứng.
## Các bước cài đặt:
1. Clone dự án về máy: https://github.com/dieptanluangithub/NHOM27-TRANSLATE-APP.git
2. Tạo tài khoản AWS
3. Ghi nhớ các thông tin cấu hình như:
* aws_access_key_id
* aws_secret_access_key
* aws_session_token
* aws_region
4. Mở file main.py và file index.html để cấu hình thông tin tài khoản AWS của bạn
5. Chạy file main.py để xem kết quả.
![image](https://user-images.githubusercontent.com/82451887/187751901-90ad34c9-f6d6-49de-8922-530e0aa3700f.png)
![image](https://user-images.githubusercontent.com/82451887/187751928-5d612af5-7a80-410c-b995-af7f743c878c.png)
![image](https://user-images.githubusercontent.com/82451887/187751954-9439fb83-c13f-40bd-bdb3-4c9d1f25b3f1.png)
- Chuyển file hình ảnh thành văn bản.
+ Đầu vào:
![image](https://user-images.githubusercontent.com/82451887/187752064-e16b1fc7-0560-4c22-8133-aaf2a18627cd.png)

+ Đầu ra:
 ![image](https://user-images.githubusercontent.com/82451887/187752043-71d4d4d6-3ed7-45dd-873e-a4ba9b2d3311.png)

+ Download file vừa chuyển từ ảnh sang văn bản
 ![image](https://user-images.githubusercontent.com/82451887/187752179-e1e35bab-7594-422f-9f36-626fa433da97.png)
![image](https://user-images.githubusercontent.com/82451887/187752192-33bcb01f-d4a0-4a51-aa6f-c5b7e9353e69.png)

 


