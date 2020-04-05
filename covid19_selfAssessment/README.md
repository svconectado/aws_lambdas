# Auto-Evaluación COVID-19 con AWS Lambdas
Para obtener una evaluación envíe un objeto JSON como cuerpo de una petición POST al siguiente API `https://api.quenecesito.org/testing/assessments`.

El formato del objeto es el siguiente:
```json
{
    "tos": true,
    "escalofrio": true,
    "diarrea": true,
    "malestar": true,
    "dolor_cabeza": true,
    "fiebre": true,
    "perdida_olfato": true,
    "dificultad_respirar": true,
    "fatiga": true,
    "has_viajado": true,
    "has_viajado_covid": true,
    "contacto_covid": true
}
```
Si desea geolocalizar guarde los atributos "lat" y "lon" dentro del objeto JSON. No guarde información sensible dentro de la evaluación.

**Nota**: Puede incluir uno o varios atributos. Atributos adicionales son guardados en el DynamoDB en el backend. El algoritmo de evaluación buscará los índices y realizará el
cálculo del score correspondiente en función de la siguiente tabla:
```python
symtom_weights = {
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
```

El método devolverá una respuesta de la forma:

```json
{
    "statusCode": 200,
    "body": {
        "hash_id": "f21577da40d33d0b3b0e8732f5a04232253896ffc8f5e93f2d676782d2a40e065e99c0d52537c2da26ee4e8eb8fe75f1f5c134c2c6192446f957ab59141e284f",
        "timestamp": "2020-04-05T20:19:10.394944",
        "risk_score": 20,
        "risk_level": 3
    }
}
```

Donde **risk_score** es la sumatoria de puntos de la evaluación enviada y **risk_level** es el nivel de riesgo según
la siguiente tabla:

- 0: Podría ser estrés, toma precauciones y observa.
- 1: Hidrátate, conserva medidas de higiene y reevalua en 2 días.
- 2: Acude a consulta con el médico.
- 3: Llama a 132 para realizar la detección del virus.


## Ejemplo de aplicación con CURL
```bash
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"tos": true,"escalofrio": true,"diarrea": true,"malestar": true,"dolor_cabeza": true,"fiebre": true,"perdida_olfato": true,"dificultad_respirar": true,"fatiga": true,"has_viajado": true,"has_viajado_covid": true,"contacto_covid": true}' \
  https://api.quenecesito.org/testing/assessments
```
