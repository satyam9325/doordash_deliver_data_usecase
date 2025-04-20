# doordash_deliver_data_usecase

This  assignment  involves  creating  an  automated  AWS-based  solution  for  processing  daily 
delivery  data  from  DoorDash.  JSON  files  containing  delivery  records  will  be  uploaded  to  an 
Amazon  S3  bucket.  An  AWS  Lambda  function,  triggered  by  the  file  upload,  will  filter  the 
records  based  on  delivery  status  and  save  the  filtered  data  to  another  S3  bucket. 
Notifications  regarding  the  processing  outcome  will  be  sent  via  Amazon  SNS.

Requirements:
● AWS  Account
● Amazon  S3  buckets:  doordash-landing-zn  and  doordash-target-zn
● AWS  Lambda
● Amazon  SNS
● AWS  IAM  (for  permissions)
● AWS  CodeBuild  (for  CI/CD)
● GitHub  (for  version  control)
● Python,  pandas  library
● Email  subscription  for  SNS  notifications

Steps:

Sample  JSON  File  for  Daily  Data:
○ A sample JSON file named 2024-03-09-raw_input.json with 10 delivery 
records, including different statuses like cancelled, delivered, and order 
placed.
{"id":  1,  "status":  "delivered",  "amount":  20.5,  "date":  "2024-03-09"}
{"id":  2,  "status":  "cancelled",  "amount":  15.0,  "date":  "2024-03-09"}
{"id":  3,  "status":  "order  placed",  "amount":  22.5,  "date":  "2024-03-09"}
{"id":  4,  "status":  "delivered",  "amount":  19.5,  "date":  "2024-03-09"}
{"id":  5,  "status":  "cancelled",  "amount":  18.0,  "date":  "2024-03-09"}
{"id":  6,  "status":  "delivered",  "amount":  23.5,  "date":  "2024-03-09"}
{"id":  7,  "status":  "order  placed",  "amount":  20.0,  "date":  "2024-03-09"}
{"id":  8,  "status":  "delivered",  "amount":  25.5,  "date":  "2024-03-09"}
{"id":  9,  "status":  "delivered",  "amount":  21.5,  "date":  "2024-03-09"}
{"id":  10,  "status":  "cancelled",  "amount":  17.5,  "date":  "2024-03-09"}


Daily  JSON  will  arrive  in  S3  bucket  doordash-landing-zn  with  format  like 
yyyy-mm-dd-raw_input.json
●        As  soon  as  file  lands  in  S3,  data  processing  should  start 
●        Set  Up  S3  Buckets:
○        Create  two  S3  buckets:  doordash-landing-zn  for  incoming  raw  files and  doordash-target-zn  for  processed  files.
●        Set  Up  Amazon  SNS  Topic:
○        Create  an  SNS  topic  for  sending  processing  notifications.
