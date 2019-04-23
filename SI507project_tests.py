# SI507project_tests.py

from SI507project_tools import *
import unittest
import itertools

class PartOne(unittest.TestCase):
    def test_park_info_csv(self):
        self.cleaned_file = open('park_info.csv','r')
        self.row_reader = self.cleaned_file.readlines()
        # print(self.row_reader) # For debug
        self.assertTrue(self.row_reader[1].split(",")[0], "Testing that there is a Park / first value in the row at index 1")
        self.assertTrue(self.row_reader[25].split(",")[0], "Testing that there is a Park / first value in the row at index 25")
        self.cleaned_file.close()

    def test_park_info2_csv(self):
        cleaned_file = open('park_info.csv','r')
        self.contents = cleaned_file.readlines()
        cleaned_file.close()
        self.assertTrue('"Birmingham Civil Rights","National Monument","AL"," In 1963, images of snarling police dogs unleashed against non-violent protesters and of children being sprayed with high-pressure hoses appeared in print and television news across the world. These dramatic scenes from Birmingham, Alabama, of violent police aggression against civil rights protesters were vivid examples of segregation and racial injustice in America. ","Alabama"\n' in self.contents, "Testing that the Harriet Tubman line exists correctly with formatted location & proper description in the clean file")
        self.assertTrue('"Green Springs","None","Louisa County, VA"," Green Springs National Historic Landmark District in Virginia’s Piedmont encompasses over 14,000 acres. Its farmsteads offer a continuum of rural vernacular architecture in original context with minimal alteration. Landscapes and buildings, many predating the Civil War and connected to one another visually and through family relationships of early occupants, are today preserved through easements. ","Virginia"\n' in self.contents, "Testing that the Green Springs line exists correctly with formatted location & proper description in the clean file")

class PartTwo(unittest.TestCase):
    def test_states_csv(self):
        self.cleaned_file = open('states.csv','r')
        self.row_reader = self.cleaned_file.readlines()
        # print(self.row_reader) # For debug
        self.assertTrue(self.row_reader[1].split(",")[0], "Testing that there is a Park / first value in the row at index 1")
        self.assertTrue(self.row_reader[25].split(",")[0], "Testing that there is a Park / first value in the row at index 25")
        self.cleaned_file.close()

    def test_states_csv2(self):
        cleaned_file = open('states.csv','r')
        self.contents = cleaned_file.readlines()
        cleaned_file.close()
        self.assertTrue('"Illinois","IL","https://www.nps.gov/state/il/index.htm"\n' in self.contents, "Testing that the Illinois line exists correctly with formatted abbreviation & proper URL in the clean file")
        self.assertTrue('"Virgin Islands","VI","https://www.nps.gov/state/vi/index.htm"\n' in self.contents, "Testing that the Virgin Islands line exists correctly with formatted abbreviation & proper URL in the clean file")


class PartThree(unittest.TestCase):
    def test_parks_csv(self):
        self.cleaned_file = open('parks.csv','r')
        self.row_reader = self.cleaned_file.readlines()
        # print(self.row_reader) # For debug
        self.assertTrue(self.row_reader[1].split(",")[0], "Testing that there is a Park / first value in the row at index 1")
        self.assertTrue(self.row_reader[25].split(",")[0], "Testing that there is a Park / first value in the row at index 25")
        self.cleaned_file.close()

    def test_parks_csv2(self):
        cleaned_file = open('parks.csv','r')
        self.contents = cleaned_file.readlines()
        cleaned_file.close()
        self.assertTrue('''18,Denali,"Denali Park, AK"," Denali is six million acres of wild land, bisected by one ribbon of road. Travelers along it see the relatively low-elevation taiga forest give way to high alpine tundra and snowy mountains, culminating in North America's tallest peak, 20,310' Denali. Wild animals large and small roam un-fenced lands, living as they have for ages. Solitude, tranquility and wilderness await. ",Alaska,"February 26, 1917",594660.0\n''' in self.contents, "Testing that the Alagnak line exists correctly with correct location, description, establish date and vistor numbers in the clean file")
        self.assertTrue('''47,Petrified Forest,"Petrified Forest National Park, AZ"," Did you know that Petrified Forest is more spectacular than ever? While the park has all the wonders known for a century, there are many new adventures and discoveries to share. There are backcountry hikes into areas never open before such as Red Basin and little known areas like the Martha's Butte. There are new exhibits that bring the stories to life. Come rediscover Petrified Forest! ",Arizona,"December 9, 1962",644922.0\n''' in self.contents, "Testing that the Petrified Forest line exists correctly with correct location, description, establish date and vistor numbers in the clean file")




if __name__ == "__main__":
    unittest.main(verbosity=2)
