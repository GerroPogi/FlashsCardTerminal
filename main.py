import json
import os
import time
import random
import keyboard
import datetime
import sys
import shutil
class Study:
    def __init__(self):
        basePath=os.path.join(os.path.dirname(__file__), "subjectsFlashCards")
        if not os.path.exists(basePath):
            os.mkdir(basePath)
        self.subjectFlashCards=os.path.join(os.path.dirname(os.path.abspath(__file__)),"subjectsFlashCards")
        self.subjectsFolder=[] #initializing the subject list without config.json
        for i in os.listdir(self.subjectFlashCards):
            if os.path.isdir(os.path.join(self.subjectFlashCards,i)) and not i=="finishedTests":
                self.subjectsFolder.append(i)
        subjects = ["math","ap","english","filipino","ict","mapeh","science","tle","others"]
        self.folderSubjects=os.listdir(self.subjectFlashCards)
        if not os.path.exists(os.path.join(basePath,"config.json")):
            name=input("Hi! You are new, what is your name?")
            grade=input("What is your grade?(Don't include section)")
            section=input("What is your section?")
            with open(os.path.join(os.path.dirname(__file__), "subjectsFlashCards","config.json"),"w") as f:
                json.dump({"name":name,"grade":grade,"section":section},f,indent=4)
        os.system("cls")
        for subject in subjects:
            path=os.path.join(basePath,subject)
            if not os.path.exists(path):
                os.mkdir(path)
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"subjectsFlashCards", "config.json"),"r") as f:
            self.user=json.load(f) #accessing the user's config to have a general score to grade them
        self.main()
    def main(self):
        os.system("cls")
        run=True
        #Start Program
        while run:
            print(f"Hello {self.user['name']} and welcome to 9-TAAL 2023-2024 Flash Cards Study Terminal \nCreated by Gerro Laurio Abarabar\nWhich would you like?\n1. Attempt Quiz\n2. Make Quiz\n3. Edit a quiz\n4. Find quiz\n5. Make a new Subject\n6. About")
            time.sleep(1)
            inp=keyboard.read_key()
            if inp.isdigit() and int(inp)>=1 and int(inp)<=6:
                run=False
            else:
                print("Fix the numbering/input")
                time.sleep(2)
            os.system("cls")
        #Directing the user to attempt and make
        if inp=="1":
            self.attempt()
            
        if inp=="2":
            self.make()
        if inp=="3":
            self.edit(None,None)
        if inp=="4":
            self.find()
        if inp=="5":
            
            self.makeSubject()
        if inp=="6":
            self.about()
    def pickFile(self,path):
        with open(path,"r") as f:
            a=json.load(f)
        return a
    def writeFile(self,path,value:dict):
        try:
            a=self.pickFile(path)
            for i in list(value.items()):
                a[i[0]]=i[1]
            with open(path,"w") as f:
                json.dump(a,f,indent=4)
        except:
            with open(path,"w") as f:
                json.dump(value,f,indent=4)
    def qna(self,test,subject):
        os.system('cls')
        score=0
        eval={}
        for i in range(1,len(test)+1):
            eval[i]={}
            question,cAnswer=random.choice(list(test.items()))
            test.pop(question)
            eval[i][question]=cAnswer
            answer=input(f"Question {i}: {question}\n Answer:")
            if answer.lower()==cAnswer.lower():
                eval[i]["answer"]=answer.capitalize()
                score+=1
            else:
                eval[i]["answer"]=answer.capitalize()
        resulti=[]
        os.system("cls")
        print("Quiz done!")
        time.sleep(1)
        os.system('cls')
        for i in eval:
            question = list(eval[i].keys())[0]
            your_answer = eval[i]["answer"]
            correct_answer = eval[i][question]
            result=f"In {i}.\nQuestion: {question}\nYour answer: {your_answer}\nCorrect Answer: {correct_answer}\n"
            resulti.append(result)
            self.typewrite(result,0.01)
        dateTime=datetime.datetime.now()
        with open("{}.txt".format(str(dateTime.strftime("%Y%m%d-%H%M%S"))),"w") as f:
            print(f"Subject: {subject}")
            for i in resulti: f.write(i)
            f.write(f"Score: {score}/{len(resulti)+1}")
        

        print(f"Score: {score}/{len(resulti)+1}\n{'You passed!' if score>=((len(resulti))*0.6)  else 'You Failed...'}")
        print("Your answers and score will be saved in: "+str(dateTime.strftime("%Y%m%d-%H%M%S"))+"\n")
        print("Press space to continue\nPress anything else to skip and leave.")
        time.sleep(1)
        keyboard.read_key()
        self.main()
    def edit(self,subject,quiz):
        if subject is None and quiz is None:
            run=True
            
            while run: #Asks for what subject
                for i in range(len(self.subjectsFolder)):
                    print(f"{i+1}. {self.subjectsFolder[i].upper()}")
                print("Which Subject?")
                time.sleep(1)
                self.subject=keyboard.read_key()
                if self.subject.isdigit():
                    for i in range(len(self.subjectsFolder)):
                        if int(self.subject)==i+1:
                            run=False
                            subject=self.subjectsFolder[i]
                else:
                    print("Fix numbering/input")
                    time.sleep(1)
                    
                os.system("cls")
            run=True
            os.system("cls")
            quizzes=os.listdir(os.path.join(self.subjectFlashCards,subject))
            
            while run:
                for i in range(len(quizzes)):
                    print(f"{i+1}. {quizzes[i].split('.')[0]}")
                print("Which quiz?")
                time.sleep(1)
                self.subject=keyboard.read_key()
                if self.subject.isdigit():
                    for j in range(len(quizzes)):
                        if int(self.subject)==j+1:
                            run=False
                            quiz=quizzes[i]
                            break
                else:
                    print("Fix numbering/input")
                    time.sleep(1)
                os.system("cls")
        a=self.pickFile(os.path.join(self.subjectFlashCards,subject,quiz))
        b=list(a.items())
        run=True
        while run:
            for i,(question, answer) in enumerate(b):
                print(f"{i+1}.\nQuestion: {question}\nAnswer: {answer}\n")
            print("Which of these are you editing?\nPress C to finish\n Press N to make a new question")
            time.sleep(1)
            inp=keyboard.read_key()
            if inp.isdigit():
                for i in range(len(b)):
                    if int(inp)==i+1:
                        run=False
                        question,answer=b[i]
                        self.editing(question,answer,subject,quiz,os.path.join(os.path.dirname(__file__),"subjectsFlashCards",subject,f"{quiz}"))
            elif inp=='c':
                self.main()
            elif inp=='n':
                self.addQuestion(subject,os.path.join(os.path.dirname(__file__),"subjectsFlashCards",subject,f"{quiz}"))
            else:
                print("Press the number of flie or\nPress C to finish\n Press N to make a new question")
            
    def editing(self,question,answer,subject,quiz,path):
        run=True
        while run:
            os.system("cls")
            print(f"Question: {question} \nAnswer: {answer}")
            print("Which are you editing?\n1. Question\n2. Answer\n3. Done\n4. Cancel")
            time.sleep(1)
            inp=keyboard.read_key()
            if inp.isdigit():
                inp=int(inp)
                if inp==1:
                    question=input(f"Question:{question}\nNew Question:")
                if inp==2:
                    answer=input(f"Answer: {question}\nNew Answer:")
                if inp==3:
                    run=False
                    self.writeFile(path,{question:answer})
                    self.edit(subject,quiz)
                if inp==4:
                    run=False
                    self.main()
            else:
                print("Choose an option...")
            os.system("cls")
    def makeSubject(self):
        print("Are you sure you want to create a new subject?\nPress Y or N to continue")
        time.sleep(1)
        yOrN=keyboard.read_key()
        os.system("cls")
        if yOrN=='y':
            subject=input("New Subject: ")
            subjectLocation=os.path.join(os.path.dirname(__file__),"subjectsFlashCards",subject)
            os.mkdir(subjectLocation)
            print(f"You can find your new subject in {subjectLocation}\nReturning home...")
            time.sleep(2)
            self.main()
        else:
            print("Ok.")
            time.sleep(1)
            self.main()
    def find(self):
        print("WARNING: This might get a little technical. If you wish to continue, make sure you know how to send a file location by either knowing it already or checking out the help menu.\nPress Y or N to continue...")
        time.sleep(1)
        yOrN=keyboard.read_key()
        if yOrN=="y":
            run=True
            while run:
                runx=True
                while runx:
                    os.system("cls")
                    print("Please type your file location of your test file, then Subject name. If it is in the same file location as this terminal then you can just paste the file's name.")
                    filePath=input("File: ")
                    if os.path.exists(os.path.join(os.path.dirname(__file__), filePath)):
                        inLocal=True
                        runx=False
                    elif os.path.exists(filePath):
                        inLocal=False
                        runx=False
                    else:
                        print("Fix file location")
                        time.sleep(1)
                os.system("cls")
                for i in range(len(self.subjectsFolder)):
                    print(f"{i+1}. {self.subjectsFolder[i].upper()}")
                print("Which subject?")
                time.sleep(1)
                inp=keyboard.read_key()
                if inp.isdigit() and (int(inp)>0 and int(inp)<=len(self.subjectsFolder)):
                    subject=self.subjectsFolder[int(inp)-1]
                    os.system("cls")
                    if inLocal:
                        added=self.add(os.path.join(os.path.dirname(__file__), filePath),subject)
                        if added:
                            print("File is now moved to: "+os.path.join(os.path.dirname(__file__), "subjectsFlashCards",subject,added))
                            run=False
                        elif added=="location":
                            print("Fix file location: "+filePath)
                        else:
                            print("Fix your quiz file. It should a .json file.")
                        run=False
                    elif not inLocal:
                        added=self.add(filePath)
                        if added:
                            print("File is now moved to: "+os.path.join(os.path.dirname(__file__), "subjectsFlashCards",subject,added))
                            run=False
                        elif added=="location":
                            print("Fix file location: "+filePath)
                        else:
                            print("Fix your quiz file. It should a .json file.")
                            
                    print("Returning home.")
                    time.sleep(2)
                    self.main()
                else:
                    print("Fix Subject Input")
        else:
            print("Ok")
            time.sleep(1)
            self.main()
    def add(self,path,subject):
        baseName=os.path.basename(path)
        splitBaseName=os.path.splitext(baseName)
        if splitBaseName[1]==".json":
            shutil.move(path,os.path.join(os.path.dirname(__file__),"subjectsFlashCards",subject,baseName))
            return baseName
    def typewrite(self,text,timeEachLetter):
        for i in str(text):
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(timeEachLetter)
    def about(self):
        self.typewrite("Welcome to the about section!\n\n Flash Card Terminal\nMade by Gerro Laurio Abarabar\nDate created: 9/2/2023\n\nThis terminal is for students to create their own customizable flash cards that have an easy learning curve and does most of the things for you.\nFunctions from main page:\n1. Attempt Quiz:\nIt will open a list of subjects and show you quizzes from that subject. You can also make your own subject so you can customize your other quizzes like your friend's or a class that is not known in highschool. In the beggining, there will be no quizzes but when you make more or get more from your friends, it will eventually be filled.\n2. Make Quiz:\nThis will make a quiz so that you can share it to your friends or make your own flash card so you can study on your own.\n3. Edit a quiz:\nThis will edit a quiz within the subjects. If you made a typo or an error, best to edit it and fix it. \n4. Find quiz:\n To find a quiz, you will send it data of file locations. Ex: C:/user/Jacob/Desktop/Jacob's files/quiz1.json. But if your quiz that your friend sent you is in the same file location as this program (Not the shortcut.) then it will work the same.\n5. Make new Subject\nIt is exactly what the title suggests. To make a new subject, you will input the name of the subject and make sure to correct any input errors. After that you're done.",0.01)
        print("\nPress Any key to go back to main page.")
        keyboard.read_key()
        self.main()
    def attempt(self):
        run=True
        tests=[]
        while run: #Asks for what subject
            for i in range(len(self.subjectsFolder)):
                print(f"{i+1}. {self.subjectsFolder[i].upper()}")
            print("What Subject?")
            time.sleep(1)
            subject=keyboard.read_key()
            for i in range(len(self.subjectsFolder)): #Checks if subject exists if not ex:(Output: a does not exist, please try again.)
                if subject==str(i-1):
                    run=False
                    break
            else:
                print("Fix numbering/input")
                time.sleep(1)
            os.system("cls")
        os.system("cls")
        for i in os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),"subjectsFlashCards",self.subjectsFolder[int(subject)-1])):
            tests.append(i.split(".")[0]) #makes a list of quizzes that have their file extension cut off
        run=True
        while run:
            os.system("cls")
            for i in range(len(tests)):
                print(f"{i+1}: {tests[i]}")# prints a list of files to pick to attemp the quiz
            print("Which one?")
            time.sleep(1)
            test=keyboard.read_key()
            if test.isdigit() and int(test)>=1 and int(test)-1<=len(tests):
                run=False
            else:
                print("Fix the numbering/input")
                time.sleep(1)
        testFile=self.pickFile(os.path.join(self.subjectFlashCards,self.subjectsFolder[int(subject)-1],f"{tests[int(test)-1]}.json"))
        self.qna(testFile,self.subjectsFolder[int(test)-1])
    def make(self):
        
        
        run=True
        while run:
            for i in range(len(self.subjectsFolder)):
                print(f"{i+1}. {self.subjectsFolder[i].upper()}")
            subject=input("For what subject?(Send number)\nTo create a new subject, you can type the name")
            if subject.isdigit() and (int(subject)<len(self.subjectsFolder) and int(subject)>0):
                for i in range(len(self.subjectsFolder)):
                    if i+1==int(subject):
                        self.questions=self.makewSubject(self.subjectsFolder[i])
                        break
                run=False
            elif not subject.isdigit():
                self.questions=self.makeNewSubject(subject)
                run=False
                
                
            else:
                print("Fix numbering/input")
                time.sleep(2)
                os.system("cls")
    def makewSubject(self,subject,mode=None):
        os.system("cls")
        questions={}
        cancel=True
        run=True
        print("You have chosen: "+subject)
        while run:
            question=input("What is your question?\nType Done if done, Cancel to cancel\n")
            if len(question)==0:
                print("You picked nothing, try again.")
                time.sleep(1)
                cancel=True
            
            elif question.lower().strip() == "done":
                if not questions:
                    print("You didn't get any questions.\nTry again?\nPress Y or N to continue\n")
                    time.sleep(1)
                    yOrN=keyboard.read_key()
                    if yOrN=="y":
                        print("Ok.")
                        time.sleep(1)
                    else:
                        print("Canceling...")
                        self.main()
                        time.sleep(1)
                else:
                    cancel=True
                    run=False
                time.sleep(1)
            elif question.lower()=="cancel":
                print("Are you sure you want to cancel?\nPress Y or N to continue\n")
                time.sleep(1)
                yOrN=keyboard.read_key()
                if yOrN=="y":
                    print("Ok.")
                    run=False
                    time.sleep(1)
                cancel=True
            elif question.isdigit():
                print("The question is just digits.\nAre you sure?\nPress Y or N to continue\n")
                time.sleep(1)
                yOrN=keyboard.read_key()
                if yOrN=="y":
                    print("Ok.")
                    time.sleep(1)
                    cancel=False
                else:
                    print("Canceling...")
                    cancel=True
                    time.sleep(1)
            elif not "?" in question:
                print("You didn't have a question mark in that question.\nAre you sure?\nPress Y or N to continue\n")
                time.sleep(1)
                yOrN=keyboard.read_key()
                if yOrN=="y":
                    print("Ok.")
                    cancel=False
                    time.sleep(1)
                else:
                    print("Canceling...")
                    cancel=True
                    time.sleep(1)
            time.sleep(2)
            
            os.system("cls")
            if not cancel:
                runx=True
                while runx:
                    print("Your question is: " + question)
                    answer=input("What is your answer?\n")
                    time.sleep(1)
                    if len(question) == 0:
                        print("You picked nothing, try again.")
                    else:
                        runx=False
                    os.system("cls")
                print("Question: " + question+"\nAnswer: " + answer+"\nAre you sure?\nPress Y or N to continue")
                time.sleep(1)
                yOrN=keyboard.read_key()
                if yOrN=="y":
                    print("Ok.")
                    questions[question]=answer
                    time.sleep(1)
                else:
                    cancel=False
                os.system("cls")
            cancel=False
        if not mode==None:
            return (question, answer)
        print("Congrats on completing your quiz!\nHere is what you've input:")
        for i in range(questions):
            print(f"{i+1}. Question: {questions[i]}\nAnswer: {questions[questions[i]]}\n\n")
        print("Are you sure you want to save?\nPress Y or N to continue\n")
        time.sleep(1)
        yOrN=keyboard.read_key()
        if yOrN=="y":
            os.system("cls")
            print("Great!\n All you need to do now is to name this quiz.")
            name=input("")
            self.writeFile(os.path.join(self.subjectFlashCards,subject,f"{name}.json"),questions)
            print(f"It is now saved in: {os.path.join(self.subjectFlashCards,subject,f'{name}.json')} Send it to others to share your questions.")
            time.sleep(1)
            print("Returning Home")
            time.sleep(1)
            os.system("cls")
        else:
            os.system("cls")
            print("Ok. Returning home.")
            time.sleep(1)
        self.main()
    def makeNewSubject(self):
        os.system("cls")
        run=True
        while run:
            os.system("cls")
            subjectName=input("What is the name of your subject?\nSubject name:")
            if subjectName.isdigit():
                print(f'Are you sure you want "{subjectName}" to be the name of your subject?\n Press Y or N to continue.')
                yOrN=keyboard.read_key()
                if yOrN=="y":
                    run=False
            elif len(subjectName)==0:
                print("You didn't put anything. Try again")
                time.sleep(2)
                
        print(f"Are you sure you want to create {subjectName} as a new subject?\nPress Y or N to continue\n")
        time.sleep(1)
        yOrN=keyboard.read_key()
        if yOrN=='y':
            self.makewSubject(subjectName)
        else:
            print("Ok, returning home...")
            time.sleep(1)
            self.main()
    def addQuestion(self, subject,path):
        
        
        os.system("cls")
        question= self.makewSubject(subject,mode="Get Data")
        print(question,)
        qna={question[0]:question[1]}
        self.writeFile(path,qna)
        print("Wrote to: ",path)
        
            
if __name__ == "__main__":
    m=Study()
