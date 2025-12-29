import os
def shutdown_pc():
    os.system("shutdown /s /t 1")

i=input("Do you want to shutdown your pc? (yes/no): ")
if i.lower()=="yes":  
    input("Press Enter to confirm shutdown...Save your files before proceeding.")  
    shutdown_pc()
else:
    print("Shutdown cancelled.")