class Robot:
    name="robo"
    def __init__(self,purpose,abilities):
        self.purpose=purpose
        self.abilities=abilities

robo_obj=Robot("learning",["answering to your questions","explaining concepts you don't understand","help you solve your homework step-by-step"])

print("My name is",robo_obj.name)
print("My purpose is",robo_obj.purpose)
print("My abilities are",robo_obj.abilities)