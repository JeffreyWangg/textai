import os
import json
import pandas as pd
rootdir = "/Users/jwang/Documents/ArknightsStoryJson-20230513/en_US/gamedata/story/obt/main"

def cleanData(data):
    lines = []

    for i in range(len(data["storyList"])):
        el = data["storyList"][i]
        # print(el["prop"])
        if(el["prop"] == "name"):
            lines.append(data["storyList"][i])
    
    data["storyList"] = lines

def returnLinesForName(name, data):
    lines = data["storyList"]
    list = []

    for i in range(len(lines)):
        el = lines[i]
        if('name' in el["attributes"] and el["attributes"]["name"] == name):
            first = lines[i-1]["attributes"]["content"] if i > 0 else ""
            list.append({
                "statement": first,
                "reply": el["attributes"]["content"],
                "prediction" : "C: " + first + "\n A: " + el["attributes"]["content"]
                })

    return list



def main():
    amiyaLines = []

    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            file_path = os.path.join(subdir, file)
            print(os.path.join(subdir, file))
            split = os.path.splitext(file)
            if(split[1] == ".json"):
                open_file = open(file_path)
                data = json.load(open_file)

                # print(len(data["storyList"]))

                cleanData(data)
                batch = returnLinesForName("Amiya", data)
                # print(batch)

                amiyaLines.extend(batch)
    
    df = pd.DataFrame.from_records(amiyaLines)
    print(amiyaLines)
    amiya_json = json.dumps(amiyaLines)
    with open("storylines.json", "w") as outfile:
        outfile.write(amiya_json)
    

print(main())






    

        

