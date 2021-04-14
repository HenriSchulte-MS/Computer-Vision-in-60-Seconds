# Computer-Vision-in-60-Seconds
This Flask app uses the Azure Cognitive Services Computer Vision API to get AI-generated descriptions for user-uploaded images. You can find it running at http://computer-vision-demo.azurewebsites.net/.

Use "flask run" to run the app locally on your machine at localhost:5000.

![Example of the web app](/img/web_app.png)

Note: The Computer Vision API currently only supports images up to 4MB. There are no checks in place to prevent users from uploading incompatible images (or other files).
