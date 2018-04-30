from Client import Useraction
import os
import requests
import shutil
import getpass
from multiprocessing import Pool
from functools import partial


def create_folder(name_folder):
    if not os.path.exists(name_folder):
        os.makedirs(name_folder, exist_ok=True)
    print("Folder {} is created!".format(name_folder))
    return name_folder


def photos_download(url, name_folder):
    response = requests.get(url, stream=True)
    name_image = url[url.rfind('/'):]
    save_path = name_folder + name_image
    with open(save_path, 'wb') as f:
        shutil.copyfileobj(response.raw, f)
        print('Download {} completed!'.format(name_image))


def main():
    # Your input
    login = input("Enter your account: ")
    password = getpass.getpass("Enter your password: ")
    url = input("Enter url album: ")

    # Call User, create folder and get photos url
    try:
        user = Useraction(user_login=login, user_password=password, url_vk=url)
        api = user.authentication()
        photo_urls = user.get_photos(api)
        folder = create_folder(str(user.get_inforalbum()[1]))

    # Download photo
        p = Pool()
        p.map(partial(photos_download, name_folder=folder), photo_urls)
    except Exception as e:
        print(e)
    finally:
        print('Done!')


if __name__ == '__main__':
    main()
