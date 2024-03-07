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
                if consulta['CPF'] != cpf:
                    continue
                else:
                    if cancelar == True:
                        lista.remove(consulta)
                        print('Consulta Cancelada')
                    else:
                        pass





        
    
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

        
lista_consultas = []

    
funcionario_1 = Funcionario(nome='Antony', especialidade='Recepcionista')
funcionario_1.AgendarConculta()

funcionario_2 = Funcionario(nome='Gleisy', especialidade='auxiliar')

medico_1 = Medico(nome='Gabriel', especialidade='Medico Psiquiatra', crm='xxxxxxxxxxx')





    
