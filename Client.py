import vk


class Useraction(object):

    def __init__(self, user_login, user_password, url_vk):
        self.user_login = user_login
        self.user_password = user_password
        self.url_vk = url_vk

    def authentication(self):
        session = vk.AuthSession(app_id=6463497, user_login=self.user_login,
                                 user_password=self.user_password,
                                 scope="photos")
        api = vk.API(session)
        return api

    def get_inforalbum(self):
        url = self.url_vk
        owner_id, album_id = url[url.rfind('-'):].split('_')
        return int(owner_id), int(album_id)

    def get_photos(self, api):
        owner, album = self.get_inforalbum()
        saved_photo = api.photos.get(owner_id=owner, album_id=album,
                                     version=5.74)
        photo_urls = [infor['src_big'] for infor in saved_photo]
        return photo_urls
