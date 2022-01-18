import os

source_folder = r'C:\storeFolder' + '\\'
target_folder = r'C:\targetFolder' + '\\'


# for path, dir, files in os.walk(source_folder):

#     print(path)
#     print(files)

# print(source_folder)


def move_files(sourceFolder, targetFolder):
    try:
        for path, dir, files in os.walk(sourceFolder):
            if files:
                for file in files:
                    if not os.path.isfile(targetFolder + file):
                        os.rename(path + '\\' + file, targetFolder + file)
        print('All files moved')
    except Exception as e:
        print(e)

move_files(source_folder, target_folder)

