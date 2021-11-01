import pandas as pd
from IPython.display import display


TabEstBR2021 = pd.DataFrame(
    {
        "Id_Partida": [2408],
        "Rodada_Atual": ["34ª Rodada"],
        "Placar": ["Santos 0x2 América-MG"],
        "Time_Mandante": ["Santos"],
        "Time_Visitante": ["América-MG"],
        "Placar_Mandante": [0],
        "Placar_Visitante": [2],
        "Data_Realizacao": ["23/10/2021"],
        "Hora_Realizacao": ["17:00"],
        "Estadio": ["Vila Belmiro"],
        "Rodada": ["28ª Rodada"],
        "Posse_de_bola_mandante": ["49%"], 
        "Finalizacao_mandante": [14],
        "Dribes_mandante": [11],
        "Posse_de_bola_visitante": ["50%"],
        "Finalizacao_visitante": [16],
        "Dribes_visitante": [10],
    }
)

if __name__ == "__main__":
    TabEstBR2021.to_excel("TabEstBR2021.xlsx", sheet_name="tabestbr2021", index=False)
    print(TabEstBR2021.head())