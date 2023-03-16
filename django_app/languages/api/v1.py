from rest_framework import generics, serializers, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

from ..models import Phrase


class PhraseSerializer(serializers.ModelSerializer):
    created_at = serializers.ReadOnlyField()
    class Meta:
        model = Phrase
        exclude = ['user']

class PhraseListCreate(generics.ListCreateAPIView):
    serializer_class = PhraseSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self): 
        return Phrase.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PhraseRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PhraseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Phrase.objects.filter(user=user)

        return queryset
