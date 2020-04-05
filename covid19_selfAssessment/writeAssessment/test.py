import unittest
import json
from risk_score import *

class RiskScoreTest(unittest.TestCase):
    
    def test_risk_level(self):
        self.assertEqual(risk_level(0),0)
        self.assertEqual(risk_level(2),0)
        self.assertEqual(risk_level(3),1)
        self.assertEqual(risk_level(5),1)
        self.assertEqual(risk_level(6),2)
        self.assertEqual(risk_level(11),2)
        self.assertEqual(risk_level(12),3)
        self.assertEqual(risk_level(13),3)
    
    def test_risk_eval(self):
        # Just 1 point
        assessment = {
            "tos": False,
            "escalofrio": False,
            "diarrea": False,
            "malestar": False,
            "dolor_cabeza": False,
            "fiebre": False,
            "perdida_olfato": True,
            "dificultad_respirar": False,
            "fatiga": False,
            "has_viajado": False,
            "has_viajado_covid": False,
            "contacto_covid": False
        }
        self.assertEqual(calculate_score(assessment),1)
        
        # 3 points
        assessment = {
            "tos": True,
            "escalofrio": False,
            "diarrea": False,
            "malestar": True,
            "dolor_cabeza": False,
            "fiebre": False,
            "perdida_olfato": True,
            "dificultad_respirar": False,
            "fatiga": False,
            "has_viajado": False,
            "has_viajado_covid": False,
            "contacto_covid": False
        }
        self.assertEqual(calculate_score(assessment),3)
        
        # 3 points
        assessment = {
            "tos": True,
            "escalofrio": False,
            "diarrea": False,
            "malestar": False,
            "dolor_cabeza": False,
            "fiebre": False,
            "perdida_olfato": False,
            "dificultad_respirar": False,
            "fatiga": True,
            "has_viajado": False,
            "has_viajado_covid": False,
            "contacto_covid": False
        }
        self.assertEqual(calculate_score(assessment),3)
        
        # 3 points
        assessment = {
            "tos": False,
            "escalofrio": False,
            "diarrea": False,
            "malestar": False,
            "dolor_cabeza": False,
            "fiebre": False,
            "perdida_olfato": False,
            "dificultad_respirar": False,
            "fatiga": False,
            "has_viajado": True,
            "has_viajado_covid": False,
            "contacto_covid": False
        }
        self.assertEqual(calculate_score(assessment),3)
        
        # 6 points
        assessment = {
            "tos": True,
            "escalofrio": True,
            "diarrea": True,
            "malestar": True,
            "dolor_cabeza": True,
            "fiebre": True,
            "perdida_olfato": False,
            "dificultad_respirar": False,
            "fatiga": False,
            "has_viajado": False,
            "has_viajado_covid": False,
            "contacto_covid": False
        }
        self.assertEqual(calculate_score(assessment),6)
        
        # 6 points
        assessment = {
            "tos": True,
            "escalofrio": True,
            "diarrea": True,
            "malestar": True,
            "dolor_cabeza": False,
            "fiebre": False,
            "perdida_olfato": False,
            "dificultad_respirar": True,
            "fatiga": False,
            "has_viajado": False,
            "has_viajado_covid": False,
            "contacto_covid": False
        }
        self.assertEqual(calculate_score(assessment),6)
        
        # 6 points
        assessment = {
            "tos": True,
            "escalofrio": False,
            "diarrea": False,
            "malestar": False,
            "dolor_cabeza": False,
            "fiebre": False,
            "perdida_olfato": False,
            "dificultad_respirar": True,
            "fatiga": False,
            "has_viajado": False,
            "has_viajado_covid": True,
            "contacto_covid": False
        }
        self.assertEqual(calculate_score(assessment),6)
        
        # 12 points
        assessment = {
            "tos": True,
            "escalofrio": True,
            "diarrea": True,
            "malestar": True,
            "dolor_cabeza": True,
            "fiebre": True,
            "perdida_olfato": False,
            "dificultad_respirar": False,
            "fatiga": False,
            "has_viajado": False,
            "has_viajado_covid": True,
            "contacto_covid": True
        }
        self.assertEqual(calculate_score(assessment),12)

if __name__ == "__main__":
    unittest.main()
