from django.db import models


# Create your models here.
class Comentario(models.Model):

    r1 = models.CharField(default=True, max_length=3)
    r2 = models.CharField(default=True, max_length=75)
    r3 = models.CharField(default=True, max_length=15)
    r4 = models.CharField(default=True, max_length=22)
    r5 = models.IntegerField(default=1)
    r6 = models.CharField(default=True, max_length=19)
    r7 = models.TextField(null=True, max_length=4000)

    def __str__(self):
        return f"Comentario {self.id}"


class Quiz(models.Model):

    r1 = models.IntegerField(default=1)
    r2 = models.IntegerField(default=1)
    r3 = models.CharField(default=True, max_length=3)
    r4 = models.CharField(default=True, max_length=52)
    r5 = models.CharField(default=True, max_length=43)
    r6 = models.CharField(default=True, max_length=21)
    r7 = models.DateField()
    r8 = models.CharField(null=True, max_length=9)
    r9 = models.CharField(default=True, max_length=24)
    r10 = models.CharField(null=True, max_length=39)

    class Meta:
        verbose_name = "Quiz"
        verbose_name_plural = "Quizzes"

    # Função utilizada para forçar lower case ao texto da reposta 8
    def save(self, force_insert=False, force_update=False):
        self.r8 = self.r8.lower()
        super(Quiz, self).save(force_insert, force_update)

    def __str__(self):
        return f"Quiz {self.id}"


class Sala(models.Model):
    codigo = models.CharField(max_length=3)
    designacao = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.designacao}"


class Aula(models.Model):
    titulo = models.CharField(max_length=64)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE, related_name="Salas")
    duracao = models.IntegerField()

    def __str__(self):
        return f"{self.titulo} ({self.sala})"


class Contato(models.Model):
    nome = models.CharField(max_length=64)
    apelido = models.CharField(max_length=64)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    data_nascimento = models.DateField()
    aulas = models.ManyToManyField(Aula, blank=True, related_name="Contatos")
    criado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} {self.apelido}"
