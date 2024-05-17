from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Contact
from .serializers import ContactSerializer
from django.core.mail import send_mail
from django.conf import settings

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all().order_by('id') 
    serializer_class = ContactSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        inquiry = serializer.instance
        subject = 'Yangi Murojat!'
        message = f"Yangi murojat: {inquiry.firstname}\nEmail: {inquiry.email}\nMessage: {inquiry.message}"
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = [inquiry.email]

        try:
            send_mail(subject, message, from_email, to_email)
            headers = self.get_success_headers(serializer.data)
            response_data = {"message": "Your message has been sent successfully"}
            return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)
        except Exception as e:
            return Response({"error": "Failed to send email"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
