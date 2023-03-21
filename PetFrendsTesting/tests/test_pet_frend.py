from api import PetFriends
from settings import valid_email, valid_password, no_valid_email, no_valid_password

pf = PetFriends()
def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_all_pets_with_valid_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0

def test_add_new_pet_with_valid_data (name='Almaz', animal_type='malamut',
                                    age='5', pet_photo=r'images\Alaskan_Malamute.jpg'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

def test_successful_delete_self_pet():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, 'Almaz', 'malamut', '5', r'images\Alaskan_Malamute.jpg')
        _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    assert status == 200
    assert pet_id not in my_pets.values()


def test_successful_update_self_pet_info(name='Ydja', animal_type='shpiz', age='5'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200
        assert result['name'] == name
    else:
        raise Exception("There is no my pets")


def test_add_new_pet_simple_with_valid_data(name='Pluton', animal_type='dzhekraasel', age='3'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name

def test_add_photo_pet_valid_format(pet_photo = r'C:\Users\Пользователь\PycharmProjects\учеба\PetFrendsTesting\tests\images\kot.jpg'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    if len(my_pets['pets']) > 0:
        if my_pets['pet_photo'] is null:
            status, result = pf.add_photo_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)
            assert status == 200
            assert result['pet_photo'] is not null
        else:
            raise Exception("Pet has a photo")
    else:
        raise Exception("There is no my pets")



def test_get_api_key_for_NO_valid_user1(email=valid_email, password=no_valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert 'key' is not result

def test_add_new_pet_with_NO_valid_data (name='Almazik', animal_type='xaski',
                                    age='1', pet_photo=r'images\song.txt'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 500
    assert result['name'] == name





