import pathlib
import sys

_MODULEPATH = pathlib.Path(__file__).parent



source_dict = {"Benson":"Coolest","Phuong":"Cooler","Kiri":"Cool"}

other_dict = {}
other_dict["Benson"] = source_dict["Benson"]


source_dict["Benson"]="Awesome!"

print(source_dict)
print(other_dict)