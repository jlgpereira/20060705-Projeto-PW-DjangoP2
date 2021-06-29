from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.index_page_view, name='index'),
    path('login/', views.login_page_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path("pesquisa", views.pesquisa_view_page, name="pesquisa"),
    path('introducao', views.introducao_page_view, name='introducao'),
    path('nprinc', views.nprinc_page_view, name='nprinc'),
    path('exercicios', views.exercicios_page_view, name='exercicios'),
    path('aboutus', views.aboutus_page_view, name='aboutus'),
    path('inserir_contato', views.inserir_contato_page_view, name='inserir_contato'),
    path('contatos', views.contatos_page_view, name='contatos'),
    path('editar_contato/<int:contato_id>', views.editar_contato_page_view, name='editar_contato'),
    path('apagar_contato/<int:contato_id>', views.apagar_contato_view, name='apagar_contato'),
    path('comentarios', views.comentarios_page_view, name='comentarios'),
    path('relatorios', views.relatorios_page_view, name='relatorios'),
    path('quiz', views.quiz_page_view, name='quiz'),
    path('aulas', views.aulas_page_view, name='aulas'),
    path('aulas_seccao/<int:num>', views.aulas_section_view, name="aulas_seccao"),
    path('aula/<int:aula_id>', views.aula_page_view, name='aula'),
    path('adicionar_contato/<int:aula_id>', views.adicionar_aluno_view, name='adicionar_contato'),
    path('remover_contato/<int:aula_id>,<int:contato_id>', views.remover_aluno_view, name='remover_contato'),
]
