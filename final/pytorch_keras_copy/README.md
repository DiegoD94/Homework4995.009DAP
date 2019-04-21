1. Download pretrained model [here](https://drive.google.com/open?id=1SYjJ-Vlu2cpAlgBG5FiJueN9W4lf48w8), put it at ./
2. Put image for predict in data/val_large and mask in mask/
3. run python test.py --snapshot 1000000.pth to get result.jpg as output

# EXAMPLE
run 
```
python script.py IMAGE_PATH MASK_PATH 
```
to predict specific IMAGE and MASK

For example, try
```
python script.py image_example/Places365_val_00000102.jpg mask_example/000003.jpg
```

