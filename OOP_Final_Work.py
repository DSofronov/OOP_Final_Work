import requests
from pprint import pprint

class VK:
    url = 'https://api.vk.com/method/'

    def __init__(self, vk_token, version):
        self.params = {'access_token': vk_token,
                       'v': version}

    def get_photos_from_vk(self, user_id, offset=0):
        url_photo = 'https://api.vk.com/method/photos.get'
        photos_params = {'owner_id': user_id,
                         'album_id': 'profile',
                         'extended': 1,
                         'photo_sizes': 1,
                         'offset': offset,
                         'count': 5}
        response = requests.get(url_photo, params={**self.params, **photos_params})
        photos = response.json()
        return photos

if __name__ == '__main__':
    vk_token = ''
    version = '5.131'
    user_id = input('Введите id: ')
    vk = VK(vk_token, version)
    photos = vk.get_photos_from_vk(user_id)
    pprint(photos)