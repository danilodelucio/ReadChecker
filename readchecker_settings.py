import nuke
import json
import os


def readChecker_Settings():
    def updateList(options, selected):
        options.remove(selected)
        options.insert(0, selected)
        return options
    
    current_dir = os.path.dirname(__file__)
    if "\\" in current_dir:
        current_dir = current_dir.replace("\\", "/")

    json_file = current_dir + "/config.json"

    # Reading JSON file (config.json)
    with open(json_file, "r") as f:
        data = json.load(f)

    # Defining the UpdateUI options
    updateUI_options = ["SelectedReadNodes", "AllReadNodes", "Off"]
    load_options = ["On", "Off"]
    save_options = ["On", "Off"]

    update_selected = data["update_ui"]
    load_selected = data["on_script_load"]
    save_selected = data["on_script_save"]

    updateList(updateUI_options, update_selected)
    updateList(load_options, load_selected)
    updateList(save_options, save_selected)

    # Creating Custom Panel
    p = nuke.Panel("ReadChecker Settings")
    p.setWidth(350)

    p.addSingleLineInput("Assets Path", data["assets_path"])
    p.addEnumerationPulldown("Update UI", " ".join(updateUI_options))
    p.addEnumerationPulldown("On Script Load", " ".join(load_options))
    p.addEnumerationPulldown("On Script Save", " ".join(save_options))

    p.addButton("Cancel")
    p.addButton("Save as default")
    
    ret = p.show()

    if ret:
        # Saving the custom options as default
        data["assets_path"] = p.value("Assets Path")
        data["update_ui"] = p.value("Update UI")
        data["on_script_load"] = p.value("On Script Load")
        data["on_script_save"] = p.value("On Script Save")

        with open(json_file, "w") as f:
            json.dump(data, f)

        nuke.message("Your ReadChecker settings were saved!\n\nPlease restart Nuke!")