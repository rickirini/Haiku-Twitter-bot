# tweeku.py
"""This module runs the Controller class from the controller module
with the Model and View classes as arguments"""
from controller import Controller
from model import Model
from view import GUIView

Controller(Model(), GUIView()).run()
