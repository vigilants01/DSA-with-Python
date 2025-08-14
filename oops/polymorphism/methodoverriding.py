class parent:
    def speak(self):
        return "father speaks"
class child(parent):
    def speak(self):
        return "child speak"
    
c=child()
print(c.speak())