from add_que import Add_Que

class combine:  
    def __init__(self, que_text, option,answer):  
        self.text = que_text  
        self.options = option 
        self.answer = answer
        
file1 = open("out_text.txt","r")
arr = file1.readlines()
que_text = ''
option = []
que_count = 0
questions = []
for line in arr:
    line = line.rstrip("\n")
    words = line.split(' ')
    text = line.replace(words[0]+' ','')  
    if words[0] == 'Subject:':
        Subject = text
    elif words[0] == 'Class:':
        Class = text
    elif words[0] == 'Chapter:':
        Chapter = text
    elif words[0] == 'Type:':
        Type = text
    elif words[0] == 'Subject:':
        subject = text
    elif words[0] == 'Complexity:':
        Comp = text
    elif words[0] == 'Marks:':
        Marks = text
    elif words[0] == 'Q:)':
        if(que_count == 0):
            que_text = text+' '
        else:
            if Type == 'MCQ':
                if answer == '' or int(answer) > len(option)-1:
                    raise Exception("Invalid answer for the Question, check this que -> " + que_text)
                if len(option)<2:
                    raise Exception("MCQ Type question should have atleast 2 Options, check this que -> " + que_text)
            elif(Type == 'FIB'):
                if answer == '':
                    raise Exception("Invalid answer for the Question, check this que -> " + que_text)
            questions.append(combine(que_text,option,answer))
            option = []
            que_text = text+' '
        que_count += 1
    elif ':' not in words[0]:
        que_text += line
    elif words[0] == 'a:)':
        option.append(text)
    elif words[0] == 'b:)':
        if Type != 'MCQ':
            raise Exception("Not MCQ type question should have only one option, check this que -> " + que_text)
        option.append(text)
    elif words[0] == 'c:)':
        if Type != 'MCQ':
            raise Exception("Not MCQ type question should have only one option, check this que -> " + que_text)
        option.append(text)
    elif words[0] == 'd:)':
        if Type != 'MCQ':
            raise Exception("Not MCQ type question should have only one option, check this que -> " + que_text)
        option.append(text)
    elif words[0] == 'answer:':
        if Type == 'MCQ':
            answer = int(text)
        else:
            answer = text
if Type == 'MCQ':
    if answer == '' or int(answer) > len(option)-1:
        raise Exception("Invalid answer for the Question, check this que -> " + que_text)
    if len(option)<2:
        raise Exception("MCQ Type question should have atleast 2 Options, check this que -> " + que_text)
elif(Type == 'FIB'):
    if answer == '':
        raise Exception("Invalid answer for the Question, check this que -> " + que_text)
questions.append(combine(que_text,option,answer))

Add_Que(Subject,Class,Chapter,Type,Comp,Marks,questions)