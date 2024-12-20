b...
b...
Online

kant — 7/16/2024 9:51 PM
เข้าดิสได้ปะ
Tawan∆~ — 7/16/2024 9:51 PM
// C++ code
#define P1 2
#define P2 3
#define P3 4
void setup()
{
  pinMode(P1, OUTPUT);
  pinMode(P2, OUTPUT);
  pinMode(P3, OUTPUT);
}

void loop()
{ 
  pinMode(P2, OUTPUT);
  digitalWrite(P1, LOW); 
  digitalWrite(P2, HIGH);
  pinMode(P3, INPUT);
  delay(500);//1

  digitalWrite(P1, HIGH); 
  digitalWrite(P2, LOW);
  pinMode(P3, INPUT);
  delay(500);//2

  pinMode(P3, OUTPUT);
  pinMode(P1,INPUT); 
  digitalWrite(P2, LOW);
  digitalWrite(P3, HIGH);
  delay(500);//3

  pinMode(P1,INPUT); 
  digitalWrite(P2, HIGH);
  digitalWrite(P3, LOW);
  delay(500);//4
 
  pinMode(P1, OUTPUT);
  digitalWrite (P1,LOW); 
  pinMode(P2,INPUT);
  digitalWrite(P3, HIGH);
  delay(500);//5

  digitalWrite (P1,HIGH); 
  pinMode(P2,LOW);
  digitalWrite(P3, LOW);
  delay(500);//5
}
Image
kant — 7/24/2024 12:00 PM
Attachment file type: unknown
-Fake_News.goodnotes
272.90 KB
kant — 7/24/2024 4:36 PM
#define button1 3
#define button2 4
#define button3 2

#define LED_R 12
#define LED_Y 11
#define LED_G 10



void setup()
{
      pinMode(LED_R,OUTPUT);
      pinMode(LED_Y,OUTPUT);
      pinMode(LED_G,OUTPUT);
    pinMode(button1,INPUT);
    pinMode(button3,INPUT_PULLUP);


    attachInterrupt(1,REDALLCLOSE,RISING);
    attachInterrupt(0,ALLCLOSE,FALLING);


}





void loop()
{
    digitalWrite(LED_R,LOW);
    digitalWrite(LED_Y,LOW);
    digitalWrite(LED_G,HIGH);
      delay(7000);

    digitalWrite(LED_G,LOW);
    digitalWrite(LED_R,LOW);
      digitalWrite(LED_Y,HIGH);
      delay(3000);

    digitalWrite(LED_G,LOW);
    digitalWrite(LED_Y,LOW);
      digitalWrite(LED_R,HIGH);
      delay(5000);

}


void REDALLCLOSE(){
      digitalWrite(LED_Y,LOW);
      digitalWrite(LED_G,LOW);
    digitalWrite(LED_R,HIGH);
    delay(500000);
    digitalWrite(LED_R,LOW);



}


void ALLCLOSE(){
      digitalWrite(LED_Y,LOW);
    digitalWrite(LED_G,LOW);
    digitalWrite(LED_R,LOW);
    delay(500000);

}
K just landed. — 7/24/2024 5:43 PM
Tawan∆~ — 7/24/2024 5:43 PM
Attachment file type: unknown
ด๊กต้าแห่งRI.goodnotes
298.82 KB
Tawan∆~ — 7/24/2024 5:44 PM
กรณ์ๆอันนี้นะ
K — 7/24/2024 5:44 PM
Ok
Tawan∆~ — 7/24/2024 5:44 PM
มีอะไรให้ทำบอกได้นะ
K — 7/24/2024 5:45 PM
ได้ๆกินข้าวแปป
Tawan∆~ — 7/24/2024 9:06 PM
วิเคราะห์1(ข้อ2)
Attachment file type: unknown
ด๊กต้าแห่งRI.goodnotes
437.17 KB
K — 7/24/2024 9:12 PM
Attachment file type: unknown
RI.goodnotes
875.93 KB
Tawan∆~ — 7/24/2024 9:29 PM
Attachment file type: unknown
ด๊กต้าแห่งRI.goodnotes
755.64 KB
Attachment file type: acrobat
ข้อ2.pdf
1.00 MB
Attachment file type: unknown
ด๊กต้าแห่งRI.goodnotes
755.64 KB
Tawan∆~ — 7/24/2024 9:48 PM
ไฟล์ ข้อ2 @K
kant — 7/25/2024 10:06 AM
https://discord.com/invite/gtXkMwKG
K — 8/7/2024 3:30 PM
#define replay 13
#define record 4
const int speakerPin = 3;
#define Note_C 262
#define Note_D 294
#define Note_E 330
#define Note_F 349
#define Note_G 392
#define Note_A 440
#define Note_B 494
#define Note_C1 523 //กำหนดDutyของแต่ละNote

const int tones[]={Note_C,Note_D,Note_E,Note_F,Note_G,Note_A,Note_B,Note_C1};
int recordArr[100];
int reset[100]={};
int recPosition=0;
void setup()
{
  Serial.begin(9600);
  for(int i=4;i<=13;i++){
  pinMode(i,INPUT);
  }
}


void loop()
{ 
  for(int i=5;i<=12;i++){
    if(digitalRead(i)==1){
      tone(speakerPin,tones[i-5]);
      delay(500);
      noTone(speakerPin);
      recordArr[recPosition]=tones[i-5];
      recPosition=recPosition+1;
    }
  }

  if(digitalRead(13)==1){
    for(int k=0;k<recPosition;k++){
    tone(speakerPin,recordArr[k]);
      delay(500);
      noTone(speakerPin);
    }
  }
 
  if(digitalRead(4)==1){
  recPosition=0;
    }



}
K — 8/9/2024 10:12 PM
bro
ทำไมกุทำตามในคลิบแล้วมันไม่ได้วะ
debug
ข้อ palindrome
kant — 8/9/2024 10:14 PM
อะไรวะ
K — 8/9/2024 10:32 PM
คือกุใช้debugไม่เป็น555
kant — 8/9/2024 10:33 PM
5555555
ดูคลิปไป 
K — 8/10/2024 9:41 AM
ดูแล้วแต่ทำแบบเขาไม่ได้อ่ะ https://youtu.be/NJYcRcqPyOw?si=tiqMN0MvY_7SdrXO
YouTube
ProgrammingKnowledge
Debugging C Program with Visual Studio Code (VSCode)
Image
ถ้าทำได้ขอมุมอร่อยหน่อยไม่ไหวละ5555
kant — 8/10/2024 7:41 PM
55555
ยังไม่ได้เริ่มเลย
Tawan∆~ — 9/3/2024 5:34 PM
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#ifdef _WIN32
#include <windows.h>  // For Sleep() on Windows
#else
Expand
gameofLife.txt
4 KB
Chat GPT 555
Tawan∆~ — 10/22/2024 5:10 PM
Attachment file type: document
RobotCarReport.docx
969.22 KB
A wild b... appeared. — 11/3/2024 8:56 PM
K — 11/4/2024 8:54 AM
มาๆ
มะกี้คุยกะแม่
b... — 11/4/2024 10:16 AM
https://new.reg.kmitl.ac.th/reg/#/teach_table?mode=by_class&selected_year=2567&selected_semester=2&selected_faculty=90&selected_department=90&selected_curriculum=x&selected_class_year=1&search_all_faculty=false&search_all_department=false&search_all_curriculum=true&search_all_class_year=false
Registration System KMITL
ระบบลงทะเบียนเรียน สถาบันเทคโนโลยีพระจอมเกล้าเจ้าคุณทหารลาดกระบัง
Image
b... — 11/4/2024 10:24 AM
Image
K — 11/4/2024 10:58 AM
Attachment file type: spreadsheet
Template KMITL Folder.xlsx
61.14 KB
Tawan∆~ — 12/6/2024 7:49 PM
def findpalin(num):
    if not(num.isnumeric()):
        return "Invalid"
    num=int(num)
    if(num<=1):
        return "Invalid"
Expand
w01_lab_2.py
1 KB
Tawan∆~ — 12/6/2024 8:06 PM
def multi(value):
    a=list(value)
    check1=0
    check2=0
    for i in a:
        if i=='[':
Expand
w01_lab_6.py
2 KB
xldn hopped into the server. — 12/9/2024 7:11 PM
Tawan∆~ — 12/10/2024 10:03 PM
Attachment file type: acrobat
แผนการศึกษา 90642118 APPLICATION SOFTWARE FOR BUSINESS 2-2567.pdf
9.21 MB
Tawan∆~ — Today at 3:49 PM
https://discord.gg/8jM8aEqK
Tawan∆~ — Today at 4:18 PM
{} | 'python' | 50
{'python': 50} | 'calculus' | 60
{'math': 80, 'science': 70} | 'english' | 90
{} | 'physics' | -10
{'history': 65} | 'history' | 75
{} | ' ' | 55
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5} | 'f' | 6
{'subject1': 100} | 'subject1' | 0
{} | 'programming' | 100
{'Math': 95, 'Physics': 92, 'Chemistry': 88} | 'Biology' | 90
for score in list(subject_score.values()):
        if score<0: score=0
        result+=score 
        count+=1
    result=result/count
    return f"{result:.2f}"
Tawan∆~ — Today at 4:34 PM
https://drive.google.com/drive/u/0/folders/1LCGunJtiq3L0V7gc9P2WbEt1pRhK2Ev9
Google Drive: Sign-in
Access Google Drive with a Google account (for personal use) or Google Workspace account (for business use).
K — Today at 4:46 PM
return F"{to_dic}, Average score: {Average:.2f}"
Tawan∆~ — Today at 4:59 PM
subject_score = {k:v for (k,v) in subject_score.items() if v>=0 and k !=''}
b... — Today at 10:20 PM
new_record = eval(dictionary_record.replace("'", """))
https://www.geeksforgeeks.org/python-convert-string-dictionary-to-dictionary/
GeeksforGeeks
Convert String Dictionary to Dictionary Python - GeeksforGeeks
A Computer Science portal for geeks. It contains well written, well thought and well explained computer science and programming articles, quizzes and practice/competitive programming/company interview Questions.
Image
K — Today at 10:43 PM
import json
def update_records(value):
    new_value = ""
    for i in range(len(value)):
        # Append all characters, including spaces
        if value[i] == ' ':
Expand
lab2_5.py
3 KB
import json
def update_records(value):
    new_value = ""
    for i in range(len(value)):
        # Append all characters, including spaces
        if value[i] == ' ':
Expand
lab2_5.py
3 KB
﻿
import json
def update_records(value):
    new_value = ""
    for i in range(len(value)):
        # Append all characters, including spaces
        if value[i] == ' ':
            # Only keep the space if it's between two alphabetic characters
            if i > 0 and i < len(value) - 1 and value[i-1].isalpha() and value[i+1].isalpha():
                new_value += value[i]
        else:
            new_value += value[i]

    value = new_value
    
    try:
        # Split value into dictionary_record, id1, property1, and value1
        dictionary_record, id1, property1, value1 = value.split("|")
        if(value1 == "''"):
           value1 = ''
        
    except ValueError:
        print("Error: Input does not contain the expected number of parts.")
        return None

    # dictionary_record = [i for i in dictionary_record if i != ' ']
    # dictionary_record = "".join(dictionary_record)
    dic = {}
    record_collection = {}
    dictionary_record = dictionary_record[1:-1]
    id_in,to_dic = dictionary_record.split(":",1)
    #record_collection = json.loads(to_dic)  
    #dictionary_record = dictionary_record.split(":")
    #if(property1 == "Track"):
    try:
        # Parse the JSON string in to_dic
        to_dic = to_dic.replace("'",'"')
        record_collection = json.loads(to_dic)
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in the dictionary.")
        return None
    
    
    if(property1 == 'tracks'):
        if 'tracks' in record_collection:
            record_collection['tracks'].append(value1.strip()) #ต่อเพิ่ม
        else:    
            record_collection['tracks'] = [value1.strip()] #เพิ่ม list
    elif property1 != '' and value1.strip() != '':
        record_collection[property1] = value1.strip()   
    elif property1.strip() != '' and value1.strip() == '':
        if property1.strip() in record_collection:
         del record_collection[property1.strip()]

 
    new_dict = {id1.strip(): record_collection}
    
    


    
    return new_dict

# def jesus(first):
#     first1 = [i for i in first if i != "{" and i != "}"]
#     first1 = "".join(first1)
    

#     return first1
    
try:
    value = input()
    
    output = update_records(value)
    print(output)
except:
    print("Invalid")
lab2_5.py
3 KB