file_path = "C:\\Users\\Nicholas Armstrong\\Development\\POC_Sem2_Assignments\\10_Functional Programming\\03_File_Handling_2\\newfile.txt"

stream = open(file_path)
stream.write("This is the first message!\n")
stream.write('This is my second message!')
stream.write("This is my second message!")
stream.close