import os
import sys
image_path = sys.argv[1]
mask_path = sys.argv[2]
if os.listdir('./data/val_large') != []:
    os.system('rm  ./data/val_large/*')
if os.listdir('./mask') != []:
    os.system('rm ./mask/*')
os.system('mv '+str(image_path)+' ./data/val_larget')
os.system('mv '+str(mask_path)+' ./mask')
os.system('python test.py --snapshot 1000000.pth')
