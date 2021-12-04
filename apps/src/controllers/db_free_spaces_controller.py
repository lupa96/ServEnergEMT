from apps.models import Parking, FreeSpaces
from datetime import datetime


def create_parking(parking_name):
    try:
        return Parking.objects.get(parking_name=parking_name)
    except Parking.DoesNotExist:
        return Parking.objects.create(
            parking_name=parking_name,
        )


def create_free_spaces(free_spaces_array):
    for free_spaces in free_spaces_array:
        try:
            FreeSpaces.objects.get(updated_at=free_spaces.updated_at)
        except FreeSpaces.DoesNotExist:
            create_parking(free_spaces.parking.parking_name)
            FreeSpaces.objects.create(
                free_spaces_number=free_spaces.free_spaces_number,
                parking=free_spaces.parking,
                updated_at=free_spaces.updated_at
        )


def get_all_free_spaces():
    free_spaces_list = FreeSpaces.objects.all()
    return free_spaces_list


def export():
    sep_char = ";"
    f = open("export.csv", "x")
    # line = "#datatype measurement,tag,dateTime:RFC3339,double\n"
    # f.write(line)
    # line = "m" + "," + "parking" + "," + "time" + "," + "free spaces" + "\n"
    # f.write(line)
    for free_spaces in get_all_free_spaces():
        time: datetime = free_spaces.updated_at
        time_string = time.isoformat(sep='T')[0: 19] + "Z"
        line = "mem" + sep_char + free_spaces.parking.parking_name + sep_char + time_string + sep_char + str(free_spaces.free_spaces_number) + "\n"
        f.write(line)

    f.close()



