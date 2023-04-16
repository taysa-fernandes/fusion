import uuid 
from django.test import TestCase
from model_mommy import mommy
from core.models import Features 

from core.models import get_file_path

class GetFilePathTestCase(TestCase):
    def setUp(self):
        self.filename = f'{uuid.uuid4()}.png'
        return super().setUp()
    def test_get_file_path(self):
        arquivo = get_file_path(None, 'Teste.png')
        self.assertTrue(len(arquivo), len(self.filename))
class ServicoTestCase(TestCase):
    def setUp(self):
        self.servico = mommy.make('servico')
    def test_str(self):
        self.assertEquals(str(self.servico),self.servico.servico)
class CargoTestCase(TestCase):
    def setUp(self):
        self.cargo = mommy.make('cargo')
    def test_str(self):
        self.assertEquals(str(self.cargo),self.cargo.cargo)
class FuncionarioTestCase(TestCase):
    def setUp(self):
        self.funcionario = mommy.make('funcionario')
    def test_str(self):
        self.assertEquals(str(self.funcionario),self.funcionario.nome)

class FeaturesTestCase(TestCase):
    def setUp(self):
        self.features = mommy.make(Features, nome='Nome de Teste')
    def test_str(self):
        self.assertEqual(str(self.features), 'Nome de Teste')
    