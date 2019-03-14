import cv2
import matplotlib.pyplot as plt
import os
import tqdm



SAVE_DIR = 'D:PythonData/ParksCanada/'
speciesdir = 'D:PythonData/ParksCanada/WildlifeImages/'
naturedir = 'D:PythonData/ParksCanada/WildlifeImages/Nature/'


# species = 'Bighorn Sheep'
# species = 'BlackBear'
# species = 'Canada Goose'
# species = 'Cougar'
# species = 'Coyote'
# species = 'Elk'
# species = 'Golden-mantled Ground Squirrel'
# species = 'Grizzly'
# species = 'Lynx'
# species = 'Marmot'
# species = 'Marten'
# species = 'Moose'
# species = 'Mountain Goat'
# species = 'Mule Deer'
# species = 'Other'
# species = 'Porcupine'
# species = 'Red Fox'
# species = 'Red Squirrel'
# species = 'Snowshoe Hare'
# species = 'Striped Skunk'
# species = 'Unknown'
# species = 'Unknown Bear'
# species = 'Unknown Canid'
# species = 'Unknown Deer'
# species = 'Unknown Mustelid'
# species = 'Unknown Ungulate'
# species = 'White-tailed Deer'
# species = 'Wolf'
# species = 'Wolverine'



if not os.path.exists(SAVE_DIR + '{}list.txt'.format(species)):
    imagelist = []
    with open(SAVE_DIR + '{}list.txt'.format(species), 'w') as f:
        f.write('')
    f.close()
else:
    with open(SAVE_DIR + '{}list.txt'.format(species), 'r') as f:
        imagelist = f.read().splitlines()
    f.close()


plt.ion()
plt.show()
fig = plt.figure(figsize=(23, 17))


def sortimages():

    for imagefile in tqdm.tqdm(os.listdir(speciesdir + species)):
        if imagefile in imagelist: pass
        else:

            im = cv2.imread(speciesdir + species + '/' + imagefile)
            plt.imshow(cv2.cvtColor(im, cv2.COLOR_BGR2RGB), interpolation='nearest', aspect='auto')
            plt.pause(0.00001)
            ans = input('Is there a {} in this image?  {}'.format(species, imagefile))
            plt.show()

            if ans == 'n':
                try:
                    os.rename(speciesdir + species + '/' + imagefile, naturedir + imagefile)
                except:
                    print('File Exists')
            elif ans == 'u':
                del imagelist[-3:]
                with open(SAVE_DIR + '{}list.txt'.format(species), 'w') as f:
                    for item in imagelist:
                        f.write("{}\n".format(item))
                sortimages()
                return
            else:
                imagelist.append(imagefile)
                with open(SAVE_DIR + '{}list.txt'.format(species), 'w') as f:
                    for item in imagelist:
                        f.write("{}\n".format(item))
                pass
            plt.clf()

sortimages()














