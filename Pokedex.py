import os
from os import listdir
from pathlib import Path
from re import I
from turtle import width
import pandas as pd
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.properties import ObjectProperty, StringProperty
from kivy.lang import Builder
from kivy.core.window import Window
import csv

with open('PokedexInfo.txt', newline='') as cvsfile:
    spamwriter = csv.reader(cvsfile, delimiter= ',', quotechar='|')

# This makes the window be the correct size for the raspberry pi.
Window.size = (790, 450)

# Information:
# Every id/program created in Kivy is to start with a capital letter.
# Every def/program created in python is to have no capital letters.
# The screens are to share the same color, but have different colors for the different screens.
# Thing that are commented out are things I think I might need in the future. They will either be reimplimented, or they will be deleted next patch
# the version number is updated upon something I believe to be a huge milestone: These are
# v0.1: This was the creation of the pokedex app
# v0.2: This was when I got it running on the Raspberry pi.
# v0.3: This was when I got images working in the pokedex screen, along with making the screen nicer to look at for the raspberry pi's smaller screen


Builder.load_string("""

<ScreenOne>:
    # This is the main screen
    FloatLayout:
        Label:
            text: 'Pokedex app v0.3' 
            background_color: 1, 0, 0, 0
            pos_hint: {"x":0, "y":0.7}
            size_hint: 1, 0.3
        Button:
            text: "Go to Pokedex"
            background_color: 1, 0, 0, 1
            pos_hint: {"x": 0, "y": 0.3}
            size_hint: 0.5, 0.3
            on_press: 
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'screen_two'
        Button:
            text: "Go to Region Maps (not worked on at all)"
            background_color: 1, 0, 1, 1
            pos_hint: {"x": 0.5, "y": 0.3}
            size_hint: 0.5, 0.3
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'screen_three'
        Button:
            text: "Go to Move Screen (not worked on at all)"
            background_color: 0, 1, 0, 1
            pos_hint: {"x": 0, "y": 0}
            size_hint: 0.5, 0.3
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'screen_four'
        Button:
            text: "Go to Catch Tracker (slightly worked on)"
            background_color: 0, 1, 1, 1
            pos_hint: {"x": 0.5, "y": 0}
            size_hint: 0.5, 0.3
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'screen_five'



<ScreenTwo>:
    FloatLayout:
    # This is the pokedex screen
# This button takes you back to the main screen
        Button:
            text: "Go back"
            pos_hint: {"x":0, "y":0}
            size_hint: 0.2, 0.2
            background_color: 1, 0, 0
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.transition.durarion = 1
                root.manager.current = 'screen_one'

# Top Lavel is some information about the pokemon, Middle three are to put down the types, abilites, and gender ratio in an easy to read way, and the bottom label is dex entries      
        Label:
            id: Pokemon_Name
            text: "Pokemon Name"
            pos_hint: {"x":0, "y":0.6}
            size_hint: 1, 0.4
            text_size: self.size
            valign: 'top'
            halign: 'center'
                    
        Label: 
            id: Pokemon_Type
            text: "Pokemon Type"
            pos_hint: {"x":0.2, "y":0.6}
            size_hint: 0.1, 0.3
            text_size: self.size
            valign: 'top'
            halign: 'center'

        Label: 
            id: Pokemon_Abilities
            text: "Pokemon Abilities"
            pos_hint: {"x":0.3, "y":0.6}
            size_hint: 0.2, 0.3
            text_size: self.size
            valign: 'top'
            halign: 'center'

        Label: 
            id: Pokemon_Gender
            text: "Pokemon Gender"
            pos_hint: {"x":0.5, "y":0.6}
            size_hint: 0.2, 0.3
            text_size: self.size
            valign: 'top'
            halign: 'center'                    

        Label:
            id: Pokemon_Stats
            text: "Pokemon Stats"
            pos_hint: {"x":0.5,"y":0.5}
            size_hint: 0.5, 0.5
            text_size: self.size
            valign: 'top'
            halign: 'center'
                                       
        Label:
            id: Dex_Entry
            text: "Pokemon Dex Entry"
            pos_hint: {"x": 0.2, "y":0}
            size_hint: 0.8, 0.6
            text_size: self.size
            valign: 'top'
            halign: 'center'

# The pokemon sprite
        Image:
            id: Normal
            source: 
            pos_hint: {"x": 0, "y": 0.8}
            size_hint: 0.2, 0.2
        Image:
            id: Shiny
            source: 
            pos_hint: {"x": 0, "y": 0.6}
            size_hint: 0.2, 0.2

# These Buttons are to change the pokemon you are viewing
        Button:
            text: "+1"
            pos_hint: {"x": 0, "y":0.2}
            size_hint: 0.1, 0.1
            background_color: 1, 0, 0
            on_press:
                app.Pokedex_Input_Buttons(1)
                app.Change_Text()

        Button:
            text: "-1"
            pos_hint: {"x": 0.1, "y":0.2}
            size_hint: 0.1, 0.1 
            background_color: 1, 0, 0
            on_press:
                app.Pokedex_Input_Buttons(-1)  
                app.Change_Text()   
        Button:
            text: "+10"
            pos_hint: {"x": 0, "y":0.3}
            size_hint: 0.1, 0.1
            background_color: 1, 0, 0
            on_press:
                app.Pokedex_Input_Buttons(10)
                app.Change_Text()
        Button:
            text: "-10"
            pos_hint: {"x": 0.1, "y":0.3}
            size_hint: 0.1, 0.1
            background_color: 1, 0, 0
            on_press:
                app.Pokedex_Input_Buttons(-10)
                app.Change_Text()
        Button:
            text: "+100"
            pos_hint: {"x": 0, "y":0.4}
            size_hint: 0.1, 0.1
            background_color: 1, 0, 0
            on_press:
                app.Pokedex_Input_Buttons(100)
                app.Change_Text()
        Button:
            text: "-100" 
            pos_hint: {"x": 0.1, "y":0.4}
            size_hint: 0.1, 0.1
            background_color: 1, 0, 0
            on_press:
                app.Pokedex_Input_Buttons(-100) 
                app.Change_Text()             

# These buttons are to change what gen the dex entry is from 
        Button: 
            text: "Inc"
            pos_hint: {"x": 0, "y": 0.5}
            size_hint: 0.1, 0.1
            background_color: 1, 0, 0
            on_press:
                app.Region_Increase()
        Button: 
            text: "Dec"
            pos_hint: {"x": 0.1, "y": 0.5}
            size_hint: 0.1, 0.1
            background_color: 1, 0, 0
            on_press:
                app.Region_Decrease()


<ScreenThree>:
    BoxLayout:
        Button:
            text: "Go back (Screen Three)"
            background_color: 1, 0, 1, 1
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.transition.durarion = 1
                root.manager.current = 'screen_one'  

<ScreenFour>
    BoxLayout:
        Button:
            text: "Go back (Screen Four)"
            background_color: 0, 1, 0, 1
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.transition.durarion = 1
                root.manager.current = 'screen_one'  
<ScreenFive>
    FloatLayout:
        Button:
            text: "Go back"
            background_color: 0, 1, 1, 1
            pos_hint: {"x": 0, "y": 0}
            size_hint: 0.2, 0.2
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.transition.durarion = 1
                root.manager.current = 'screen_one' 
    
# the pokemon input
        Label:
            id: Pokemon_Catch   
            text: "Pokemon"
            pos_hint: {"x": 0.2, "y": 0.8}
            size_hint: 0.8, 0.2
            valign: 'top'
            halign: 'center'
                     
# These Buttons are to change the pokemon you are viewing
        Button:
            text: "+1"
            pos_hint: {"x": 0, "y":0.2}
            size_hint: 0.1, 0.1
            background_color: 0, 1, 1, 1
            on_press:
                app.Pokedex_Input_Buttons(1)


        Button:
            text: "-1"
            pos_hint: {"x": 0.1, "y":0.2}
            size_hint: 0.1, 0.1 
            background_color: 0, 1, 1, 1
            on_press:
                app.Pokedex_Input_Buttons(-1)  

        Button:
            text: "+10"
            pos_hint: {"x": 0, "y":0.3}
            size_hint: 0.1, 0.1
            background_color: 0, 1, 1, 1
            on_press:
                app.Pokedex_Input_Buttons(10)

        Button:
            text: "-10"
            pos_hint: {"x": 0.1, "y":0.3}
            size_hint: 0.1, 0.1
            background_color: 0, 1, 1, 1
            on_press:
                app.Pokedex_Input_Buttons(-10)
                    
        Button:
            text: "+100"
            pos_hint: {"x": 0, "y":0.4}
            size_hint: 0.1, 0.1
            background_color: 0, 1, 1, 1
            on_press:
                app.Pokedex_Input_Buttons(100)
                    
        Button:
            text: "-100" 
            pos_hint: {"x": 0.1, "y":0.4}
            size_hint: 0.1, 0.1
            background_color: 0, 1, 1, 1
            on_press:
                app.Pokedex_Input_Buttons(-100) 

        
    """)


# Global Variables
text_pokedex = "0"
text_catch_tracker = "0"
region = 1

# This part is used for the multiple windows by declaring what they are and where what they should be.
class ScreenOne(Screen):
    pass
class ScreenTwo(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    pass
class ScreenThree(Screen):
    pass
class ScreenFour(Screen):
    pass
class ScreenFive(Screen):
    pass

screen_manager = ScreenManager()
# Main screen
screen_manager.add_widget(ScreenOne(name = "screen_one"))
# Pokedex Screen
screen_manager.add_widget(ScreenTwo(name = "screen_two"))
# Map Screen
screen_manager.add_widget(ScreenThree(name = "screen_three"))
# Move Screen?
screen_manager.add_widget(ScreenFour(name = "screen_four"))
# Catch Tracker
screen_manager.add_widget(ScreenFive(name = "screen_five"))

# This is the main screen
class ScreenApp(App):
    def build(self):
        return screen_manager

# Screen 2 Functions
# This process gets the inputted number.
    def process(self):
        PokeNumberMain = self.root.get_screen('screen_two').ids.PokeNumber.text

# This process is to get the pokedex number and processed to go to the pokedex entry of that pokemon.
    def Search_Click(self):
        global text_pokedex
        dataframe = pd.read_excel('Pokemonstuff2.xlsx')
        text_pokedex = self.root.get_screen('screen_two').ids.PokeNumber.text
        usedtext = float(text_pokedex)


# used to change the pokemon text_pokedex
    def Change_Text(self):
        global text_pokedex
        usedtext = float(text_pokedex)
        dataframe = pd.read_excel('Pokemonstuff2.xlsx')
        # Name string is for the name and the classification of the pokemon
        name_string = str(usedtext) + ": " + str(dataframe.loc[0, usedtext]) +  "\n Species: " + str(dataframe.loc[11, usedtext]) 
        # Type string is for the pokemon type
        type_string = "Types: \n " + str(dataframe.loc[3, usedtext]) 
        # Abilities string is for the pokemon abilities"
        abilities_string = "Abilities: \n" + str(dataframe.loc[14, usedtext])
        # Gender string is for the gender ratio of the pokemon
        gender_string =  "Gender ratio: \n" + str(dataframe.loc[17, usedtext])
        # Stat string is the pokemon stats
        stat_string = "Stat Total: " + str(dataframe.loc[4, usedtext]) + "\n Hp: " + str(dataframe.loc[5, usedtext]) + "\n Attack: " + str(dataframe.loc[6, usedtext]) + "\n Defense: " + str(dataframe.loc[7, usedtext]) + "\n Special Attack: " + str(dataframe.loc[8, usedtext]) + "\n Special Defense: " + str(dataframe.loc[9, usedtext]) + "\n Speed: " + str(dataframe.loc[10, usedtext]) 
        # These ffive commands change the screen to provide accurate information of the newly selected pokemon
        self.root.get_screen('screen_two').ids.Pokemon_Name.text = name_string
        self.root.get_screen('screen_two').ids.Pokemon_Type.text = type_string
        self.root.get_screen('screen_two').ids.Pokemon_Abilities.text = abilities_string
        self.root.get_screen('screen_two').ids.Pokemon_Gender.text = gender_string
        self.root.get_screen('screen_two').ids.Pokemon_Stats.text = stat_string
        # This important set of elif's are to send the correct regional data to the pokedex
        if region == 1:
            entry_output = str(dataframe.loc[20, 0]) + ": " + str(dataframe.loc[20, float(text_pokedex)]) + "\n" + str(dataframe.loc[21, 0]) + ": " + str(dataframe.loc[21, float(text_pokedex)])
        elif region == 2:
            entry_output = str(dataframe.loc[22, 0]) + ": " + str(dataframe.loc[22, float(text_pokedex)]) + "\n" + str(dataframe.loc[23, 0]) + ": " + str(dataframe.loc[23, float(text_pokedex)]) + "\n" + str(dataframe.loc[24, 0]) + ": " + str(dataframe.loc[24, float(text_pokedex)])
        elif region == 3:
             entry_output = str(dataframe.loc[25, 0]) + ": " + str(dataframe.loc[25, float(text_pokedex)]) + "\n" + str(dataframe.loc[26, 0]) + ": " + str(dataframe.loc[26, float(text_pokedex)]) + "\n" + str(dataframe.loc[27, 0]) + ": " + str(dataframe.loc[27, float(text_pokedex)]) + "\n" + str(dataframe.loc[28, 0]) + ": " + str(dataframe.loc[28, float(text_pokedex)]) + "\n" + str(dataframe.loc[29, 0]) + ": " + str(dataframe.loc[29, float(text_pokedex)])
        elif region == 4:
             entry_output = str(dataframe.loc[30, 0]) + ": " + str(dataframe.loc[30, float(text_pokedex)]) + "\n" + str(dataframe.loc[31, 0]) + ": " + str(dataframe.loc[31, float(text_pokedex)]) + "\n" + str(dataframe.loc[32, 0]) + ": " + str(dataframe.loc[32, float(text_pokedex)]) + "\n" + str(dataframe.loc[33, 0]) + ": " + str(dataframe.loc[33, float(text_pokedex)]) + "\n" + str(dataframe.loc[34, 0]) + ": " + str(dataframe.loc[34, float(text_pokedex)])
        elif region == 5:
             entry_output = str(dataframe.loc[35, 0]) + ": " + str(dataframe.loc[35, float(text_pokedex)]) + "\n" + str(dataframe.loc[36, 0]) + ": " + str(dataframe.loc[36, float(text_pokedex)]) + "\n" + str(dataframe.loc[37, 0]) + ": " + str(dataframe.loc[37, float(text_pokedex)]) + "\n" + str(dataframe.loc[38, 0]) + ": " + str(dataframe.loc[38, float(text_pokedex)])
        elif region == 6:
             entry_output = str(dataframe.loc[39, 0]) + ": " + str(dataframe.loc[39, float(text_pokedex)]) + "\n" + str(dataframe.loc[40, 0]) + ": " + str(dataframe.loc[40, float(text_pokedex)]) + "\n" + str(dataframe.loc[41, 0]) + ": " + str(dataframe.loc[41, float(text_pokedex)]) + "\n" + str(dataframe.loc[42, 0]) + ": " + str(dataframe.loc[42, float(text_pokedex)])
        elif region == 7:
             entry_output = str(dataframe.loc[43, 0]) + ": " + str(dataframe.loc[43, float(text_pokedex)]) + "\n" + str(dataframe.loc[44, 0]) + ": " + str(dataframe.loc[44, float(text_pokedex)]) + "\n" + str(dataframe.loc[45, 0]) + ": " + str(dataframe.loc[45, float(text_pokedex)]) + "\n" + str(dataframe.loc[46, 0]) + ": " + str(dataframe.loc[46, float(text_pokedex)])
        elif region == 8: 
             entry_output = str(dataframe.loc[47, 0]) + ": " + str(dataframe.loc[47, float(text_pokedex)]) + "\n" + str(dataframe.loc[48, 0]) + ": " + str(dataframe.loc[48, float(text_pokedex)]) + "\n" + str(dataframe.loc[49, 0]) + ": " + str(dataframe.loc[49, float(text_pokedex)]) + "\n" + str(dataframe.loc[50, 0]) + ": " + str(dataframe.loc[50, float(text_pokedex)]) + "\n" + str(dataframe.loc[51, 0]) + ": " + str(dataframe.loc[51, float(text_pokedex)]) + "\n" + str(dataframe.loc[52, 0]) + ": " + str(dataframe.loc[52, float(text_pokedex)])
        else:
             entry_output = str(dataframe.loc[53, 0]) + ": " + str(dataframe.loc[53, float(text_pokedex)]) + "\n" + str(dataframe.loc[54, 0]) + ": " + str(dataframe.loc[54, float(text_pokedex)]) + "\n" + str(dataframe.loc[55, 0]) + ": " + str(dataframe.loc[55, float(text_pokedex)]) + "\n" + str(dataframe.loc[56, 0]) + ": " + str(dataframe.loc[56, float(text_pokedex)])
        self.root.get_screen("screen_two").ids.Dex_Entry.text = entry_output
        
        
        # This function calls pokemon images. Currently _mf_n images work, which is the female of the pokemon. Males are _md_n and gigantamax forms are _mf_g.
        directory = os.getcwd()
        multipliedBy10 = usedtext * 10
        fraction = int(multipliedBy10 % 10)
        imageNumber = int(usedtext)
        if (fraction != 0):
            normalPokemonImage = directory + "/Images/" +  format(imageNumber, "04") + "_" + format(fraction, "03") + "_mf_n_00000000_f_n.png"
        else:
            normalPokemonImage = directory + "/Images/" +  format(imageNumber, "04") + "_000_mf_n_00000000_f_n.png"
        if (fraction != 0):
            shinyPokemonImage = directory +  "/Images/" +  format(imageNumber, "04") + "_" + format(fraction, "03") + "_mf_n_00000000_f_r.png"
        else:
            shinyPokemonImage = directory + "/Images/" + format(imageNumber, "04") + "_000_mf_n_00000000_f_r.png"
        self.root.get_screen("screen_two").ids.Normal.source = normalPokemonImage
        self.root.get_screen("screen_two").ids.Shiny.source = shinyPokemonImage

# This function is used to change the pokemon number without having to input a number. It takes an input from that is provided by the button functions up top.
    def Pokedex_Input_Buttons(self, input_button_number):
        global text_pokedex
        dataframe = pd.read_excel('Pokemonstuff2.xlsx')
        text_pokedex = float(text_pokedex) + input_button_number
        if (float(text_pokedex) < 1):
            text_pokedex = 1
        if (float(text_pokedex) > 1025):
            text_pokedex = 1025

    

# The next two functions will choose which generation that the pokemon comes from. 
    def Region_Increase(self):
        global region
        if region >= 9:
            region = 9
        else:
            region = region + 1
        dataframe = pd.read_excel('Pokemonstuff2.xlsx')
        if region == 1:
            entry_output = str(dataframe.loc[20, 0]) + ": " + str(dataframe.loc[20, float(text_pokedex)]) + "\n" + str(dataframe.loc[21, 0]) + ": " + str(dataframe.loc[21, float(text_pokedex)])
        elif region == 2:
            entry_output = str(dataframe.loc[22, 0]) + ": " + str(dataframe.loc[22, float(text_pokedex)]) + "\n" + str(dataframe.loc[23, 0]) + ": " + str(dataframe.loc[23, float(text_pokedex)]) + "\n" + str(dataframe.loc[24, 0]) + ": " + str(dataframe.loc[24, float(text_pokedex)])
        elif region == 3:
             entry_output = str(dataframe.loc[25, 0]) + ": " + str(dataframe.loc[25, float(text_pokedex)]) + "\n" + str(dataframe.loc[26, 0]) + ": " + str(dataframe.loc[26, float(text_pokedex)]) + "\n" + str(dataframe.loc[27, 0]) + ": " + str(dataframe.loc[27, float(text_pokedex)]) + "\n" + str(dataframe.loc[28, 0]) + ": " + str(dataframe.loc[28, float(text_pokedex)]) + "\n" + str(dataframe.loc[29, 0]) + ": " + str(dataframe.loc[29, float(text_pokedex)])
        elif region == 4:
             entry_output = str(dataframe.loc[30, 0]) + ": " + str(dataframe.loc[30, float(text_pokedex)]) + "\n" + str(dataframe.loc[31, 0]) + ": " + str(dataframe.loc[31, float(text_pokedex)]) + "\n" + str(dataframe.loc[32, 0]) + ": " + str(dataframe.loc[32, float(text_pokedex)]) + "\n" + str(dataframe.loc[33, 0]) + ": " + str(dataframe.loc[33, float(text_pokedex)]) + "\n" + str(dataframe.loc[34, 0]) + ": " + str(dataframe.loc[34, float(text_pokedex)])
        elif region == 5:
             entry_output = str(dataframe.loc[35, 0]) + ": " + str(dataframe.loc[35, float(text_pokedex)]) + "\n" + str(dataframe.loc[36, 0]) + ": " + str(dataframe.loc[36, float(text_pokedex)]) + "\n" + str(dataframe.loc[37, 0]) + ": " + str(dataframe.loc[37, float(text_pokedex)]) + "\n" + str(dataframe.loc[38, 0]) + ": " + str(dataframe.loc[38, float(text_pokedex)])
        elif region == 6:
             entry_output = str(dataframe.loc[39, 0]) + ": " + str(dataframe.loc[39, float(text_pokedex)]) + "\n" + str(dataframe.loc[40, 0]) + ": " + str(dataframe.loc[40, float(text_pokedex)]) + "\n" + str(dataframe.loc[41, 0]) + ": " + str(dataframe.loc[41, float(text_pokedex)]) + "\n" + str(dataframe.loc[42, 0]) + ": " + str(dataframe.loc[42, float(text_pokedex)])
        elif region == 7:
             entry_output = str(dataframe.loc[43, 0]) + ": " + str(dataframe.loc[43, float(text_pokedex)]) + "\n" + str(dataframe.loc[44, 0]) + ": " + str(dataframe.loc[44, float(text_pokedex)]) + "\n" + str(dataframe.loc[45, 0]) + ": " + str(dataframe.loc[45, float(text_pokedex)]) + "\n" + str(dataframe.loc[46, 0]) + ": " + str(dataframe.loc[46, float(text_pokedex)])
        elif region == 8: 
             entry_output = str(dataframe.loc[47, 0]) + ": " + str(dataframe.loc[47, float(text_pokedex)]) + "\n" + str(dataframe.loc[48, 0]) + ": " + str(dataframe.loc[48, float(text_pokedex)]) + "\n" + str(dataframe.loc[49, 0]) + ": " + str(dataframe.loc[49, float(text_pokedex)]) + "\n" + str(dataframe.loc[50, 0]) + ": " + str(dataframe.loc[50, float(text_pokedex)]) + "\n" + str(dataframe.loc[51, 0]) + ": " + str(dataframe.loc[51, float(text_pokedex)]) + "\n" + str(dataframe.loc[52, 0]) + ": " + str(dataframe.loc[52, float(text_pokedex)])
        else:
             entry_output = str(dataframe.loc[53, 0]) + ": " + str(dataframe.loc[53, float(text_pokedex)]) + "\n" + str(dataframe.loc[54, 0]) + ": " + str(dataframe.loc[54, float(text_pokedex)]) + "\n" + str(dataframe.loc[55, 0]) + ": " + str(dataframe.loc[55, float(text_pokedex)]) + "\n" + str(dataframe.loc[56, 0]) + ": " + str(dataframe.loc[56, float(text_pokedex)])
        self.root.get_screen("screen_two").ids.Dex_Entry.text = entry_output

        
    def Region_Decrease(self):
        global region
        if region <= 1:
            region = 1
        else:
            region = region - 1
        dataframe = pd.read_excel('Pokemonstuff2.xlsx')
        if region == 1:
            entry_output = str(dataframe.loc[20, 0]) + ": " + str(dataframe.loc[20, float(text_pokedex)]) + "\n" + str(dataframe.loc[21, 0]) + ": " + str(dataframe.loc[21, float(text_pokedex)])
        elif region == 2:
            entry_output = str(dataframe.loc[22, 0]) + ": " + str(dataframe.loc[22, float(text_pokedex)]) + "\n" + str(dataframe.loc[23, 0]) + ": " + str(dataframe.loc[23, float(text_pokedex)]) + "\n" + str(dataframe.loc[24, 0]) + ": " + str(dataframe.loc[24, float(text_pokedex)])
        elif region == 3:
             entry_output = str(dataframe.loc[25, 0]) + ": " + str(dataframe.loc[25, float(text_pokedex)]) + "\n" + str(dataframe.loc[26, 0]) + ": " + str(dataframe.loc[26, float(text_pokedex)]) + "\n" + str(dataframe.loc[27, 0]) + ": " + str(dataframe.loc[27, float(text_pokedex)]) + "\n" + str(dataframe.loc[28, 0]) + ": " + str(dataframe.loc[28, float(text_pokedex)]) + "\n" + str(dataframe.loc[29, 0]) + ": " + str(dataframe.loc[29, float(text_pokedex)])
        elif region == 4:
             entry_output = str(dataframe.loc[30, 0]) + ": " + str(dataframe.loc[30, float(text_pokedex)]) + "\n" + str(dataframe.loc[31, 0]) + ": " + str(dataframe.loc[31, float(text_pokedex)]) + "\n" + str(dataframe.loc[32, 0]) + ": " + str(dataframe.loc[32, float(text_pokedex)]) + "\n" + str(dataframe.loc[33, 0]) + ": " + str(dataframe.loc[33, float(text_pokedex)]) + "\n" + str(dataframe.loc[34, 0]) + ": " + str(dataframe.loc[34, float(text_pokedex)])
        elif region == 5:
             entry_output = str(dataframe.loc[35, 0]) + ": " + str(dataframe.loc[35, float(text_pokedex)]) + "\n" + str(dataframe.loc[36, 0]) + ": " + str(dataframe.loc[36, float(text_pokedex)]) + "\n" + str(dataframe.loc[37, 0]) + ": " + str(dataframe.loc[37, float(text_pokedex)]) + "\n" + str(dataframe.loc[38, 0]) + ": " + str(dataframe.loc[38, float(text_pokedex)])
        elif region == 6:
             entry_output = str(dataframe.loc[39, 0]) + ": " + str(dataframe.loc[39, float(text_pokedex)]) + "\n" + str(dataframe.loc[40, 0]) + ": " + str(dataframe.loc[40, float(text_pokedex)]) + "\n" + str(dataframe.loc[41, 0]) + ": " + str(dataframe.loc[41, float(text_pokedex)]) + "\n" + str(dataframe.loc[42, 0]) + ": " + str(dataframe.loc[42, float(text_pokedex)])
        elif region == 7:
             entry_output = str(dataframe.loc[43, 0]) + ": " + str(dataframe.loc[43, float(text_pokedex)]) + "\n" + str(dataframe.loc[44, 0]) + ": " + str(dataframe.loc[44, float(text_pokedex)]) + "\n" + str(dataframe.loc[45, 0]) + ": " + str(dataframe.loc[45, float(text_pokedex)]) + "\n" + str(dataframe.loc[46, 0]) + ": " + str(dataframe.loc[46, float(text_pokedex)])
        elif region == 8: 
             entry_output = str(dataframe.loc[47, 0]) + ": " + str(dataframe.loc[47, float(text_pokedex)]) + "\n" + str(dataframe.loc[48, 0]) + ": " + str(dataframe.loc[48, float(text_pokedex)]) + "\n" + str(dataframe.loc[49, 0]) + ": " + str(dataframe.loc[49, float(text_pokedex)]) + "\n" + str(dataframe.loc[50, 0]) + ": " + str(dataframe.loc[50, float(text_pokedex)]) + "\n" + str(dataframe.loc[51, 0]) + ": " + str(dataframe.loc[51, float(text_pokedex)]) + "\n" + str(dataframe.loc[52, 0]) + ": " + str(dataframe.loc[52, float(text_pokedex)])
        else:
             entry_output = str(dataframe.loc[53, 0]) + ": " + str(dataframe.loc[53, float(text_pokedex)]) + "\n" + str(dataframe.loc[54, 0]) + ": " + str(dataframe.loc[54, float(text_pokedex)]) + "\n" + str(dataframe.loc[55, 0]) + ": " + str(dataframe.loc[55, float(text_pokedex)]) + "\n" + str(dataframe.loc[56, 0]) + ": " + str(dataframe.loc[56, float(text_pokedex)])
        self.root.get_screen("screen_two").ids.Dex_Entry.text = entry_output



# Screen 5 Functions
    def Catch_Tracker(self, input):
        global text_catch_tracker
        dataframe = pd.read_excel('Pokemonstuff2.xlsx')
        # self.root.get_screen('screen_five').ids.

    def Catch_Tracker_Buttons(self, input_catch_tracker_buttons):
        global text_pokedex
        dataframe = pd.read_excel('Pokemonstuff2.xlsx')
        text_catch_tracker = float(text_pokedex) + input_catch_tracker_buttons
        if (float(text_catch_tracker) < 1):
            text_catch_tracker = 1
        if (float(text_catch_tracker) > 1025):
            text_catch_tracker = 1025



# Starts the app when you run the python file
if __name__ == '__main__' :
    ScreenApp().run()






