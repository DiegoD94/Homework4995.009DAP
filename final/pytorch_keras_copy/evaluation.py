import torch
from torchvision.utils import make_grid
from torchvision.utils import save_image

from util.image import unnormalize


def evaluate(model, dataset, device, filename):
    image, mask, gt = zip(*[dataset[i] for i in range(1)])
    image = torch.stack(image)
    mask = torch.stack(mask)
    gt = torch.stack(gt)
    with torch.no_grad():
        output, _ = model(image.to(device), mask.to(device))
    output = output.to(torch.device('cpu'))
    output_comp = mask * image + (1 - mask) * output

#    grid = make_grid(
#        torch.cat((unnormalize(image), unnormalize(output),
           
    save_image(unnormalize(output), filename)
