# user/views.py
from django.contrib.auth.views import PasswordResetView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from user.forms import CustomPasswordResetForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string 
from django.http import HttpResponseRedirect
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = 'registration/password_reset_form.html'
    success_url = reverse_lazy('password_reset_done')
    email_template_name = 'registration/password_reset_email.html'  # Define o template HTML

    def form_valid(self, form):
        # Armazena o e-mail enviado na sessão para exibir posteriormente na tela de sucesso
        self.request.session['email_sent_to'] = form.cleaned_data['email']

        # Recupera informações da requisição para compor o link no e-mail
        domain = self.request.META['HTTP_HOST']               # Domínio atual (ex: localhost:8000 ou seu domínio real)
        site_name = 'Hopen data'                              # Nome do site que aparecerá no e-mail
        protocol = 'https' if self.request.is_secure() else 'http'  # Detecta se o acesso está sendo feito via HTTPS ou HTTP
        from_email = 'datahopen@gmail.com'                    # Remetente do e-mail
        subject = 'Redefinição de Senha'                      # Assunto do e-mail

        # Para cada usuário encontrado com o e-mail informado
        for user in form.get_users(form.cleaned_data['email']):
            uid = urlsafe_base64_encode(force_bytes(user.pk))                # UID codificado
            token = self.token_generator.make_token(user)                    # Token de redefinição

            # Monta o contexto com os dados necessários para o e-mail
            context = {
                'email': user.email,
                'domain': domain,
                'site_name': site_name,
                'uid': uid,
                'user': user,
                'token': token,
                'protocol': protocol,
            }

            # Renderiza os templates de e-mail em texto puro e HTML
            text_content = render_to_string('registration/password_reset_email.txt', context)
            html_content = render_to_string('registration/password_reset_email.html', context)

            # Cria o e-mail e adiciona a versão HTML como alternativa
            msg = EmailMultiAlternatives(subject, text_content, from_email, [user.email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()  # Envia o e-mail

        # Redireciona para a URL de sucesso (ex: página "E-mail enviado")
        return HttpResponseRedirect(self.success_url)

class CustomPasswordResetDoneView(TemplateView):
    template_name = 'registration/password_reset_done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['email_sent_to'] = self.request.session.get('email_sent_to', '')
        return context
