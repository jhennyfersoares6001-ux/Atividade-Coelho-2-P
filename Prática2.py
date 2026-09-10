class Cliente:
    def __init__(self, nome, cpf, cnpj, telefone, documento):
        self.nome = nome
        self.cpf = cpf
        self.cnpj = cnpj
        self.telefone = telefone
        self.documento = documento

    def exibir_informacoes(self):
        print("Nome:", self.nome)
        print("CPF:", self.cpf)
        print("CNPJ:", self.cnpj)
        print("Telefone:", self.telefone)
        print("Endereço:", self.endereco)

class Veiculo:
    def __init__(self, placa, modelo, ano, ValorDiaria):
        self.placa = placa
        self.modelo = modelo
        self.ano = ano
        self.ValorDiaria = ValorDiaria

    def exibir_informacoes(self):
            print("Placa:", self.placa)
            print("Modelo:", self.modelo)
            print("Ano:", self.ano)
            print("Documento:", self.documento)

class Manutencao:
    def __init__(self, descricao, custo, data, veiculo, idManutencao):
        self.descricao = descricao
        self.custo = custo
        self.data = data
        self.veiculo = veiculo
        self.idManutencao = idManutencao
        self.HistoricoManutencao = []

    def registrar_manutencao(self, manutencao):
        self.manutencao.append(manutencao)

    def historico_manutencao(self, manutencao):
        self.manutencao.append(manutencao)

class Condutor:
    def __init__(self, nome, cnh):
        self.nome = nome
        self.cnh = cnh

    def exibir_informacoes(self):
        print("Nome:", self.nome)
        print("CNH:", self.cnh)

class Contrato:
    def __init__(self, idcontrato, nome, telefone, condutor, veiculo, DataInicio, DataFim, status, ValorTotal):
        self.idcontrato = idcontrato
        self.nome = nome
        self.telefone = telefone
        self.condutor = condutor
        self.veiculo = veiculo
        self.DataInicio = DataInicio
        self.DataFim = DataFim
        self.status = "ativo"
        self.ValorTotal = ValorTotal
        self.manutencao = []
        self.contrato = []

    def finalizar(self):
        self.status = "finalizado"

    def cancelar(self):
        self.status = "cancelado"

    def criar_contrato(self, contrato):
        self.contrato.append(contrato)

    def excluir_contrato(self, idcontrato):
        self.idcontrato = idcontrato
        for contrato in self.contrato:
            if contrato.idContrato == idcontrato:
                self.contrato.remove(contrato)
                print("Contrato excluído com sucesso!")
                return

                print("Contrato não encontrado.")

        