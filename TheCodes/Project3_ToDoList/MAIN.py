#Creates a list. 
tasks=[]
while True:
  #Add a task.

  def add_task():
    global tasks
    task=input("Enter your task:")
    tasks.append(task)
    print("Added")
    
  #Show all tasks
  def show():
    if tasks:
      for i, task in enumerate(tasks): # Enumerate returns two values.
        print(f"{i+1} {task}")
    else:
      print("The list is empty.")

  #Drop a task.
  def delete_task():
    global tasks
    show()
    if not tasks:
      print("Cannot delete from an empty list.")
    else:
      task_number=input("Enter the task number you want to delete")
      try:
        task_remove=int(task_number)
      except ValueError:
        print("Please enter correct value.")
      tasks.pop(task_remove-1)
      print("Task removed.")
      print("The new list after removal.")
      show()

  #Update an existing task.
  def update_task():
    global tasks
    show()
    task_to_be_updated=input("Enter the number of task to be updated:")
    try:
      task_to_be_updated=int(task_to_be_updated)
    except ValueError:
      print("Please enter correct value.")
    updated_task=input("Enter the updated task:")
    try:
      updated_task=int(updated_task)
    except ValueError:
      print("Please enter correct value.")
    tasks[task_to_be_updated-1]=updated_task
    print("Updated")

  # Ask user to enter their option
  print("MAIN MENU\n1. Show all tasks.\n 2. Add a task.\n 3. Remove a task \n 4. Update an existing task.")
  option=input("What do you want to do?")

  try:
    num=int(option)
  except ValueError:
    print("Please enter correct value.")

  if num==1:
    show()
    continue
  elif num==2:
    add_task()
    continue
  elif num==3:
    delete_task()
    continue
  elif num==4:
    update_task()
    continue
