import pickle
import time
import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import pyttsx3
import cv2

speak = pyttsx3.init()

def submit():
   def set_data():
       rollno = int(input('Enter roll number: '))
       name = input('Enter name: ')
       english = int(input('Enter Marks in English: '))
       maths = int(input('Enter Marks in Maths: '))
       physics = int(input('Enter Marks in Physics: '))
       chemistry = int(input('Enter Marks in Chemistry: '))
       cs = int(input('Enter Marks in CS: '))
       print()

       # create a dictionary
       student = {}
       student['rollno'] = rollno
       student['name'] = name
       student['english'] = english
       student['maths'] = maths
       student['physics'] = physics
       student['chemistry'] = chemistry
       student['cs'] = cs
       return student

   def display_data(student):
       print('\nSTUDENT DETAILS..')
       print('Roll Number:', student['rollno'])
       print('Name:', student['name'])
       print('English:', student['english'])
       print('Maths:', student['maths'])
       print('Physics:', student['physics'])
       print('Chemistry:', student['chemistry'])
       print('CS:', student['cs'])

   def display_data_tabular(student):
       print(student['rollno'], student['name'], student['english'],
             student['maths'], student['physics'], student['chemistry'],
             student['cs'], sep='\t')

   def class_result():
       # open file in binary mode for reading
       try:
           infile = open('student.dat', 'rb')
       except FileNotFoundError:
           print('No record found..')
           print('Go to admin menu to create record')
           return

       print('\nRollno', ' Name', '\tEnglish', 'Maths', 'Physics', 'Chemistry', 'CS')
       # read to the end of file.
       while True:
           try:
               # reading the oject from file
               student = pickle.load(infile)

               # display the record
               display_data_tabular(student)
           except EOFError:
               break

       # close the file
       infile.close()

   def write_record():
       # open file in binary mode for writing.
       outfile = open('student.dat', 'ab')

       while (True):
           # serialize the record and writing to file
           pickle.dump(set_data(), outfile)
           ans = input('Want to enter more record (y/n)?: ')
           if ans in 'nN':
               break

       # close the file
       outfile.close()

   def read_records():
       # open file in binary mode for reading
       try:
           infile = open('student.dat', 'rb')
       except FileNotFoundError:
           print('No record found..')
           return

       # read to the end of file.
       while True:
           try:
               # reading the oject from file
               student = pickle.load(infile)

               # display the record
               display_data(student)
           except EOFError:
               break

       # close the file
       infile.close()

   def search_record():
       # open file in binary mode for reading
       try:
           infile = open('student.dat', 'rb')
       except FileNotFoundError:
           print('No record..')
           return

       found = False
       rollno = int(input('Enter the rollno you want to search: '))
       # read to the end of file.
       while True:
           try:
               # reading the oject from file
               student = pickle.load(infile)
               if student['rollno'] == rollno:
                   # display the record
                   display_data(student)
                   found = True
                   break
           except EOFError:
               break
       if found is False:
           print('Record not found!!')

       # close the file
       infile.close()

   def delete_record():
       print('\nDELETE RECORD')

       try:
           infile = open('student.dat', 'rb')
       except FileNotFoundError:
           print('No record found to delete..')
           return

       outfile = open("temp.dat", "wb")
       found = False

       rollno = int(input('Enter roll number: '))
       while True:
           try:
               # reading the oject from file
               student = pickle.load(infile)

               # display record if found and set flag
               if student['rollno'] == rollno:
                   display_data(student)
                   found = True
                   break
               else:
                   pickle.dump(student, outfile)
           except EOFError:
               break

       if found is False:
           print('Record not Found')
           print()
       else:
           print("record found and deleted")
       infile.close()
       outfile.close()
       os.remove("student.dat")
       os.rename("temp.dat", "student.dat")

   def modify_record():
       print('\nMODIFY RECORD')
       try:
           infile = open('student.dat', 'rb')
       except FileNotFoundError:
           print('No record found to modify..')
           return

       found = False
       outfile = open("temp.dat", "wb")
       rollno = int(input('Enter roll number: '))
       while True:
           try:
               # reading the oject from file
               student = pickle.load(infile)

               # display record if found and set flag
               if student['rollno'] == rollno:

                   print('Name:', student['name'])
                   ans = input('Want to edit(y/n)? ')
                   if ans in 'yY':
                       student['name'] = input("Enter the name ")

                   print('English marks:', student['english'])
                   ans = input('Want to edit(y/n)? ')
                   if ans in 'yY':
                       student['english'] = int(input("Enter new marks: "))

                   print('Maths marks:', student['maths'])
                   ans = input('Want to edit(y/n)? ')
                   if ans in 'yY':
                       student['maths'] = int(input("Enter new marks: "))

                   print('Physics marks:', student['physics'])
                   ans = input('Want to edit(y/n)? ')
                   if ans in 'yY':
                       student['physics'] = int(input("Enter new marks: "))

                   print('Chemistry marks:', student['chemistry'])
                   ans = input('Want to edit(y/n)? ')
                   if ans in 'yY':
                       student['chemistry'] = int(input("Enter new marks: "))

                   print('CS marks:', student['cs'])
                   ans = input('Want to edit(y/n)? ')
                   if ans in 'yY':
                       student['cs'] = int(input("Enter new marks: "))

                   pickle.dump(student, outfile)
                   found = True
                   break
               else:
                   pickle.dump(student, outfile)
           except EOFError:
               break
       if found is False:
           print('Record not Found')
       else:
           print('Record updated')
           display_data(student)

       infile.close()
       outfile.close()
       os.remove("student.dat")
       os.rename("temp.dat", "student.dat")

   def intro():
       print("=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x")
       print("        STUDENT")
       print("      REPORT CARD")
       print("        PROJECT")
       print("  MADE BY : Vishwajith Lal, Rizwan and Olin ")
       print("  SCHOOL : GEMS MILLENNIUM SCHOOL SHARJAH")
       print("=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x==x=x")
       print()
       time.sleep(1)

   def main_menu():
       print("Hii",uname.get(),"!!!  choose your option from below: ")
       print("Welcome to Skillcept Portal !!")
       speak.say("Welcome !!")
       speak.say(uname.get())
       speak.say("Welcome to Skillcept Portal !!")
       speak.say("Choose one of the four options from below ")
       speak.runAndWait()
       print()
       print("MAIN MENU")
       print("1. REPORT MENU")
       print("2. ADMIN MENU")
       print("3. SCAN QR-CODE ")
       print("4. EXIT")



   def report_menu():
       print("REPORT MENU")
       print("1. CLASS RESULT")
       print("2. STUDENT REPORT CARD")
       print("3. BACK TO MAIN MENU")
       print("4. SCAN QR-CODE ")
       speak.say("REPORT MENU")
       speak.say("Choose one of the four options from below ")
       speak.runAndWait()

   def admin_menu():
       print("ADMIN MENU")
       print("1. CREATE STUDENT RECORD")
       print("2. DISPLAY ALL STUDENTS RECORDS")
       print("3. SEARCH STUDENT RECORD ")
       print("4. MODIFY STUDENT RECORD ")
       print("5. DELETE STUDENT RECORD ")
       print("6. BACK TO MAIN MENU")
       speak.say("ADMIN MENU")
       speak.say("Choose one of the six options from below ")
       speak.runAndWait()

   def main():
       intro()
       while (True):
           main_menu()
           choice = input('Enter choice(1-4): ')
           print()

           if choice == '1':
               report_menu()
               rchoice = input('Enter choice(1-4): ')
               if rchoice == '1':
                   class_result()
               elif rchoice == '2':
                   search_record()
               elif rchoice == '3':
                   pass
               else:
                   print('Invalid input !!!')
               print()

           elif choice == '2':
               admin_menu()
               echoice = input('Enter choice(1-6): ')
               if echoice == '1':
                   write_record()
               elif echoice == '2':
                   read_records()
               elif echoice == '3':
                   search_record()
               elif echoice == '4':
                   modify_record()
               elif echoice == '5':
                   delete_record()
               elif echoice == '6':
                   pass
               else:
                   print('Invalid input !!!')
               print()
           elif choice == '3':
               cap = cv2.VideoCapture(0)
               detector = cv2.QRCodeDetector()
               while True:
                   _, img = cap.read()
                   data, one, _ = detector.detectAndDecode(img)
                   if data:
                       a = data
                       break
                   cv2.imshow(" QRCodeScanner app", img)
                   if cv2.waitKey(1) == ord("q"):
                       break
               print(" Details of the students: ",a)

               cv2.destroyAllWindows()
               break


           elif choice == '4':
               print("Thank you for visiting Skillcept Portal ")
               print("Have a good day!!! ")
               speak.say("Thank you for visiting Skillcept Portal ")
               speak.say("Have a good day ")
               speak.runAndWait()

               break
           else:
               print('Invalid input!!!')
               print()

   main()

#--------------------------------------------------------------------------------------------------
root = tk.Tk()
root.title("STP-Skillcept Portal")
root.geometry('500x300')
Label(root, text=" Welcome to Skillcept Portal !! " , font=("Courier 15 bold")).place(x=40, y=8)
Label(root, text="Username").place(x=40,y=60)
Label(root, text="Password").place(x=40,y=100)
submit = Button(root, text="Submit", font=("Courier 15 bold"), command=submit)
submit.place(x=40, y=160)
uname = Entry(root, width=30)
uname.place(x=120, y=55)
upass = Entry(root, width=30, show='*')
upass.place(x=120, y=95)
Label(text="SKILLCEPT PORTAL.CO",font=("Courier 15 bold")).place(x=16,y=260)
Label(text="===============================================",font=("Courier 15 bold")).place(x=0.1,y=30)
Label(text="___________________________________",font=("Courier 15 bold")).place(x=0.1,y=231)


#------------------------------------
frame = Frame(root, width=2, height=2)
frame.pack()
frame.place(anchor='center', relx=0.77, rely=0.7)
image=Image.open('/Users/Rizwan/OneDrive/Desktop/SkillCept.jpg')
# Resize the image in the given (width, height)
img=image.resize((200, 150))
# Convert the image in TkImage
my_img=ImageTk.PhotoImage(img)
label = Label(frame, image = my_img)
label.pack()
#---------------------------------
root.mainloop()
