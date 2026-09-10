class Professor:
    def __init__(self, nome, idade, disciplina, matricula):
        self.nome = nome
        self.matricula = matricula
        self.idade = idade
        self.disciplina = disciplina

    def mostrar(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Disciplina:", self.disciplina)
        print("Matrícula:", self.matricula)


class Endereco:
    def __init__(self, rua, bairro, cidade, cep):
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade
        self.cep = cep

    def mostrar(self):
        print("Rua:", self.rua)
        print("Bairro:", self.bairro)
        print("Cidade:", self.cidade)
        print("CEP:", self.cep)


class Aluno:
    def __init__(self, nome, idade, matricula, cpf, endereco):
        self.nome = nome
        self.matricula = matricula
        self.idade = idade
        self.cpf = cpf
        self.endereco = endereco

    def mostrar(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("CPF:", self.cpf)
        print("Matrícula:", self.matricula)


class SalaDeAula:
    def __init__(self, numero):
        self.numero = numero

    def mostrar(self):
        print("Sala:", self.numero)


class Escola:
    def __init__(self, nome, cnpj, telefone, endereco):
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone
        self.endereco = endereco
        self.professores = []
        self.alunos = []
        self.salas = [
            SalaDeAula(1),
            SalaDeAula(2),
            SalaDeAula(3)
        ]

    def adicionar_professor(self, professor):
        self.professores.append(professor)

    def cadastrar_aluno(self, aluno):
        self.alunos.append(aluno)

    def exibir_informacoes(self):
        print("Nome:", self.nome)
        print("CNPJ:", self.cnpj)
        print("Telefone:", self.telefone)
        print("Endereço:", self.endereco)