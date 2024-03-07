class Funcionario:
    def __init__(self, nome, especialidade):
        self.nome = nome
        self.especialidade = especialidade

    def AgendarConculta(self):
        print('Consulta agendada')
    
    def RemarcarConsulta(self):
        print('Consulta Remarcada')
    
    def FazerExame(self, exame):
        print(f'Realizando exame: {exame}')
    
class Medico(Funcionario):
    def __init__(self, nome, especialidade, crm):
        super().__init__(nome, especialidade)
        self.crm = crm
    
    def PrescMedicamento(self, medicamento):
        print(f'Prescrição medica: {medicamento}' )

class Enfermeira(Funcionario):
    def __init__(self, nome, especialidade, coren):
        super().__init__(nome, especialidade)
        self.coren = coren

    def AplicaInjecao(self, medicamento):
        print(f'Aplicando injeção: {medicamento}')

        


    
    
    
funcionario_1 = Funcionario(nome='Antony', especialidade='Recepcionista')
funcionario_1.AgendarConculta()

funcionario_2 = Funcionario(nome='Gleisy', especialidade='auxiliar')

medico_1 = Medico(nome='Gabriel', especialidade='Medico Psiquiatra', crm='xxxxxxxxxxx')




    
