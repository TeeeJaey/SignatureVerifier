
import os
import shutil
import inspect
import PySimpleGUI as sg

def getData():
    try:
        sg.ChangeLookAndFeel('SandyBeach')

        os.getcwd()
        collection = "DataSet"
        training_folder = "Data/Training"
        testing_folder = "Data/Testing"
        sg.ChangeLookAndFeel('SandyBeach')


        images=0
        classes=0
        f = open("Data/Analysis.txt", "w")
        print("   Dataset Analysis\n")
        f.write("   Dataset Analysis\n\n")
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
                exists = os.path.isfile(collection+"/"+folder+"/"+folder+"_"+str(j)+".png")
                if not exists:
                    os.rename(collection+"/" + folder + "/" + file, collection+"/" + folder + "/" + folder + "_" + str(j) + ".png")

                dataFolder = training_folder if (j <= (80*total/100)) else testing_folder
                dataexists = os.path.isfile(dataFolder + "/" + folder + "_" + str(j) + ".png")
                if not dataexists:
                    shutil.copy(collection+"/" + folder + "/" + folder + "_" + str(j) + ".png", dataFolder)


                if not sg.OneLineProgressMeter('Testing Progress', images, 1272, 'key', orientation='h'):
                    print("Exiting Dataest...")
                    break

            tab = "\t " if(total<10) else "\t"
            print(folder + tab + str(total)+ " images")
            f.write(folder + tab + str(total)+ " images\n")


        authors = int(classes / 2)
        imgAnalysis = str(authors)+" Authors, "+str(images)+" Images"
        print ("\n"+imgAnalysis)
        f.write("\n"+imgAnalysis)

        training_files = 0
        for file in os.listdir(training_folder):
            training_files += 1
        training_files_percent = round((100*training_files/images),2)

        testing_files = 0
        for file in os.listdir(testing_folder):
            testing_files += 1
        testing_files_percent = round((100*testing_files/images),2)

        trainAnalysis = str(training_files)+" Training images ("+str(training_files_percent)+"%)"
        testAnalysis = str(testing_files) + " Testing images (" + str(testing_files_percent) + "%)"

        print ("\n"+trainAnalysis)
        print ("\n"+testAnalysis)
        f.write("\n"+trainAnalysis)
        f.write("\n"+testAnalysis)

        sg.Popup('DataSet Analysis..',imgAnalysis,trainAnalysis,testAnalysis)

        f.close()


    except Exception as error:
        print("An exception in " + inspect.stack()[0][3])
        print("Error: "+ str(error))
        sg.Popup('Exception..','thrown in ',str(inspect.stack()[0][3]),str(error))

    finally:
        return