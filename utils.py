import pandas as pd
from datetime import datetime
from datetime import timedelta
import os

class DiasUteis:
    def __init__(self):
        # Carregar as datas não úteis a partir do arquivo DNU.txt que está na mesma pasta
        filepath = os.path.join(os.path.dirname(__file__), 'DNU.txt')
        with open(filepath, 'r') as file:
            self.dias_nao_uteis = [line.strip() for line in file.readlines()]
        
        # Converter a lista de strings para uma lista de objetos datetime
        self.dnu = pd.to_datetime(self.dias_nao_uteis, format='%d/%m/%Y')
    
    def is_dia_util(self, date):
        """Verifica se a data fornecida é um dia útil."""
        date = pd.to_datetime(date)
        return not (date in self.dnu.values or date.weekday() >= 5)  # Fins de semana e DNU
    
    def get_dia_util(self, date, days_offset=0):
        """Calcula o próximo dia útil a partir de uma data, com a opção de offset."""
        date = pd.to_datetime(date)
        while days_offset != 0 or not self.is_dia_util(date):
            date += timedelta(days=1 if days_offset >= 0 else -1)
            if self.is_dia_util(date):
                days_offset += 1 if days_offset < 0 else -1
        return date

    def hoje(self, days_offset=0):
        """
        Retorna o dia útil de hoje com a opção de deslocamento (positivo ou negativo) em dias úteis.
        Exemplo: du.hoje() retorna o dia útil de hoje.
                 du.hoje(-1) retorna o último dia útil.
                 du.hoje(+2) retorna o dia útil daqui a dois dias úteis.
        """
        dia_util = self.get_dia_util(datetime.now(), days_offset)
        # Converter para string no formato yyyy-mm-dd
        return dia_util.strftime('%Y-%m-%d')
    
    def qntdu(self, data_inicio, data_fim):
        """
        Retorna a quantidade de dias úteis entre duas datas.
        Aceita as datas no formato 'YYYY-MM-DD' ou como variáveis datetime.
        
        Exemplo: du.qntdu('2024-01-01', '2024-01-10') retorna a quantidade de dias úteis entre as duas datas.
        """
        # Converter strings no formato 'YYYY-MM-DD' para datetime
        data_inicio = pd.to_datetime(data_inicio)
        data_fim = pd.to_datetime(data_fim)
        
        # Verificar se a data de início é maior que a data de fim
        if data_inicio > data_fim:
            raise ValueError("A data de início não pode ser maior que a data de fim.")
        
        # Gerar uma lista de todos os dias entre as duas datas
        dias = pd.date_range(start=data_inicio, end=data_fim)
        
        # Filtrar os dias úteis removendo fins de semana e dias não úteis
        dias_uteis = [dia for dia in dias if self.is_dia_util(dia)]
        
        # Retornar a quantidade de dias úteis
        return len(dias_uteis)
