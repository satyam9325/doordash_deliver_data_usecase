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