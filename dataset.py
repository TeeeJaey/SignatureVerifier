
import os

os.getcwd()
collection = "DataSet"
training_folder = "Data\Training"
testing_folder = "Data\Testing"

images=0
classes=0
f = open("datasetCount.txt", "w")
print("     Dataset Count\n")
f.write("     Dataset Count\n\n")
f.close()
f = open("datasetCount.txt", "a")

for folder in os.listdir(collection):
    classes+=1
    j=0
    for file in os.listdir(collection+"/"+folder):
        j+=1
        images+=1
        #os.rename("DataSet/"+folder+"/"+file,"DataSet/"+folder+"/"+folder+"_"+str(j)+".png")
    print(folder +"\t"+ str(j)+ " images")
    f.write(folder +"\t"+ str(j)+ " images\n")

authors = int(classes / 2)
print ("\n"+str(authors)+" Authors, "+str(classes)+" Classes, "+str(images)+" Images")
f.write("\n"+str(authors)+" Authors, "+str(classes)+" Classes, "+str(images)+" Images")

training_files = 0
for file in os.listdir(training_folder):
    training_files += 1


testing_files = 0
for file in os.listdir(testing_folder):
    testing_files += 1
print ("\n"+str(training_files)+" Training images, "+str(testing_files)+" Testing images")
f.write("\n"+str(training_files)+" Training images, "+str(testing_files)+" Testing images")
f.close()
