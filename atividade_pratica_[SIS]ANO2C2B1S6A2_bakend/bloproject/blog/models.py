from django.db import models

# Create your models here.
class Post(models.Model):
    titulo = Models.charField(max_length=100)
    conteudo = models.TextField()
    data_publicaçcao = models.DateTimeField(auto_now_add=True)

    def_str__(self):
        return self.titulo
