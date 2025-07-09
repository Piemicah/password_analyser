from rest_framework.views import APIView
from rest_framework.response import Response
import joblib
from .features import extract_features
import os

file_path = os.path.abspath("password_classifier.joblib")


class PasswordView(APIView):

    def post(self, request):
        password = request.data["password"]
        feat = extract_features(password)
        model = joblib.load(file_path)
        classification = model.predict(feat)[0]
        return Response({"type": classification})
