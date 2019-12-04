from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField
from django.utils.translation import ugettext_lazy as _


class Election(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', unique=True)
    description = models.TextField(blank=True)
    searchable = models.BooleanField(default=True)
    highlighted = models.BooleanField(default=False)
    extra_info_title = models.CharField(max_length=50, blank=True, null=True)
    extra_info_content = models.TextField(max_length=3000, blank=True, null=True)
    uses_preguntales = models.BooleanField(default=False, help_text=_(u"Esta elección debe usar preguntales?"))
    uses_ranking = models.BooleanField(default=False, help_text=_(u"Esta elección debe usar ranking"))
    uses_face_to_face = models.BooleanField(default=True, help_text=_(u"Esta elección debe usar frente a frente"))
    uses_soul_mate = models.BooleanField(default=True, help_text=_(u"Esta elección debe usar 1/2 naranja"))
    uses_questionary = models.BooleanField(default=True, help_text=_(u"Esta elección debe usar cuestionario"))
    candidates_can_commit_everywhere = models.BooleanField(default=True,
                                                           help_text=_(u"Los candidatos en esta elección pueden comprometerse en todas las elecciones"))
    position = models.CharField(default='',
                                null=True,
                                blank=True,
                                max_length=255,
                                help_text=_(u'A qué cargo está postulando?'))

    second_round = models.ForeignKey('self', blank=True, null=True, default=None, on_delete=models.CASCADE)

    ogp_enabled = True

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('election_view', kwargs={'slug': self.slug})

    def get_extra_info_url(self):
            return reverse('election_extra_info', kwargs={'slug': self.slug})

    '''def has_anyone_answered(self):
        return TakenPosition.objects.filter(person__in=self.candidates.all()).exists()

    def card(self, context):
        template_str = get_template('elections/election_card.html')
        context['election'] = self
        if isinstance(context, Context):
            context = context.flatten()
        return template_str.render(context)
    '''

    class Meta:
            verbose_name = _(u'Elección')
            verbose_name_plural = _(u'Elecciones')
