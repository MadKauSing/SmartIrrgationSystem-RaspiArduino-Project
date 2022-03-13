import RPi.GPIO as gp
gp.setmode(gp.BOARD)
gp.setup(8,gp.IN)
gp.setup(36,gp.OUT,initial=gp.LOW)
gp.setup(32,gp.OUT,initial=gp.LOW)
while True:
    try:
        print(not gp.input(8))  
        gp.output(36,gp.input(8))  
        gp.output(32,not gp.input(8))   
    except:
        gp.cleanup()
