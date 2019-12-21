class car():
    def __init__(self,model,color,name,miles,speed):
        self.model=model
        self.color=color
        self.name=name
        self.miles=miles
        self.speed=speed
    def c_name(self):
        print("name= "+self.name)
    
    def c_color(self):
        print("color= "+self.color)
        
    def c_model(self):
       print("model= "+str(self.model))
    
    def c_miles(self):
       print("miles travelled= "+str(self.miles))
       
    def c_speed(self):
       print("miles travelled= "+str(self.speed))
        
c=car(2016,"black","G WAGON", 0,250)  
c.c_name()
c.c_color()
c.c_model()
c.c_miles()
c.c_speed()


