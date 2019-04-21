1. Put image for predict in data/val_large and mask in mask/
2. run python test.py --snapshot 1000000.pth to get result.jpg as output

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

