from django import forms
from django.forms import ModelForm
from .models import Contato, Comentario, Quiz


class ContatoForm(ModelForm):
    class Meta:
        model = Contato
        fields = '__all__'
        exclude = ['aulas']

        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva o seu nome...'}),
            'apelido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva o seu apelido...'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva o número de telefone...'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Escreva o seu email...'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

        # texto a exibir junto à janela de inserção
        labels = {
            'nome': 'Nome',
            'apelido': 'Apelido',
            'telefone': 'Telefone',
            'email': 'Email',
        }

        # texto auxiliar a um determinado campo do formulário
        help_texts = {
            'email': 'nome@endereco.com',
            'telefone': 'ex.: 210 000 000',
        }


class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__'

        op1 = (('Sim', 'Sim'),
               ('Não', 'Não'))

        op2 = (('Pesquisa na web', 'Pesquisa na web'),
               ('Recomendado por um amigo(a)/familiar/colega', 'Recomendado por um amigo(a)/familiar/colega'),
               ('Outro', 'Outro'))

        op3 = (('Sim, tudo', 'Sim, tudo'),
               ('Sim, uma parte', 'Sim, uma parte'),
               ('Não, nada', 'Não, nada'))

        op4 = (('Muito compreensíveis', 'Muito compreensíveis'),
               ('Compreensíveis', 'Compreensíveis'),
               ('Pouco compreensíveis', 'Pouco compreensíveis'),
               ('Incompreensíveis', 'Incompreensíveis'),
               ('Muito incompreensíveis', 'Muito incompreensíveis'))

        op6 = (('Definitivamente sim', 'Definitivamente sim'),
               ('Provavelmente sim', 'Provavelmente sim'),
               ('Não sei', 'Não sei'),
               ('Provavelmente não', 'Provavelmente não'),
               ('Definitivamente não', 'Definitivamente não'))

        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'r1': forms.RadioSelect(choices=op1),
            'r2': forms.CheckboxSelectMultiple(choices=op2),
            'r3': forms.RadioSelect(choices=op3),
            'r4': forms.Select(choices=op4, attrs={'class': 'form-control'}),
            'r5': forms.NumberInput(attrs={'type': 'range', 'step': '1', 'min': '1', 'max': '5'}),
            'r6': forms.RadioSelect(choices=op6),
            'r7': forms.Textarea(attrs={'class': 'form-control', 'rows': '5', 'placeholder': 'Escreva aqui a sua mensagem...'})
        }

        labels = {
            'r1': '1. Foi a primeira vez que visitou o website?',
            'r2': '2. Como conheceu o nosso site?',
            'r3': '3. Encontrou o que precisava?',
            'r4': '4. As informações do site são compreensíveis?',
            'r5': '5. Qual a sua opinião sobre os seguintes aspetos do website? (Numa escala de 1 a 5 em que 1 é Completamente Insatisfatório e 5 é Excelente)',
            'r6': '6. Recomendaria o nosso site a outra pessoa?',
            'r7': '7. Deixe-nos as suas sugestões de melhoria:'
        }


class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = '__all__'

        op3 = (('Sol', 'Sol'),
               ('Si', 'Si'),
               ('Lá', 'Lá'))

        op4 = (('nulo', ''),
               ('Notas tocadas simultaneamente', 'Notas tocadas simultaneamente'),
               ('Conjunto de notas ordernadas pela sua frequência/tom', 'Conjunto de notas ordernadas pela sua frequência/tom'),
               ('Notas tocadas em oitavas', 'Notas tocadas em oitavas'))

        op5 = (('nulo', ''),
               ('Um peça que compõe a viola', 'Um peça que compõe a viola'),
               ('Notas tocadas em terças', 'Notas tocadas em terças'),
               ('Um conjunto harmónico de três ou mais notas', 'Um conjunto harmónico de três ou mais notas'))

        op6 = (('nulo', ''),
               ('Trastes e casas', 'Trastes e casas'),
               ('Separadores e espaços', 'Separadores e espaços'),
               ('Divisores e casas', 'Divisores e casas'))

        op9 = (('nulo', ''),
               ('Mi, Lá, Ré, Sol, Si e Mi', 'Mi, Lá, Ré, Sol, Si e Mi'),
               ('Lá, Dó, Si, Mi, Lá e Sol', 'Lá, Dó, Si, Mi, Lá e Sol'),
               ('Sol, Lá, Si, Mi, Dó e Fá', 'Sol, Lá, Si, Mi, Dó e Fá'))

        op10 = (('Slide', 'Slide'),
                ('Bend', 'Bend'),
                ('Dedilhado', 'Dedilhado'),
                ('Pitch', 'Pitch'))

        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: John Doe'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: nome@email.com'}),
            'e1': forms.NumberInput(attrs={'type': 'range', 'step': '1', 'min': '1', 'max': '6'}),
            'e2': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 6}),
            'e3': forms.RadioSelect(choices=op3),
            'e4': forms.Select(choices=op4, attrs={'class': 'form-control'}),
            'e5': forms.Select(choices=op5, attrs={'class': 'form-control'}),
            'e6': forms.Select(choices=op6, attrs={'class': 'form-control'}),
            'e7': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'e8': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva aqui...'}),
            'e9': forms.Select(choices=op9, attrs={'class': 'form-control'}),
            'e10': forms.CheckboxSelectMultiple(choices=op10)
        }

        help_texts = {
            'nome': 'mandatório',
            'email': 'mandatório',
            'e1': '(de 1 a 6)',
            'e1': '(de 1 a 6)',
            'e8': 'Escreva apenas uma palavra'
        }
