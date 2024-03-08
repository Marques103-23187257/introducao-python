class Funcionario:
    def __init__(self, nome, especialidade):
        self.nome = nome
        self.especialidade = especialidade

    def AgendarConculta(self, paciente, cpf, medico, data, horario, lista):
        consulta = {
            'Paciente': paciente.capitalize(),
            'CPF': cpf,
            'Medico': medico.capitalize(),
            'Data': data,
            'Horario': horario,
            'Marcado por': self.nome,
            }
        lista.append(consulta)
        print('Consulta agendada!')

    
    def GerenciarConsulta(self, lista, cpf, novo_horario, nova_data, cancelar=False):

        
        if len(lista) == 0:
            print('Não há consultas marcadas na lista')
        
        else:
            for consulta in lista:
                if consulta['CPF'] == cpf:
                    if cancelar == True:
                        lista.remove(consulta)
                        print('Consulta Cancelada')

    def ImprimirConsultas(self, lista):
        from datetime import datetime
        print(f"{10*'-'}Consultas{11*'-'}\n\nRelatorio gerado por: {self.nome}\nHorario: {datetime.today()}\n{30*'_'}")
        
        for consulta in lista:
            paciente, cpf, medico, data, horario, responsavel = consulta.values()
            print(f'''
Paciente: {paciente}
CPF: {cpf}
Medico: {medico}
Data: {data}
Horario: {horario}
Marcado por: {responsavel}
{30*'_'}
''')
        
    def FazerExame(self, exame):
        print(f'Realizando exame: {exame}')
    
class Medico(Funcionario):
    def __init__(self, nome, especialidade, crm):
        super().__init__(nome, especialidade)
        self.crm = crm
    
    def PrescMedicamento(self, medicamento):
        print(f'Prescrição medica: {medicamento}')

class Enfermeira(Funcionario):
    def __init__(self, nome, especialidade, coren):
        super().__init__(nome, especialidade)
        self.coren = coren

    def AplicaInjecao(self, medicamento):
        print(f'Aplicando injeção: {medicamento}')

        
lista_consultas = []

medico_1 = Medico(nome='Gabriel', especialidade='Medico Psiquiatra', crm='xxxxxxxxxxx')
    
funcionario_1 = Funcionario(nome='Antony', especialidade='Recepcionista')
funcionario_1.AgendarConculta(paciente='enzo', cpf='01', medico=medico_1.nome, data='22/04/2024', horario='09:00', lista=lista_consultas)

funcionario_1.ImprimirConsultas(lista_consultas)

# funcionario_2 = Funcionario(nome='Gleisy', especialidade='auxiliar')