file_path = "C:\\Users\\Nicholas Armstrong\\Development\\POC_Sem2_Assignments\\10_Functional Programming\\03_File Handling\myFile.txt"

try:
    stream= open("file_patch")
    print(stream.read())
     stream.close()
except Exception as e:
    print("an error occured", e)
