#### This file contains tests to evaluate that your bot behaves as expected.
#### If you want to learn more, please see the docs: https://rasa.com/docs/rasa/user-guide/testing-your-assistant/

## normal path
* greeting: xin chào
  - utter_greet
* ask_point: tôi muốn tra cứu điểm chuẩn của đại học công nghệ
  - utter_ask_point

## normal path 3
* greeting: chào bạn
  - utter_greet
* ask_information: khoa công nghệ thông tin của trường đại học công nghệ học những gì
 - respond_ask_information
 - utter_continue


## normal path 3
* greeting: hello
  - utter_greet
* ask_information: tôi muốn tìm hiểu về điều kiện xét tuyển vào trường đại học công nghệ
 - respond_ask_information
 - utter_continue

## normal path 4
* ask_information: tôi muốn biết định hướng tương lai nếu học đại học công nghệ
  - respond_ask_information
  - utter_continue
## normal path 3
* greeting: chào bạn
  - utter_greet
* ask_information: để xét tuyển vào đại học công nghệ cần những gì
 - respond_ask_information
 - utter_continue

## normal path 4
* ask_information: học đại học công nghệ thì có thể có tương lai như thế nào
 - respond_ask_information
 - utter_continue

 ## normal path 4
* ask_information: địa điểm để nộp hồ sơ đăng ký nguyện vọng vào trường đại học công nghệ
 - respond_ask_information
 - utter_continue

## normal path 4
* ask_information: không nộp hồ sơ đúng hạn có làm sao không
 - respond_ask_information
 - utter_continue

## normal path 4
* ask_information: nộp hồ sơ muộn không sao đúng không
 - respond_ask_information
 - utter_continue

## normal path 4
* ask_information: nộp hồ sơ đợt hai ở đâu
 - respond_ask_information
 - utter_continue

## normal path 4
* ask_information: nộp hồ sơ muộn thì nộp ở đâu
 - respond_ask_information
 - utter_continue

 
## normal path 4
* ask_information: hạn cuối để nộp hồ sơ đợt một vào đại học công nghệ
 - respond_ask_information
 - utter_continue


## normal path 4
* ask_information: khi nào không nộp được hồ sơ cho trường
 - respond_ask_information
 - utter_continue


## normal path 4
* ask_information: khi nào không thể nộp lại hồ sơ cho trường đại học công nghệ nữa
 - respond_ask_information
 - utter_continue

## normal path 4
* ask_information: các ngành học của đại học công nghệ
 - respond_ask_information
 - utter_continue