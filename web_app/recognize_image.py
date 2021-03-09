from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

def recognize_image(image):
    # Authenticate
    subscription_key = "YOUR_RESOURCE_KEY" # Add the key for your Computer Vision resource
    endpoint = "YOUR_COMPUTER_VISION_ENDPOINT" # Add your Computer Vision endpoint, looks like https://{resource-name}.cognitiveservices.azure.com/
    computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

    # Call API
    description_result = computervision_client.describe_image_in_stream(image)

    return description_result