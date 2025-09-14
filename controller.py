from data_access import add_car, remove_car, get_all_cars

def enter_car(name, model, color, plate):
    if not (name and model and color and plate):
        return False, "تمام فیلدها باید پر شود!"
    success = add_car(name, model, color, plate)
    if success:
        return True, "ماشین با موفقیت وارد شد!"
    else:
        return False, "خطا: شماره پلاک تکراری است!"

def exit_car(plate):
    if not plate:
        return False, "شماره پلاک را وارد کنید!"
    remove_car(plate)
    return True, "ماشین خارج شد!"

def list_cars():
    return get_all_cars()
