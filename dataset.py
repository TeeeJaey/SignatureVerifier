
import os
import shutil
import inspect

try:
    os.getcwd()
    collection = "DataSet"
    training_folder = "Data/Training"
    testing_folder = "Data/Testing"

    images=0
    classes=0
    f = open("Data/Analysis.txt", "w")
    print("     Dataset Count\n")
    f.write("     Dataset Count\n\n")
    f.close()
    f = open("Data/Analysis.txt", "a")

    for folder in os.listdir(collection):
        classes+=1
        j=0
        list = os.listdir(collection+"/"+folder)
        total = len(list)
        for file in os.listdir(collection+"/"+folder):
            j+=1
            images+=1
            exists = os.path.isfile("DataSet/"+folder+"/"+folder+"_"+str(j)+".png")
            if not exists:
                os.rename("DataSet/" + folder + "/" + file, "DataSet/" + folder + "/" + folder + "_" + str(j) + ".png")

            dataFolder = training_folder if (j < (4*total/5)) else testing_folder
            dataexists = os.path.isfile(dataFolder + "/" + folder + "_" + str(j) + ".png")
            if not dataexists:
                shutil.copy("DataSet/" + folder + "/" + folder + "_" + str(j) + ".png", dataFolder)

        tab = "\t " if(total<10) else "\t"
        print(folder + tab + str(total)+ " images")
        f.write(folder + tab + str(total)+ " images\n")


    authors = int(classes / 2)
    print ("\n"+str(authors)+" Authors, "+str(classes)+" Classes, "+str(images)+" Images")
    f.write("\n"+str(authors)+" Authors, "+str(classes)+" Classes, "+str(images)+" Images")

    training_files = 0
    for file in os.listdir(training_folder):
        training_files += 1
    training_files_percent = round((100*training_files/images),2)

    testing_files = 0
    for file in os.listdir(testing_folder):
        testing_files += 1
    testing_files_percent = round((100*testing_files/images),2)

    print ("\n"+str(training_files)+" Training images ("+str(training_files_percent)+"%)")
    print ("\n"+str(testing_files)+" Testing images ("+str(testing_files_percent)+"%)")
    f.write("\n"+str(training_files)+" Training images ("+str(training_files_percent)+"%)")
    f.write("\n"+str(testing_files)+" Testing images ("+str(testing_files_percent)+"%)")


    f.close()

except Exception as error:
    print ("An exception was thrown in ",inspect.stack()[0][3])
    print ("Error: ",str(error))