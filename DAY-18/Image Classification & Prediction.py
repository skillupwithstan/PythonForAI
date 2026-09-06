from fastapi import FastAPI, File, UploadFile
import io
import uvicorn
from PIL import Image
import torch
import torchvision.transforms as transforms
from torchvision.models import mobilenet_v3_small, MobileNet_V3_Small_Weights

# 1. Initialize FastAPI App
app = FastAPI(title="Animal and Fruit Classifier API")

# 2. Load Pre-trained Machine Learning Model (MobileNet V3)
weights = MobileNet_V3_Small_Weights.DEFAULT
model = mobilenet_v3_small(weights=weights)
model.eval()  

# Load the text labels for the 1,000 categories
categories = weights.meta["categories"]

# 3. Standardize Image Preprocessing
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# 4. Filter logic for Broad Categories
def get_broad_type(label: str) -> str:
    label_lower = label.lower()
    
    # Common fruit keywords inside the ImageNet dataset labels
    fruits = ['apple', 'banana', 'orange', 'lemon', 'fig', 'strawberry', 'pineapple', 
              'pomegranate', 'granny smith', 'custard apple', 'banana', 'grape']
    
    if any(fruit in label_lower for fruit in fruits):
        return "Fruit"
        
    return "Animal/Other"

# 5. API Endpoints
@app.get("/")
def home():
    return {"status": "API Online", "task": "Send an image to /predict"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        # Read the uploaded image bytes
        image_bytes = await file.read()
        img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        
        # Preprocess image and add batch dimension -> shape: (1, 3, 224, 224)
        input_tensor = preprocess(img)
        input_batch = input_tensor.unsqueeze(0)
        
        # Run inference
        with torch.no_grad():
            output = model(input_batch)
            
        # --- FOOLPROOF EXTRACTION LAYER ---
        # 1. Remove the batch dimension to make it a flat 1D array of 1,000 items
        logits = output.squeeze(0)
        
        # 2. Convert raw outputs to percentages/probabilities
        probabilities = torch.nn.functional.softmax(logits, dim=0)
        
        # 3. Find the index of the highest score
        top_cat_id = torch.argmax(probabilities).item()
        confidence = float(probabilities[top_cat_id])
        # -----------------------------------
        
        # Extract metadata
        specific_name = categories[top_cat_id]
        broad_category = get_broad_type(specific_name)
        
        return {
            "identified_as": broad_category,
            "specific_object": specific_name,
            "confidence": round(confidence, 4)
        }
        
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
