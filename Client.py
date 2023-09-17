from ClientModel import ClientModel
from ClientController import ClientController

import sys
import common
from omniORB.ami import CORBA
from tkinter import messagebox
import subprocess

# create ORB object and connect to server
orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
obj = orb.string_to_object("corbaname::localhost:9999#Conn")
GameFunctions = obj._narrow(common.GameFunctions)

# check if connection was successful and open login window
if GameFunctions:
    print("Connection to server established successfully")
    # subprocess.call(['python', 'C:/Users/user/PycharmProjects/2022-2_9328-fingrp1_other/gui/LoginView.py'])
else:
    messagebox.showerror("Connection error", "Failed to connect to server")

# Create instances of the model and controller
model = ClientModel()
controller = ClientController(model)

# Run the application
controller.run()