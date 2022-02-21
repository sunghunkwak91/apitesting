import requests
import json

def test_User():
    print("/n", "************ Test User API ************")

    # Create New User 1
    url_createUser = "https://petstore.swagger.io/v2/user"
    f = open('/Users/sunghunkwak/PycharmProjects/apiTesting/createUser/createUser1.json', 'r')
    user_info = json.loads(f.read())
    createUser = requests.post(url_createUser, json=user_info)
    assert createUser.status_code == 200

    # Create New User 2
    url_createUser = "https://petstore.swagger.io/v2/user"
    f = open('/Users/sunghunkwak/PycharmProjects/apiTesting/createUser/createUser2.json', 'r')
    user_info = json.loads(f.read())
    createUser = requests.post(url_createUser, json=user_info)
    assert createUser.status_code == 200

    # Create New User 3
    url_createUser = "https://petstore.swagger.io/v2/user"
    f = open('/Users/sunghunkwak/PycharmProjects/apiTesting/createUser/createUser3.json', 'r')
    user_info = json.loads(f.read())
    createUser = requests.post(url_createUser, json=user_info)
    assert createUser.status_code == 200

    # Get User 1 info
    url_getUser = "https://petstore.swagger.io/v2/user/jameskwak"
    getUser = requests.get(url_getUser)
    assert getUser.status_code == 200
    print(getUser.text)

    # Get User 2 info
    url_getUser = "https://petstore.swagger.io/v2/user/peterlee"
    getUser = requests.get(url_getUser)
    assert getUser.status_code == 200
    print(getUser.text)

    # Get User 3 info
    url_getUser = "https://petstore.swagger.io/v2/user/leahlee"
    getUser = requests.get(url_getUser)
    assert getUser.status_code == 200
    print(getUser.text)

    print("************** User Login **************")

    #####################
    #    User Login     #
    #####################
    # User1 log in
    url_login = "https://petstore.swagger.io/v2/user/login?username=jameskwak&password=jameskwak"
    userLogin = requests.get(url_login)
    assert userLogin.status_code == 200
    print(userLogin.text)

    # User2 log in
    url_login = "https://petstore.swagger.io/v2/user/login?username=peterlee&password=peterlee"
    userLogin = requests.get(url_login)
    assert userLogin.status_code == 200
    print(userLogin.text)

    # User3 log in
    url_login = "https://petstore.swagger.io/v2/user/login?username=leahlee&password=leahlee"
    userLogin = requests.get(url_login)
    assert userLogin.status_code == 200
    print(userLogin.text)

    # Log out All users
    url_logout = "https://petstore.swagger.io/v2/user/logout"
    userLogout = requests.get(url_logout)
    assert userLogout.status_code == 200
    print(userLogout.text)

    # Delete User1
    url_deleteUser = "https://petstore.swagger.io/v2/user/jameskwak"
    deleteUser = requests.delete(url_deleteUser)
    assert deleteUser.status_code == 200

    # Delete User2
    url_deleteUser = "https://petstore.swagger.io/v2/user/peterlee"
    deleteUser = requests.delete(url_deleteUser)
    assert deleteUser.status_code == 200

    # Delete User3
    url_deleteUser = "https://petstore.swagger.io/v2/user/leahlee"
    deleteUser = requests.delete(url_deleteUser)
    assert deleteUser.status_code == 200

    # Get User1
    url_getUser = "https://petstore.swagger.io/v2/user/jameskwak"
    getDeletedUser = requests.get(url_getUser)
    assert getDeletedUser.status_code == 404
    print(getDeletedUser.text)

    # Get User2
    url_getUser = "https://petstore.swagger.io/v2/user/peterlee"
    getDeletedUser = requests.get(url_getUser)
    assert getDeletedUser.status_code == 404
    print(getDeletedUser.text)

    # Get User3
    url_getUser = "https://petstore.swagger.io/v2/user/leahlee"
    getDeletedUser = requests.get(url_getUser)
    assert getDeletedUser.status_code == 404
    print(getDeletedUser.text)

def test_Pet():
    print("************ Test Pet API ************")

    # Create New Pet 1
    url_createPet = "https://petstore.swagger.io/v2/pet"
    f = open('/Users/sunghunkwak/PycharmProjects/apiTesting/createPet/createPet1.json', 'r')
    pet_info = json.loads(f.read())
    createPet = requests.post(url_createPet, json=pet_info)
    assert createPet.status_code == 200

    # Create New Pet 2
    url_createPet = "https://petstore.swagger.io/v2/pet"
    f = open('/Users/sunghunkwak/PycharmProjects/apiTesting/createPet/createPet2.json', 'r')
    pet_info = json.loads(f.read())
    createPet = requests.post(url_createPet, json=pet_info)
    assert createPet.status_code == 200

    # Create New Pet 3
    url_createPet = "https://petstore.swagger.io/v2/pet"
    f = open('/Users/sunghunkwak/PycharmProjects/apiTesting/createPet/createPet3.json', 'r')
    pet_info = json.loads(f.read())
    createPet = requests.post(url_createPet, json=pet_info)
    assert createPet.status_code == 200

    # Get Pet 1 info
    url_getPet = "https://petstore.swagger.io/v2/pet/111"
    getPet = requests.get(url_getPet)
    assert getPet.status_code == 200
    print(getPet.text)

    # Get Pet 2 info
    url_getPet = "https://petstore.swagger.io/v2/pet/222"
    getPet = requests.get(url_getPet)
    assert getPet.status_code == 200
    print(getPet.text)

    # Get Pet 3 info
    url_getPet = "https://petstore.swagger.io/v2/pet/333"
    getPet = requests.get(url_getPet)
    assert getPet.status_code == 200
    print(getPet.text)

    print("************** Update Pet status **************")
    #####################
    # Update Pet 1 info #
    #####################
    url_updatePet = "https://petstore.swagger.io/v2/pet"
    f = open('/Users/sunghunkwak/PycharmProjects/apiTesting/createPet/UpdateCreatePet1.json', 'r')
    pet_info = json.loads(f.read())
    updatePet = requests.post(url_updatePet, json=pet_info)
    assert updatePet.status_code == 200
    # Get Updated Pet 1 info
    url_getPet = "https://petstore.swagger.io/v2/pet/111"
    getPet = requests.get(url_getPet)
    assert getPet.status_code == 200
    print(getPet.text)

    #####################
    # Update Pet 2 info #
    #####################
    url_updatePet = "https://petstore.swagger.io/v2/pet"
    f = open('/Users/sunghunkwak/PycharmProjects/apiTesting/createPet/UpdateCreatePet2.json', 'r')
    pet_info = json.loads(f.read())
    updatePet = requests.post(url_updatePet, json=pet_info)
    assert updatePet.status_code == 200
    # Get Updated Pet 2 info
    url_getPet = "https://petstore.swagger.io/v2/pet/222"
    getPet = requests.get(url_getPet)
    assert getPet.status_code == 200
    print(getPet.text)

    #####################
    # Update Pet 3 info #
    #####################
    url_updatePet = "https://petstore.swagger.io/v2/pet"
    f = open('/Users/sunghunkwak/PycharmProjects/apiTesting/createPet/UpdateCreatePet3.json', 'r')
    pet_info = json.loads(f.read())
    updatePet = requests.post(url_updatePet, json=pet_info)
    assert updatePet.status_code == 200
    # Get Updated Pet 3 info
    url_getPet = "https://petstore.swagger.io/v2/pet/333"
    getPet = requests.get(url_getPet)
    assert getPet.status_code == 200
    print(getPet.text)

    #Get Avaiable pets
    url_getAvailablePets = "https://petstore.swagger.io/v2/pet/findByStatus?status=available"
    getPetAvailable = requests.get(url_getAvailablePets)
    assert getPetAvailable.status_code == 200

    print("************** Delete Pet 1 ( sold ) **************")
    # Delete Pet 1
    url_deletePet = "https://petstore.swagger.io/v2/pet/111"
    deletePet = requests.delete(url_deletePet)
    assert deletePet.status_code == 200
    # Get Pet 1 info
    url_getPet = "https://petstore.swagger.io/v2/pet/111"
    getPet = requests.get(url_getPet)
    assert getPet.status_code == 404
    print("Pet 1 = ", getPet.text)

def test_Store():

    print("************ Test Store API ************")

    # Create New Order 1
    url_createOrder = "https://petstore.swagger.io/v2/store/order"
    f = open('/Users/sunghunkwak/PycharmProjects/apiTesting/createOrder/createOrder1.json', 'r')
    order_info = json.loads(f.read())
    createOrder = requests.post(url_createOrder, json=order_info)
    assert createOrder.status_code == 200
    # Create New Order 2
    url_createOrder = "https://petstore.swagger.io/v2/store/order"
    f = open('/Users/sunghunkwak/PycharmProjects/apiTesting/createOrder/createOrder2.json', 'r')
    order_info = json.loads(f.read())
    createOrder = requests.post(url_createOrder, json=order_info)
    assert createOrder.status_code == 200

    # Create New Order 3
    url_createOrder = "https://petstore.swagger.io/v2/store/order"
    f = open('/Users/sunghunkwak/PycharmProjects/apiTesting/createOrder/createOrder3.json', 'r')
    order_info = json.loads(f.read())
    createOrder = requests.post(url_createOrder, json=order_info)
    assert createOrder.status_code == 200

    # Get Order 1 info
    url_getOrder = "https://petstore.swagger.io/v2/store/order/202001"
    getOrder = requests.get(url_getOrder)
    print(getOrder.status_code)
    print("\n", getOrder.text)

    # Get Order 2 info
    url_getOrder = "https://petstore.swagger.io/v2/store/order/202002"
    getOrder = requests.get(url_getOrder)
    assert getOrder.status_code == 200
    print(getOrder.text)

    # Get Order 3 info
    url_getOrder = "https://petstore.swagger.io/v2/store/order/202003"
    getOrder = requests.get(url_getOrder)
    assert getOrder.status_code == 200
    print(getOrder.text)

    #####################
    #   Delete Orders   #
    #####################
    print("************* Delete Orders *************")
    # Delete Order 1
    url_deleteOrder = "https://petstore.swagger.io/v2/store/order/202001"
    deleteOrder = requests.delete(url_deleteOrder)
    # print(deleteOrder.status_code)
    assert deleteOrder.status_code == 200

    # Delete Order 2
    url_deleteOrder = "https://petstore.swagger.io/v2/store/order/202002"
    deleteOrder = requests.delete(url_deleteOrder)
    # print(deleteOrder.status_code)
    assert deleteOrder.status_code == 200

    # Delete Order 3
    url_deleteOrder = "https://petstore.swagger.io/v2/store/order/202003"
    deleteOrder = requests.delete(url_deleteOrder)
    # print(deleteOrder.status_code)
    assert deleteOrder.status_code == 200

    # Get Order 1 info
    url_getOrder = "https://petstore.swagger.io/v2/store/order/202001"
    getOrder = requests.get(url_getOrder)
    assert getOrder.status_code == 404
    print(getOrder.text)

    # Get Order 2 info
    url_getOrder = "https://petstore.swagger.io/v2/store/order/202002"
    getOrder = requests.get(url_getOrder)
    assert getOrder.status_code == 404
    print(getOrder.text)

    # Get Order 3 info
    url_getOrder = "https://petstore.swagger.io/v2/store/order/202003"
    getOrder = requests.get(url_getOrder)
    assert getOrder.status_code == 404
    print(getOrder.text)

    # Get Inventory info
    url_getInventory = "https://petstore.swagger.io/v2/store/inventory"
    getInventory = requests.get(url_getInventory)
    assert getInventory.status_code == 200
    print(getInventory.text)















