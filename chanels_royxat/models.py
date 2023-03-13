from django.db import models

class Category(models.Model):
    name = models.CharField("Bo'lim ", max_length=50)

    createdat = models.DateTimeField("Qo'shilgan vaqti ", auto_now_add=True)
    updatedat = models.DateTimeField("Yangilangan vaqti ", auto_now=True)
    

    def __repr__(self) -> str:
        return f"{self.name}"
    
class Language(models.Model):

    name = models.CharField("tvKanal tili ", max_length=100)

    createdat = models.DateTimeField("Qo'shilgan vaqti ", auto_now_add=True)
    updatedat = models.DateTimeField("Yangilangan vaqti ", auto_now=True)

    def __repr__(self) -> str:
        return  f"{self.name.upper()}"   
    

class Channels(models.Model):
    name = models.CharField("Channel", max_length=50)
    description = models.TextField("Qisqacha info")

    price = models.IntegerField("Narxi")
    channel_number = models.IntegerField("tvKanal raqmi")
    upload_img = models.FileField(upload_to="tvImges/%Y/%m/%d/")


    created_at = models.DateTimeField("Qo'shilgan vaqti", auto_now_add=True)
    updated_at = models.DateTimeField("Yangilangan vaqti", auto_now=True)

    def __str__(self):
        return f"{self.name} | {self.price} so'm"

    

    

class Contact(models.Model):
    
    tvwebsite = models.URLField("tvWebsite ")

    phone_number = models.IntegerField("Aloqa uchun raqam ",)

    tv_email = models.EmailField("Email ",) 
     
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    channels = models.ForeignKey(Channels, on_delete=models.CASCADE)

    
    def __repr__(self) -> str:
        return f"{self.phone_number} | {self.tv_email} "   
    
      


