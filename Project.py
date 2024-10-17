#Available Tasks 
tasks = [{"task":"Quran", "completed":True},
         {"task":"Salah", "completed":True}, 
         {"task":"Study", "completed":True}, 
         {"task":"Sleep", "completed":False},
         {"task":"Visit Hamada", "completed":True}]

# main message 
message_1 = """1. Add New Task
2. View My Tasks
3. Quit """

# Message For control On Tasks 
message_2 = """1. Mark Task as Completed
2. Delete Task
3. Return To Main Menu
"""

# Add Function 
def add_task():
  user_task = input("Enter Your Task : ")
  tasks.append({"task":user_task, "completed":False})
  print("Task Added Successfully")
  print("-"*30)

# View Function
def view_task ():
  for index,task in enumerate(tasks,1):
    if len(task) == 0 :
      pass
    else :  
      if task["completed"] :
        print(f'{index}. {task["task"]} ✅')
      else:  
        print(f'{index}. {task["task"]} ❌')
  print("-"*30)        

# Delete Function
def delete_task (user_input):
  for index,task in enumerate(tasks) :
   if user_input > len(tasks):
     print("Invalid Input")
     print("-"*30)
     return
   else:   
     if user_input-1 == index :
       del tasks[index]
       print("Task Deleted Successfully")
       print("-"*30)
       return

# Mark Function
def mark_task_complete (user_input):
  for index,task in enumerate(tasks,1):
   if user_input > len(tasks):
     print("Invalid Input")
     print("-"*30)
     return
   else :  
     if user_input == index :
      if task["completed"]:
         print("Task Already Completed")
         print("-"*30)
         return
      else :   
         task["completed"] = True
         print("Task Completed Successfully")
         print("-"*30)


while True :
  print(message_1)
  choice_1 = input("Enter your choice: ")

  match(choice_1):
  
    case "1":
      print("-"*30)
      add_task()

    case "2":
      print("-"*30)
      view_task()
      choice_2 = int(input(f"What Do You Want :\n{message_2}\n----> "))
      if choice_2 == 1 :
        choice_3 = int(input("Enter Task Number To Mark It Complete : "))
        mark_task_complete(choice_3)
      elif choice_2 == 2 :
        choice_3 = int(input("Enter Task Number To Delete It : "))
        delete_task(choice_3)
      elif choice_2 == 3 :
        print("-"*30)
        continue  
      else:
        print("Invalid choice")
        print("-"*30)
      continue  

    case "3":
      break

    case _: 
      print("Invalid Choice, Please Enter A Number Between 1 And 3")
      print("-"*30)
      continue
