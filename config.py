# config.py

# Configuration of Brazilian Political Parties and Ideologies

political_parties = {
    "PT": {
        "full_name": "Partido dos Trabalhadores",
        "ideology": "Socialism, Progressivism",
        "year_founded": 1980,
        "notable_figures": ["Lula da Silva", "Dilma Rousseff"]
    },
    "PSDB": {
        "full_name": "Partido da Social Democracia Brasileira",
        "ideology": "Social Democracy, Liberalism",
        "year_founded": 1988,
        "notable_figures": ["Fernando Henrique Cardoso", "Aécio Neves"]
    },
    "PMDB": {
        "full_name": "Partido do Movimento Democrático Brasileiro",
        "ideology": "Centrist",
        "year_founded": 1965,
        "notable_figures": ["Michel Temer", "José Sarney"]
    },
    "PSL": {
        "full_name": "Partido Social Liberal",
        "ideology": "Libertarianism, Right-wing Populism",
        "year_founded": 1994,
        "notable_figures": ["Jair Bolsonaro"]
    },
    "PCdoB": {
        "full_name": "Partido Comunista do Brasil",
        "ideology": "Communism, Left-wing",
        "year_founded": 1922,
        "notable_figures": ["Haroldo Lima", "Luciana Santos"]
    }
    # Add more parties as needed...
}

# Example function to display party information
def display_parties():
    for party, info in political_parties.items():
        print(f"{party}: {info['full_name']} - Ideology: {info['ideology']}")

if __name__ == "__main__":
    display_parties()