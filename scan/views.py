from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from PIL import Image
import pytesseract
import os

# Configure tesseract path if needed
# pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"  
@csrf_exempt
def extract_prescription(request):
    if request.method == "POST" and request.FILES.get("image"):
        try:
            uploaded_file = request.FILES["image"]
            file_path = default_storage.save(uploaded_file.name, uploaded_file)

            image = Image.open(file_path)

            # Extract text using Tesseract OCR
            extracted_text = pytesseract.image_to_string(image)
            os.remove(file_path)

            return JsonResponse({"extracted_text": extracted_text}, status=200)
        except Exception as e:
            return JsonResponse({"error": f"An error occurred: {str(e)}"}, status=500)
    else:
        return JsonResponse({"error": "Invalid request. Please upload an image."}, status=400)
