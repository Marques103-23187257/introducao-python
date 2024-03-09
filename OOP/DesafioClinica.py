class Funcionario:
    def __init__(self, nome, especialidade):
        self.nome = nome
        self.especialidade = especialidade

    def AgendarConculta(self, paciente, cpf, data, horario, lista):
        consulta = {
            'Paciente': paciente.capitalize(),
            'CPF': cpf,
            'Data': data,
            'Horario': horario,
            'Marcado por': self.nome,
            }
        lista.append(consulta)
        print('Consulta agendada!')

    
    def GerenciarConsulta(self, lista, cpf, novo_horario, nova_data, cancelar=False):

        if len(lista) == 0:
            print('Não há consultas marcadas na lista')

            for consulta in lista:
                if consulta['CPF'] == cpf:
                    if cancelar == True:
                        lista.remove(consulta)
                        print('Consulta Cancelada')
                    else:
                        consulta['Data'] = nova_data
                        consulta['Horario'] = novo_horario
                        

    def ImprimirConsultas(self, lista):
        if len(lista) == 0:
            print('Não há consultas registradas na lista')
        else:
            from datetime import datetime
            print(f"{15*'-'}Consultas{16*'-'}\n\nRelatorio gerado por: {self.nome}\nCargo: {self.especialidade}\nHorario: {datetime.today()}\n{40*'_'}")
            for consulta in lista:
                paciente, cpf, medico, data, horario, responsavel = consulta.values()
                print(f'Paciente: {consulta['Paciente']}\nCPF: {consulta['CPF']}\nData: {consulta['Data']}\nHorario: {consulta['Horario']}\nMarcado por: {consulta['Marcado por']}\n Modificado por: \n{40*"_"}')
        
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


# Testes
        
lista_consultas_1 = []
lista_consultas_2 = []

    
funcionario_1 = Funcionario(nome='Antony', especialidade='Recepcionista')
funcionario_1.AgendarConculta(paciente='enzo', cpf='01', data='22/04/2024', horario='09:00', lista=lista_consultas_1)

medico_1 = Medico(nome='Dr. Gabriel', especialidade='Medico Psiquiatra', crm='xxxxxxxxxxx')

funcionario_1.ImprimirConsultas(lista_consultas_1)

# funcionario_2 = Funcionario(nome='Gleisy', especialidade='auxiliar')