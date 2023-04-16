from django.test import TestCase

from core.forms import ContatoForm

class ContatoFormTestCase(TestCase):
    def setUp(self):
        self.nome = 'Felicity jones'
        self.email = 'felicity@gmail.com'
        self.assunto = 'qualquer assunto'
        self.mensagem = 'qualquer mensagem'
        
        self.dados = {
            'nome': self.nome,
            'email': self.email,
            'assunto': self.email,
            'mensagem': self.mensagem
        }
        
        self.form = ContatoForm(data=self.dados)
    def test_send_mail(self):
        form1 = ContatoForm(data=self.dados)
        form1.is_valid()
        res1 = form1.send_mail()
        
        form2 = self.form
        form2.is_valid()
        res2 = form2.send_mail()
        self.assertEquals(res1,res2)