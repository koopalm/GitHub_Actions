import os
def get_file_path(__file__):
    absolute_path = os.path.abspath(__file__)
    print("Full path: " + absolute_path)
    print("Directory Path: " + os.path.dirname(absolute_path))

get_file_path(__file__)