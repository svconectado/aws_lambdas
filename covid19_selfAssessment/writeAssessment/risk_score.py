def risk_level(score):
    if score < 3:
        return 0
    if score < 6:
        return 1
    if score < 12:
        return 2
    if score >= 12:
        return 3

def calculate_score(event):
    total_score = 0
    
    symptom_weights = {
        "tos": 1,
        "escalofrio": 1,
        "diarrea": 1,
        "malestar": 1,
        "dolor_cabeza": 1,
        "fiebre": 1,
        "perdida_olfato": 1,
        "dificultad_respirar": 2,
        "fatiga": 2,
        "has_viajado": 3,
        "has_viajado_covid": 3,
        "contacto_covid": 3
    }
    
    for symptom in symptom_weights:
        if symptom in event and event[symptom] == True:
            total_score += symptom_weights[symptom]
    
    return total_score
