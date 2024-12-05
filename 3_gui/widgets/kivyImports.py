import os
from kivy.factory import Factory
from kivy.properties import ListProperty, ObjectProperty, StringProperty, NumericProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.core.text import LabelBase
from kivy.uix.popup import Popup
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window

from plyer import filechooser

from glob import glob
import datetime as dt
import json
import sys
import re