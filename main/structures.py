class category(object):
    id = 0
    code = 0
    name = ""


class manufacturer(object):
    id = 0
    name = ""
    country = ""


class storage_place(object):
    building = 0
    room = 0


class condition(object):
    id = 0
    works = False
    location =""


class description(object):
    id = 0
    name = ""
    brand = ""
    model = ""
    manufacturer = manufacturer()
    category = category()


class report(object):
    id = 0
    description = description()
    serial_number = 0
    inventory_number = 0
    manufacture_date = 0
    storage_place = storage_place()
    condition = condition()