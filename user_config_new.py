import dearpygui.dearpygui as dpg

dpg.create_context()

def sensor_selection(sender, value, user_data):
    sensor_clicked = [False, False, False, False, False, False, False, False, False, False]
    
    n = 0
    while n < 10:
        sensor_clicked[n] = dpg.get_value(sensor_tags[n])
        n += 1

    indices = [t for t in range(len(sensor_clicked)) if sensor_clicked[t] == True]
    sensors_selected = []

    p = 0
    while p < len(indices):
        sensors_selected.append(sensor_labels[indices[p]])
        p += 1

    dpg.set_value(user_data,f"You have selected the following sensors: " + ", ".join(sensors_selected))

def clear_sensors(sender, value, user_data):
    sensor_false = [False, False, False, False, False, False, False, False, False, False]
    
    h = 0
    while h < 10:
        dpg.set_value(user_data[h], sensor_false[h])
        h += 1

def all_sensors(sender, value, user_data):
    sensor_true = [True, True, True, True, True, True, True, True, True, True]

    m = 0
    while m < 10:
        dpg.set_value(user_data[m], sensor_true[m])
        m += 1

def gesture_selection(sender, value, user_data):
    gesture_clicked = [False, False, False, False, False, False, False, False]
    
    k = 0
    while k < 8:
        gesture_clicked[k] = dpg.get_value(gesture_tags[k])
        k += 1

    indices = [t for t in range(len(gesture_clicked)) if gesture_clicked[t] == True]
    gestures_selected = []

    p = 0
    while p < len(indices):
        gestures_selected.append(gesture_labels[indices[p]])
        p += 1

    dpg.set_value(user_data,f"You have selected the following gestures: " + ", ".join(gestures_selected))

def clear_gestures(sender, value, user_data):
    gesture_false = [False, False, False, False, False, False, False, False]
    
    h = 0
    while h < 8:
        dpg.set_value(user_data[h], gesture_false[h])
        h += 1

def all_gestures(sender, value, user_data):
    gesture_true = [True, True, True, True, True, True, True, True]

    m = 0
    while m < 8:
        dpg.set_value(user_data[m], gesture_true[m])
        m += 1

def forward():
    if dpg.does_item_exist(sensor_menu[0]) == True:
        for x in range(len(sensor_labels)):
            dpg.delete_item(sensor_menu[x])

    if dpg.does_item_exist(gesture_menu[0]) == True:
        for y in range(len(gesture_labels)):
            dpg.delete_item(gesture_menu[y])

with dpg.window(tag = "Primary Window"):
    dpg.add_text("Welcome to the user configuration window. Please follow the directions below to set up. ")

    # Sensor selection
    dpg.add_text("Select all sensors to read:")
    sensor_labels = ["FSR 1", "FSR 2", "FSR 3", "FSR 4", "FSR 5", "FSR 6", "FSR 7", "FSR 8", "Accelerometer (IMU)", "Gyroscope (IMU)"]
    sensor_tags = ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "accel", "gyro"]

    sensor_menu = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    i = 1
    
    while i < 9:
        sensor_menu[i - 1] = dpg.add_menu_item(tag = "F" + str(i), label = "FSR " + str(i), check = True)
        i += 1
    sensor_menu[8] = dpg.add_menu_item(tag = "accel", label = "Accelerometer (IMU)", check = True)
    sensor_menu[9] = dpg.add_menu_item(tag = "gyro", label = "Gyroscope (IMU)", check = True)
    
    text_sensor = dpg.add_text("You have selected the following sensors: ")

    with dpg.group(horizontal = True):
        dpg.add_button(label = "Confirm selection", callback = sensor_selection, user_data = text_sensor)
        dpg.add_button(label = "Clear selection", callback = clear_sensors, user_data = sensor_menu)
        dpg.add_button(label = "Select all", callback = all_sensors, user_data = sensor_menu)
    
    dpg.add_text(" ")

    # Gesture selection
    dpg.add_text("Select all gestures to train:")
    gesture_labels = ["No Motion","Chuck Grip","Hand Open","Hand Closed","Thumbs Down","Thumbs Up","Wrist Extension","Wrist Flexion"]
    gesture_tags = ["G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8"]

    gesture_menu = [0, 0, 0, 0, 0, 0, 0, 0]
    q = 1
    
    while q < 9:
        gesture_menu[q - 1] = dpg.add_menu_item(tag = "G" + str(q), label = gesture_labels[q - 1], check = True)
        q += 1
    
    text_gesture = dpg.add_text("You have selected the following gestures: ")

    with dpg.group(horizontal = True):
        dpg.add_button(label = "Confirm selection", callback = gesture_selection, user_data = text_gesture)
        dpg.add_button(label = "Clear selection", callback = clear_gestures, user_data = gesture_menu)
        dpg.add_button(label = "Select all", callback = all_gestures, user_data = gesture_menu)
    
    dpg.add_button(tag = "Forward", arrow = True, direction = 1, callback = forward)

print(dpg.does_item_exist(sensor_menu[0]))

dpg.create_viewport(title = "User Configuration", width = 650, height = 550)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()