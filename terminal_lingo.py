def terminal_command():
     command = input("Type a command for a defition: ")
     if (command == "touch" ):
       	 print("\n")
       	 print("this command is used to create files")
 
     if (command == "cd" ):
         print("\n")
         print("this command will change the directory")
 
     if (command == "cat" ):
         print("\n")
         print("cat command allows us to create single or multiple files")
 
     if (command == "ls" ):
         print("\n")
         print("Use this command after navigating into a directory using the cd command to view the contents")
 
     if (command == "mkdir" ):
         print("\n")
         print("This command will allow you to create a directory folder right from the CLI")
terminal_command()
