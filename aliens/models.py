from django.db               import models
from datetime                import date
from django.utils            import timezone
from django.utils.functional import cached_property

# A ESCOLHA DE CRIAR UM MODELO SEPARA PARA OS ESTADOS FOI UMA TENTATIVA DE DEIXAR O BANCO DE DADOS NORMALIZADO SEGUNDO A 3NF. 
#
#
#
#           MODELO STATE
#    CAMPOS:
#    INITIALS -> TIPO CHAR, MAX 2 CARACTERES, NOT NULL  -> SIGLA DO ESTADO
#    NAME     -> TIPO CHAR, MAX 50 CARACTERES, NOT NULL -> NOME DO ESTADO ONDE OCORREU A APARIÇÃO
#    COUNT    -> TIPO INTEIRO, VALOR PADRAO = 0         -> QUANTIDADE DE APARIÇÕES OCORRIDAS NESSE ESTADO
#
class State(models.Model):
    initials = models.CharField('Sigla', max_length=2, blank = False)
    name     = models.CharField('Estado', max_length=50, blank = False)
    count    = models.IntegerField('Total de Eventos', default=0)

    def __str__(self):
        return self.name



    class Meta:
        verbose_name        = 'Estado'
        verbose_name_plural = 'Estados'
        ordering            = ['initials']


#
#           MODELO ALIEN
#    CAMPOS:
#    CITY  -> TIPO CHAR, MAX 50 CARACTERES, NOT NULL  -> NOME DA CIDADE ONDE OCORREU A APARIÇÃO
#    STATE -> CHAVE ESTRANGEIRA                       -> NOME DO ESTADO ONDE OCORREU A APARIÇÃO
#    DATE  -> TIPO DATA, NOT NULL                     -> DATA DA APARIÇÃO
#
class Alien(models.Model):
    city     = models.CharField('Cidade', max_length=50, blank = False)
    state    = models.ForeignKey(State, verbose_name='Estado', related_name='state_fk', on_delete=models.DO_NOTHING, blank=False)
    date     = models.DateField('Data', blank = False, default = date.today)    # ON_DELETE SETADO COMO DO_NOTHING POIS NENHUM ESTADO
                                                                                # SERÁ DELETADO DO DB EM NENHUM MOMENTO.

    @property
    def state_initial(self):
        return self.state.initials

    @property
    def state_name(self):
        return self.state

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.state.count += 1
            self.state.save()
            super(Alien, self).save(*args, **kwargs)
        pass

    def __str__(self):
        return self.city

    class Meta:
        verbose_name        = 'Ocorrência'
        verbose_name_plural = 'Ocorrências'

#
# SIGNALS CRIADO COM INTUITO DE MANTER O DB CONSISTENTE QUANDO O ADMIN DECIDIR DELETAR UMA INSTANCIA DO MODELO ALIEN
#
def post_delete_alien(instance, **kwargs):
    instance.state.count -= 1
    instance.state.save()

models.signals.post_delete.connect(
    post_delete_alien, sender=Alien, dispatch_uid='post_delete_alien'
)
