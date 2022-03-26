from urllib import request
import requests
class dog:
    def __init__(self, name, breed_type): #self means the dog
        self.name = name
        self.breed_type = breed_type

    def get_name(self):
        print (self.name)

    def get_breed_img(self):
        response = requests.get('https://dog.ceo/api/breed/'+self.breed_type+'/images')
        print(response.content)
        print("retrieving imgs of breed", self.breed_type)