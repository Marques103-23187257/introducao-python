class Funcionario:
    def __init__(self, nome, especializacao):
        self.nomee = nome
        self.especializacao = especializacao

    def AgendarConculta(self, paciente, data):
        self.paciente = paciente
        self.data = data
        
        print('Consulta agendada')
    
class Medico(Funcionario):
    def __init__(self, nome, especializacao, crm):
        super().__init__(nome, especializacao)
        self.crm = crm
    
consultas = []
    
funcionario_1 = Funcionario(nome='Gabriel', especializacao='Gerente')
# funcionario_1.AgendarConculta(paciente='Fernando', data='XX/XX/XXXX XX:XX')

medico_1 = Medico(nome='Glauber', especializacao='Clinica', crm='xxxxxxxxxxx')

print(medico_1.nomee)



    
