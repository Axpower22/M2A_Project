from django.contrib import admin
from M2A_app import models

admin.site.register(models.UsuarioInfo)
admin.site.register(models.Situacao)
admin.site.register(models.Perfil)
admin.site.register(models.Empresa)
admin.site.register(models.Resposta)
admin.site.register(models.Projeto)
# admin.site.register(models.RespostaQuestionario)


class RespostaQuestionarioInline(admin.StackedInline):
    model = models.RespostaQuestionario


class DiagnosticoAdmin(admin.ModelAdmin):
    inlines = [
        RespostaQuestionarioInline
    ]


class RespostaInline(admin.TabularInline):
    model = models.Resposta


class PerguntaInline(admin.TabularInline):
    model = models.Pergunta.questionario.through


class PerguntaAdmin(admin.ModelAdmin):
    inlines = [
        RespostaInline
    ]


class QuestionarioAdmin(admin.ModelAdmin):
    inlines = [
        PerguntaInline
    ]


admin.site.register(models.Pergunta, PerguntaAdmin)
admin.site.register(models.Questionario, QuestionarioAdmin)
admin.site.register(models.Diagnostico, DiagnosticoAdmin)
