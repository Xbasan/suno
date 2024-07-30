import json
import time
import requests
import os
import shutil


class api:
    def __init__(self):
        self.res_json = {}
        self.api_url = "https://udioapi.pro/api/generate" 
        self.prompt_json = {
            "title": "",
            "prompt": "",
            "gpt_description_prompt": "pop",
            "custom_mode": 'false',  
            "make_instrumental": 'false',
            "model": "chirp-v3.0", 
            "continue_clip_id": "",             
            "continue_at": "", 
            "callback_url":"",  
            "token":"aXVWQ6NBbpv7s8zOCyd94"         
        }
         
    def create(self,
        title = '',
        prompt = '',
        custom_mode = False,
        make_instrumental = False,
        model = 'chirp-v3.0',    
        continue_clip_id = '',
        continue_at = '', 
        callback_url = 'https://www.google.com'          
    ):
        if len(title) <= 90 and len(prompt) <= 90:
            self.prompt_json['title'] = title
            self.prompt_json['prompt'] = prompt
            self.prompt_json['custom_mode'] = custom_mode
            self.prompt_json['make_instrumental'] = make_instrumental
            self.prompt_json['model'] = model 
            self.prompt_json['continue_clip_id'] = continue_clip_id
            self.prompt_json['continue_at'] = continue_at
            self.prompt_json["callback_url"] = callback_url
        else:
            print(prompt[:100])
            self.prompt_json['title'] = title[:90]
            self.prompt_json['prompt'] = prompt[:90]
            self.prompt_json['custom_mode'] = custom_mode
            self.prompt_json['make_instrumental'] = make_instrumental
            self.prompt_json['model'] = model 
            self.prompt_json['continue_clip_id'] = continue_clip_id
            self.prompt_json['continue_at'] = continue_at
            self.prompt_json["callback_url"] = callback_url

    # Отвечает за генерацию токена
    # Responsible for token generation    
    def token(self, test=""):
        email_json = {"userEmail":"hamzatganukae@gmail.com"}
        token_rec = requests.post(url="https://udioapi.pro/api/token-g", json=email_json).json()
        self.prompt_json['token'] = token_rec['token']
        
        if test != "" : 
            print(self.prompt_json['token'])
        
    # Отвечает за выбор жанра музыки
    # Responsible for choosing the genre of music
    def gpt_prompt(self, gpt_description_prompt):
        self.prompt_json['gpt_description_prompt'] = gpt_description_prompt

    # Делает запрос для генерации музыки
    # Makes a request to generate music
    def ai_requsts(self):                
        res = requests.post(url=self.api_url, json = self.prompt_json)
        
        if res.json() == {'message': 'prompt too long'}:
            print('Длина промпта привышает норму')
            # print(self.prompt_json)
        else:
            if 'workId' in res.json():
                self.res_json = res.json() 
                print(self.res_json)
            else:
                print(res.json())
                self.res_json = {
                    "message": 'success',
                    "workId": 'KNH2b7uhXT7lvrZnxPRWG'
                }
           


    # ЗАПИСЫВАЕТ ДАННЫЕ ПЕСНИ В JSON ФАЙЛ
    # WRITES SONG DATA TO JSON FILE
    def save_music(self, music_json={}):
        os.makedirs("music", exist_ok=True)

        with open('music/music.json', "a+") as file:
            file.write(f"{music_json}")

    # ЧИТАЕТ ДАННЫЕ ПЕСНИ В JSON ФАЙЛ
    # READS SONG DATA INTO JSON FILE
    def readings_music_list(self):
        with open("music/music.json", "r") as file:
            music_file_json = file.readlines()       
        return music_file_json
    
        
    # Генерирует ответ с ссылкой на музыку
    # Generates a response with a link to the music
    
    # НУЖНО СДЕЛАТЬ АСИНХРОННОЙ
    # NEEDS TO BE MADE ASYNCHRONOUS
    def res_music(self):
        # time.sleep(90)                
        res_api_url = 'https://udioapi.pro/api/feed?workId='

        while True:
            res_api_json = requests.post(url=f'{ res_api_url }{ self.res_json['workId'] }').json()
            # res_api_json = requests.post(url=f'{ res_api_url }KNH2b7uhXT7lvrZnxPRWG').json()            
            try:
                info = json.loads(res_api_json['data'][-1]['info'])['data']['data']
                
                if json.loads(res_api_json['data'][-1]['info'])['data']['data'][0]['audio_url'] != '':
                      
                    audio_url_0 = info[0]['audio_url']
                    audio_url_1 = info[1]['audio_url']
                                        
                    image_url_0 = info[0]['image_url']
                    image_url_1 = info[1]['image_url']

                    res = {}

                    res["title"] = info[0]['title'],
                    res["audio_url_0"] = audio_url_0,
                    res["image_url_0"] = image_url_0, 
                    res["audio_url_1"] = audio_url_1, 
                    res["image_url_1"] = image_url_1,
                    res["text_music_0"] = text_music_0,
                    res["text_music_1"] = text_music_1,

                    save_music(res)
                                        
                    return res
                else:
                    text_music_0 = info[0]["prompt"]
                    text_music_1 = info[1]["prompt"] 
                    time.sleep(60)
            except KeyError:
                time.sleep(60)
                 

def main():
    ap = api()
    ap.token(test=" ")
    ap.gpt_prompt('рэп')
    ap.create('заголовак' ,input("Введи текст песни  ") )
    ap.ai_requsts()
    # print(ap.res_music())
    # print(ap.readings_music_list()[0])    
    
if __name__ == "__main__":
    main()
