from rest_framework import generics

from .models import *
from .serializers import *

class ItemList(generics.ListCreateAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset =Item.objects.all()
        newsletter = self.request.query_params.get('newsletter')
        if newsletter is not None:
            queryset = queryset.filter(newsitem=newsletter)
        return queryset
    
class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()



class NewsList(generics.ListCreateAPIView):
    serializer_class = NewsletterSerializer
    queryset = Newletter.objects.all()


class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NewsletterSerializer
    queryset = Newletter.objects.all()