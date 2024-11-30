from django.db import models
#database create "en"
#database yaratma "tr"
#teacher name creation "en
#öğretymen ismi kayıt etme "tr"
class Teacher(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.isim
#lesson creation "en"
#Ders oluşturma "tr"
class Lesson(models.Model):
    
    code=models.CharField(max_length=10)
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.code
#file type creation "en"
#dosya tipi oluşturma "tr"
class Type(models.Model):
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    lesson=models.ForeignKey(Lesson,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    type=models.FileField(upload_to='dosyalar/')

    def __str__(self):
        return self.type