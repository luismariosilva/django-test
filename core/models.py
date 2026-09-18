from django.db import models

# Create your models here.

class Livro(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=100)
    ano_publicacao = models.IntegerField()
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return f'Título: {self.titulo}, Autor: {self.autor}, Ano de publicação: {self.ano_publicacao}'


class Autor(models.Model):
    nome = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    biografia = models.TextField()

    def __str__(self):
        return f'Nome: {self.nome}, Nacionalidade: {self.nacionalidade}, Data de nascimento: {self.data_nascimento}'
    

