# -----------------------------------------------------------------------------------
#  ReadChecker - Versioning validation tool for Read nodes in Nuke
#  Version: v01.1
#  Author: Danilo de Lucio
#  Website: www.danilodelucio.com
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
#  [Summary]
#  This tool checks the versions of your Read nodes, coloring them to:
#
# - GREEN: if they are updated;
# - ORANGE: if they are out of date;
# - RED: if they don't exist;
# - BLUE: if they come from your Assets Library;
#
# For more information please check out the User Guide.
# -----------------------------------------------------------------------------------

import nuke
import os
import re
import sys
import json
import traceback
from readchecker_settings import readChecker_Settings


current_dir = os.path.dirname(__file__)
if "\\" in current_dir:
    current_dir = current_dir.replace("\\", "/")
json_file = current_dir + "/config.json"

with open(json_file, "r") as f:
    data = json.load(f)

# Reading JSON file (config.json)
assets_path = data["assets_path"]
update_ui = data["update_ui"]
on_script_load = data["on_script_load"]
on_script_save = data["on_script_save"]


def tileColor(r,g,b):
    # Converting RGB to HEX
    hex_color = r << 24 | g << 16 | b << 8 | 1
    return hex_color


def colorNode(node, color_name):
    if color_name == "GREEN":
        node["tile_color"].setValue(tileColor(25, 255, 25))
        
    elif color_name == "ORANGE":
        node["tile_color"].setValue(tileColor(255, 100, 0))
        
    elif color_name == "RED":
        node["tile_color"].setValue(tileColor(255, 0, 0))

    elif color_name == "ASSETS":
        node["tile_color"].setValue(tileColor(25, 25, 255))   
         
    elif color_name == "DEFAULT":
        node["tile_color"].setValue(tileColor(255, 255, 255))  
         
    return color_name


def debugMsg(msg):
    # Change here to True/False, to enable/disable the print statements for debugging.
    # It's highly recommended to keep it disabled, otherwise, your Nuke will slow down.
    # You can use this function in an empty script with a few nodes only;
    enable = False
    if enable:
        print(msg)
    return


def search_pattern(search_list):
    regex_pattern = re.compile(r"[vV][0-9][0-9]?[0-9]?")
    matched_items = []
    index_item = []
    version_id = []

    for item in search_list:
        if regex_pattern.search(item):
            matched_items.append(item)
            index_item.append(search_list.index(item))
            version_id = re.compile(regex_pattern).findall(item)

    if len(version_id) > 0:
        version_id = version_id[0]

    return matched_items, index_item, regex_pattern, version_id


def readChecker(node):
    try:
        printDiv = 200

        # Getting the file path
        path_node = nuke.filename(node, nuke.REPLACE)
        read_name = node.name()
        debugMsg(read_name)

        path_node_split = path_node.split("/")
        debugMsg(path_node_split)

        if len(path_node_split) > 2 and os.path.isfile(path_node):
            if not assets_path in path_node:
                debugMsg("- Python version: " + sys.version[:6])

                file_name = path_node_split[-1]
                debugMsg("- File name: " + file_name)

                file_ext = path_node_split[-1][-3:]
                debugMsg("- File extension: " + file_ext)

                current_folder = "/".join(path_node_split[:-1])
                debugMsg("- Current folder path: " + current_folder)
                debugMsg("")

                folder_name = path_node_split[-2]
                debugMsg("- Folder name: " + folder_name)

                matched_items, index_item, regex_pattern, version_id = search_pattern(path_node_split)
                debugMsg("- Matched items: " + str(matched_items))
                debugMsg("- Index item: " + str(index_item))
                debugMsg("- Version ID: " + str(version_id) + " / Lenght: " + str(len(version_id)))
                debugMsg("")

                ##########################################################################################
                version_list = []
                version_folder_name = ""
                # If it has only 1 versioning, validate the file's current folder
                if len(matched_items) == 1:
                    debugMsg("[1 VERSIONING ID HAS BEEN FOUND!]")
                    debugMsg("Listing all files to compare...")

                    debugMsg("")
                    # If it has versioning in the file name
                    if regex_pattern.search(file_name):
                        for file in os.listdir(current_folder):
                            if file.endswith(file_ext):
                                if regex_pattern.search(file):
                                    file_name_pattern = re.compile(regex_pattern).finditer(file_name)
                                    for item in file_name_pattern:
                                        file_name_pattern = item.group(0)
                                        file_name_split = file_name.split(file_name_pattern)

                                        file_pattern = re.compile(regex_pattern).finditer(file)
                                        for item in file_pattern:
                                            file_pattern = item.group(0)
                                            search_name = file_name_split[0] + file_pattern + file_name_split[1]

                                            if search_name in file:
                                                debugMsg("__ " + file)
                                                version_list.append(file)
                    
                    # If it has versioning in the previous folder
                    elif regex_pattern.search(current_folder):
                        version_folder = current_folder.split("/")
                        version_folder = "/".join(version_folder[:-1])

                        for file in os.listdir(version_folder):
                            if len(file) == len(folder_name):
                                if re.compile(regex_pattern).search(file):
                                    version_list.append(file)
                                    debugMsg("__ " + file)

                # If it has 2 or more versioning, always validate the second last folder that contains the version
                elif len(matched_items) >= 2:
                    debugMsg("[2 OR MORE VERSIONING IDs WERE FOUND!]")
                    debugMsg("Listing all files to compare...")

                    version_folder = "/".join(path_node_split[:index_item[-2]])
                    debugMsg("- Version folder path: " + version_folder)
                    version_folder_name = path_node_split[index_item[-2]]
                    debugMsg("- Version folder name: " + version_folder_name)
                    debugMsg("")

                    for file in os.listdir(version_folder):
                        if len(version_folder_name) > len(version_id):
                            folder_name_pattern = re.compile(regex_pattern).finditer(version_folder_name)
                            for item in folder_name_pattern:
                                folder_name_pattern = item.group(0)
                                folder_name_split = version_folder_name.split(folder_name_pattern)

                                file_pattern = re.compile(regex_pattern).finditer(file)
                                for item in file_pattern:
                                    file_pattern = item.group(0)
                                    search_name = folder_name_split[0] + file_pattern + folder_name_split[1]
                                    if search_name in file:
                                        debugMsg("__ " + file)
                                        version_list.append(file)

                        else:
                            if len(file) == len(version_folder_name):
                                if re.compile(regex_pattern).search(file):
                                    version_list.append(file)
                                    debugMsg("__ " + file)

                # If no versioning is found, don't do anything
                elif len(matched_items) == 0:
                    debugMsg("[NO VERSIONING ID FOUND!]")

                ##########################################################################################
                # Figuring out the higher version
                debugMsg("")
                if len(version_list) == 0:
                    higher_version = None
                else:
                    higher_version = max(version_list)
                debugMsg("- Higher version: " + str(higher_version))

                ##########################################################################################
                # If the file is the last version, apply Green color
                if version_folder_name == higher_version or folder_name == higher_version or file_name == higher_version:
                    colorNode(node, "GREEN")

                # If the file is out of date, apply Orange color
                elif version_folder_name < higher_version or folder_name < higher_version or file_name < higher_version:
                    colorNode(node, "ORANGE")

                # If the file path doesn't contain a versioning ID, don't do anything
                elif higher_version == None:
                    colorNode(node, "DEFAULT")
                    debugMsg("-" * printDiv)  

            # If the file is from the Assets Library, apply Blue color
            else:        
                colorNode(node, "ASSETS")
                debugMsg("[FILE FROM ASSETS LIBRARY]")
                debugMsg("-" * printDiv)

        else:
            colorNode(node, "DEFAULT")
            debugMsg("-" * printDiv)
    
    except:
        print(traceback.format_exc())
    
    finally:
        pass
        

# Setting Callbacks Functions
def callback_selectedNodes():
    for node in nuke.selectedNodes("Read"):
        readChecker(node)

def callback_allNodes():
    for node in nuke.allNodes("Read"):
        readChecker(node)

def callback_allNodes_withError():
    for node in nuke.allNodes("Read"):
        if node.error():
            colorNode(node, "RED")
            debugMsg("[THIS FILE DOESN'T EXIST!]")
        else:
            readChecker(node)

def button_allNodes():
    for node in nuke.allNodes("Read"):
        if node.error():
            colorNode(node, "RED")
            debugMsg("[THIS FILE DOESN'T EXIST!]")
        else:
            readChecker(node)
        
    nuke.message("[ReadChecker]:\n\nAll Read nodes were successfully validated!")


# Defining Callbacks from the config.json file
if update_ui == "SelectedReadNodes":
    nuke.addUpdateUI(callback_selectedNodes)
elif update_ui == "AllReadNodes":
    nuke.addUpdateUI(callback_allNodes)

if on_script_load == "On":
    nuke.addOnScriptLoad(callback_allNodes_withError)

if on_script_save == "On":
    nuke.addOnScriptSave(callback_allNodes_withError)


nuke.menu('Nuke').addCommand('ReadChecker/Validate now', button_allNodes, "ctrl+shift+r", icon="validate_icon.png")
nuke.menu('Nuke').addCommand('ReadChecker/Settings', readChecker_Settings, icon="settings_icon.png")
nuke.menu('Nuke').addCommand('ReadChecker', icon="ReadChecker_Icon.png")