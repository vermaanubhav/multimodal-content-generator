# utils/image_utils.py

from PIL import Image
import torchvision.transforms as transforms
import torch
import torchvision.models as models

def get_image_description(image_path):
    model = models.resnet50(pretrained=True)
    model.eval()

    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )
    ])

    image = Image.open(image_path).convert("RGB")
    input_tensor = preprocess(image).unsqueeze(0)  # shape: [1, 3, 224, 224]

    with torch.no_grad():
        output = model(input_tensor)
    
    # Get human-readable labels
    from torchvision.models import ResNet50_Weights
    weights = ResNet50_Weights.DEFAULT
    categories = weights.meta["categories"]
    top_cat = torch.argmax(output).item()
    return categories[top_cat]
