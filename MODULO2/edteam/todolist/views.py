from rest_framework.views import APIView
from rest_framework.response import Response


class IndexView(APIView):

    def get(self, request):
        context = {
            "status": True,
            "content": "Servidor activo"
        }

        return Response(context)