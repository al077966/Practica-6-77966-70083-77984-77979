materiales_base = {
    "muro": {"ladrillo": 50, "cemento (kg)": 12, "arena (kg)": 25},
    "piso": {"cemento (kg)": 15, "arena (kg)": 25, "grava (kg)": 30},
    "losa": {"cemento (kg)": 20, "arena (kg)": 30, "grava (kg)": 40, "varilla (kg)": 5},
    "cimentación": {"cemento (kg)": 25, "arena (kg)": 40, "grava (kg)": 50, "varilla (kg)": 10},
    "castillo": {"cemento (kg)": 18, "arena (kg)": 28, "grava (kg)": 35, "varilla (kg)": 8},
    "aplanado": {"cemento (kg)": 8, "arena (kg)": 20},
    "techumbre": {"varilla (kg)": 4, "cemento (kg)": 12, "grava (kg)": 22},
    "barda": {"block sólido estructural": 40, "cemento (kg)": 12, "arena (kg)": 25}
}

material_opciones = {
    "cemento (kg)": {
        "CPC 30R (rápido)": {"precio": 3.4, "calidad": 7},
        "CPO 40 (alta resistencia)": {"precio": 3.9, "calidad": 9},
        "Mortero compuesto": {"precio": 2.8, "calidad": 5}
    },
    "ladrillo": {
        "Ladrillo rojo recocido": {"precio": 4.5, "calidad": 7},
        "Block hueco 12×20×40": {"precio": 8.0, "calidad": 6},
        "Block sólido estructural": {"precio": 12.0, "calidad": 9}
    },
    "arena (kg)": {
        "Arena fina lavada": {"precio": 0.35, "calidad": 6},
        "Arena gruesa para concreto": {"precio": 0.40, "calidad": 8}
    },
    "grava (kg)": {
        "Grava 3/8”": {"precio": 0.45, "calidad": 6},
        "Grava 1/2”": {"precio": 0.40, "calidad": 8},
        "Grava 3/4”": {"precio": 0.42, "calidad": 9}
    },
    "varilla (kg)": {
        "Varilla grado 42 (3/8”)": {"precio": 27, "calidad": 7},
        "Varilla grado 42 (1/2”)": {"precio": 33, "calidad": 9}
    },
    "block sólido estructural": {
        "Block sólido estructural premium": {"precio": 14, "calidad": 10}
    }
}
