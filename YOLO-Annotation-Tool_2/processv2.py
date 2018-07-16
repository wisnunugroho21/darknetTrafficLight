import glob, os

# Current directory
current_dir = os.path.dirname(os.path.abspath(__file__)) + '/Multi-Image-Train'
print(current_dir)

# Create and/or truncate train.txt and test.txt
file_train = open('train.txt', 'w')  

# Populate train.txt
for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.jpg")):  
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    file_train.write(current_dir + "/" + title + '.jpg' + "\n")
