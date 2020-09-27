import mysql.connector

mydb = mysql.connector.connect(
  host="adhyapak.cmh6pvva4wrd.ap-south-1.rds.amazonaws.com",
  user="admin",
  password="adhyapak1",
  database="adhyapak"
)

mycursor = mydb.cursor()

def Add_Que(sub,clas,chapter,que_type,comp,marks,questions):
    for obj in questions:
        sql = """insert into Question_Bank(SUB,CLASS,CHAPTER,QUE_TYPE,COMP,MARKS,QUE_DESC,CUST_ID)
               values(%s,%s,%s,%s,%s,%s,%s,%s)"""
        values = (sub,clas,chapter,que_type,comp,marks,obj.text,'system')
        mycursor.execute(sql,values)
        mydb.commit()
        que_id = mycursor.lastrowid
        options = obj.options
        if que_type == 'MCQ':
            for i in range(len(options)):
                sql = """insert into Test_Option (QUE_ID,OPT) values(%s,%s)"""
                values = (que_id,options[i])
                mycursor.execute(sql,values)
                mydb.commit()
                if( i== obj.answer):
                    ans_id = mycursor.lastrowid
                    sql = """UPDATE Question_Bank SET ANS_ID = %s WHERE QUE_ID = %s"""
                    values = (ans_id,que_id)
                    mycursor.execute(sql,values)
                    mydb.commit()
        elif que_type == 'FIB':
            sql = """insert into Test_Option (QUE_ID,OPT) values(%s,%s)"""
            values = (que_id,obj.answer)
            mycursor.execute(sql,values)
            mydb.commit()
            ans_id = mycursor.lastrowid
            sql = """UPDATE Question_Bank SET ANS_ID = %s WHERE QUE_ID = %s"""
            values = (ans_id,que_id)
            mycursor.execute(sql,values)
            mydb.commit()