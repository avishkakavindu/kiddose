from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from kid_dose.ml_models.EmotionDModel import videotester


class EmotionDetectionAPIView(APIView):
    """
     Emotion recognition
    """

    def post(self, request,*args, **kwargs):
        """
            Returns emotional details of image sent in POST request
            :param request:
            :param args:
            :param kwargs:
            :return:
                - string - Predicted feeling('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')
                - list - Coordinated of detected faces
                    The returned array contains information about each face detected in the input image. For each face, the
                    array contains a tuple of four values:

                    1. The x-coordinate of the top-left corner of the face bounding box
                    2. The y-coordinate of the top-left corner of the face bounding box
                    3. The x-coordinate of the bottom-right corner of the face bounding box
                    4. The y-coordinate of the bottom-right corner of the face bounding box
                    So if the function detects N faces in the input image, the returned array will contain N tuples,
                     with each tuple representing the coordinates of a single face.
        """

        image_file = request.FILES.get('image_file')

        if not image_file:
            return Response({'error': 'No image file provided'}, status=status.HTTP_400_BAD_REQUEST)

        # call the emotion detection function with the image file
        predicted_emotion, faces_detected = videotester.predict_emotion(image_file)

        context = {
            'prediction': predicted_emotion,
            'faces_detected': faces_detected
        }

        return Response(context, status=status.HTTP_200_OK)
