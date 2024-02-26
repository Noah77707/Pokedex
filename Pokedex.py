import os
from os import listdir
from pathlib import Path
from pandas import read_excel
from decimal import Decimal, getcontext
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.lang import Builder
from kivy.core.window import Window
import csv

# Information:
# Every id/program created in Kivy is to start with a capital letter.
# Every def/program created in python is to have no capital letters.
# The screens are to share the same color, but have different colors for the different screens.
# Thing that are commented out are things I think I might need in the future. They will either be reimplimented, or they will be deleted next patch
# the version number is updated upon something I believe to be a huge milestone: These are in the README.txt

# This makes the window be the correct size for the raspberry pi.
Window.fullscreen = 'auto'
print(Window.size)

# This builds the correct file
Builder.load_file("pokedexkv.kv")

# Global Variables
text_pokedex = float(0)
form_value = text_pokedex
text_catch_tracker = "0"
region = 1
map_value = 0
pokedex_file = read_excel('Pokemonstuff2.xlsx')
directory = os.getcwd()

# This part is used for the multiple windows by declaring what they are and where what they should be.
class ScreenOne(Screen):
    pass
class ScreenTwo(Screen):
    pass
class ScreenThree(Screen):
    pass
class ScreenFour(Screen):
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

# Function to change the Generations that the pokedex shows
def Region_Change(value):
        global pokedex_file
        if value == 1:
            return str(pokedex_file.loc[20, 0]) + ": " + str(pokedex_file.loc[20, float(text_pokedex)]) + "\n" + str(pokedex_file.loc[21, 0]) + ": " + str(pokedex_file.loc[21, float(text_pokedex)])
        elif value == 2:
            return str(pokedex_file.loc[22, 0]) + ": " + str(pokedex_file.loc[22, float(text_pokedex)]) + "\n" + str(pokedex_file.loc[23, 0]) + ": " + str(pokedex_file.loc[23, float(text_pokedex)]) + "\n" + str(pokedex_file.loc[24, 0]) + ": " + str(pokedex_file.loc[24, float(text_pokedex)])
        elif value == 3:
             return str(pokedex_file.loc[25, 0]) + ": " + str(pokedex_file.loc[25, float(text_pokedex)]) + "\n" + str(pokedex_file.loc[26, 0]) + ": " + str(pokedex_file.loc[26, float(text_pokedex)]) + "\n" + str(pokedex_file.loc[27, 0]) + ": " + str(pokedex_file.loc[27, float(text_pokedex)]) + "\n" + str(pokedex_file.loc[28, 0]) + ": " + str(pokedex_file.loc[28, float(text_pokedex)]) + "\n" + str(pokedex_file.loc[29, 0]) + ": " + str(pokedex_file.loc[29, float(text_pokedex)])
        elif value == 4:
             return str(pokedex_file.loc[30, 0]) + ": " + str(pokedex_file.loc[30, float(text_pokedex)]) + "\n" + str(pokedex_file.loc[31, 0]) + ": " + str(pokedex_file.loc[31, float(text_pokedex)]) + "\n" + str(pokedex_file.loc[32, 0]) + ": " + str(pokedex_file.loc[32, float(text_pokedex)]) + "\n" + str(pokedex_file.loc[33, 0]) + ": " + str(pokedex_file.loc[33, float(text_pokedex)]) + "\n" + str(pokedex_file.loc[34, 0]) + ": " + str(pokedex_file.loc[34, float(text_pokedex)])
        elif value == 5:
             return str(pokedex_file.loc[35, 0]) + ": " + str(pokedex_file.loc[35, float(text_pokedex)]) + "\n" + str(pokedex_file.loc[36, 0]) + ": " + str(pokedex_file.loc[36, float(text_pokedex)]) + "\n" + str(pokedex_file.loc[37, 0]) + ": " + str(pokedex_file.loc[37, float(text_pokedex)]) + "\n" + str(pokedex_file.loc[38, 0]) + ": " + str(pokedex_file.loc[38, float(text_pokedex)])
        elif value == 6:
             return str(pokedex_file.loc[39, 0]) + ": " + str(pokedex_file.loc[39, float(text_pokedex)]) + "\n" + str(pokedex_file.loc[40, 0]) + ": " + str(pokedex_file.loc[40, float(text_pokedex)]) + "\n" + str(pokedex_file.loc[41, 0]) + ": " + str(pokedex_file.loc[41, float(text_pokedex)]) + "\n" + str(pokedex_file.loc[42, 0]) + ": " + str(pokedex_file.loc[42, float(text_pokedex)])
        elif value == 7:
             return str(pokedex_file.loc[43, 0]) + ": " + str(pokedex_file.loc[43, float(text_pokedex)]) + "\n" + str(pokedex_file.loc[44, 0]) + ": " + str(pokedex_file.loc[44, float(text_pokedex)]) + "\n" + str(pokedex_file.loc[45, 0]) + ": " + str(pokedex_file.loc[45, float(text_pokedex)]) + "\n" + str(pokedex_file.loc[46, 0]) + ": " + str(pokedex_file.loc[46, float(text_pokedex)])
        elif value == 8: 
             return str(pokedex_file.loc[47, 0]) + ": " + str(pokedex_file.loc[47, float(text_pokedex)]) + "\n" + str(pokedex_file.loc[48, 0]) + ": " + str(pokedex_file.loc[48, float(text_pokedex)]) + "\n" + str(pokedex_file.loc[49, 0]) + ": " + str(pokedex_file.loc[49, float(text_pokedex)]) + "\n" + str(pokedex_file.loc[50, 0]) + ": " + str(pokedex_file.loc[50, float(text_pokedex)]) + "\n" + str(pokedex_file.loc[51, 0]) + ": " + str(pokedex_file.loc[51, float(text_pokedex)]) + "\n" + str(pokedex_file.loc[52, 0]) + ": " + str(pokedex_file.loc[52, float(text_pokedex)])
        else:
            return str(pokedex_file.loc[53, 0]) + ": " + str(pokedex_file.loc[53, float(text_pokedex)]) + "\n" + str(pokedex_file.loc[54, 0]) + ": " + str(pokedex_file.loc[54, float(text_pokedex)]) 

def Region_Name(value):
    if value == 1:
        return "Kanto"
    elif value == 2:
        return "Johto"
    elif value == 3:
        return "Hoenn"
    elif value == 4:
        return "Sinnoh"
    elif value == 5:
        return "Unova"
    elif value == 6:
        return "Kalos"
    elif value == 7:
        return "Alola"
    elif value == 8:
        return "Galar"
    elif value == 9:
        return "Paldea"
    else:
        return "No Region"

# def Type_Effectiveness_Chart(value):
#     global pokedex_file
#     pokemon_types = str(pokedex_file.loc[3, value]).split()
#     type_chart_offensive = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#     type_chart_defensive = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#     type_list = ["Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting", "Poison", "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"]
#     for x in range(len(pokemon_types)):
#         try:
#             index = type_list.index(pokemon_types[x])
#             print(index)
#             print(str(pokedex_file.loc[98, 12+index]))
#         except:
#             print("Not recognized type")



# This is the main screen
class PokedexApp(App):
    def build(self):
        return screen_manager

# Screen 2 Functions
# This process gets the inputted number.
    def process(self):
        PokeNumberMain = self.root.get_screen('screen_two').ids.PokeNumber.text

# This process is to get the pokedex number and processed to go to the pokedex entry of that pokemon.
    def Search_Click(self):
        global text_pokedex
        text_pokedex = self.root.get_screen('screen_two').ids.PokeNumber.text
        usedtext = float(text_pokedex)


# used to change the pokemon text_pokedex
    def Change_Text(self):
        global text_pokedex
        global pokedex_file
        usedtext = float(text_pokedex)
        # Name string is for the name and the classification of the pokemon
        name_string = str(usedtext) + ": " + str(pokedex_file.loc[0, usedtext]) +  "\n Species: " + str(pokedex_file.loc[11, usedtext]) 
        # Type string is for the pokemon type
        type_string = "Types: \n " + str(pokedex_file.loc[3, usedtext]) 
        # Abilities string is for the pokemon abilities"
        abilities_string = "Abilities: \n" + str(pokedex_file.loc[14, usedtext])
        # Stat string is the pokemon stats
        stat_string = "Stat Total: " + str(pokedex_file.loc[4, usedtext]) + "\n Hp: " + str(pokedex_file.loc[5, usedtext]) + "\n Attack: " + str(pokedex_file.loc[6, usedtext]) + "\n Defense: " + str(pokedex_file.loc[7, usedtext]) + "\n Special Attack: " + str(pokedex_file.loc[8, usedtext]) + "\n Special Defense: " + str(pokedex_file.loc[9, usedtext]) + "\n Speed: " + str(pokedex_file.loc[10, usedtext]) 
        # These ffive commands change the screen to provide accurate information of the newly selected pokemon
        self.root.get_screen('screen_two').ids.Pokemon_Name.text = name_string
        self.root.get_screen('screen_two').ids.Pokemon_Type.text = type_string
        self.root.get_screen('screen_two').ids.Pokemon_Abilities.text = abilities_string
        self.root.get_screen('screen_two').ids.Pokemon_Stats.text = stat_string
        # This important set of elif's are to send the correct regional data to the pokedex
        entry_output = Region_Change(region)
        self.root.get_screen("screen_two").ids.Dex_Entry.text = entry_output
        
        
        # This function calls pokemon images. Currently _mf_n images work, which is the female of the pokemon. Males are _md_n and gigantamax forms are _mf_g.
        global directory
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
        global pokedex_file
        text_pokedex = int(text_pokedex) + input_button_number
        pokedex_number_check = text_pokedex
        if (int(text_pokedex) < 1):
            text_pokedex = 1
        if (int(text_pokedex) > 1025):
            text_pokedex = 1025

# The next two functions will choose which generation that the pokemon comes from. 
    def Region_Change(self, value):
        global region
        global pokedex_file
        region = region + value
        if region > 9:
            region = 9
        elif region < 1:
            region = 1
        entry_output = Region_Change(region)
        self.root.get_screen("screen_two").ids.Dex_Entry.text = entry_output

    def Form_Change(self, value):
        global text_pokedex
        global pokedex_file
        try:
            text_pokedex = round(text_pokedex + value, 2)
            print(pokedex_file.loc[0, text_pokedex])
        except:
            text_pokedex = round(text_pokedex - value)
            print("there is no alt form")

# Screen 3 Functions
    def Region_Map(self):
        global directory
        global map_value
        Regional_Map = directory + "/Images/" + "Gen" + str(map_value) + "Map.png"
        self.root.get_screen("screen_three").ids.Map_Image.source = Regional_Map

    def Map_Changer(self, value):
        global map_value
        map_value = map_value + value
        if (map_value > 9):
            map_value = 9
        elif (map_value < 1):
            map_value = 1
        self.root.get_screen("screen_three").ids.Increase_Map.text = Region_Name(map_value + 1) 
        self.root.get_screen("screen_three").ids.Map_Name.text = Region_Name(map_value) 
        self.root.get_screen("screen_three").ids.Decrease_Map.text = Region_Name(map_value - 1)





# Screen 5 Functions
    def Catch_Tracker(self, input):
        global text_catch_tracker
        global pokedex_file
        # self.root.get_screen('screen_five').ids.

    def Catch_Tracker_Buttons(self, input_catch_tracker_buttons):
        global text_pokedex
        global pokedex_file
        text_catch_tracker = float(text_pokedex) + input_catch_tracker_buttons
        if (float(text_catch_tracker) < 1):
            text_catch_tracker = 1
        if (float(text_catch_tracker) > 1025):
            text_catch_tracker = 1025



# Starts the app when you run the python file
if __name__ == '__main__' :
    PokedexApp().run()






