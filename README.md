# Funnel de suscripción y experimentos A/B en una app freemium

> 🚧 Proyecto en construcción. Este README se completará con resultados, gráficos y enlace a la demo.

## Problema de negocio

Una app de bienestar con modelo freemium quiere aumentar la conversión a la suscripción premium.
El equipo de producto propone cambiar el paywall (ofrecer 7 días de prueba gratis) y necesita saber:

1. **¿Dónde se pierden usuarios** en el funnel instalación → registro → onboarding → paywall → suscripción?
2. **¿El nuevo paywall mejora la conversión** de forma estadísticamente fiable, sin aumentar las cancelaciones?
3. **¿Podemos fiarnos de los datos** antes de tomar la decisión?

## Enfoque (previsto)

| Fase | Qué se hace | Herramientas |
|---|---|---|
| Datos | Generación de eventos sintéticos realistas (usuarios, versiones de app, suscripciones) | Python, NumPy, pandas |
| Análisis | Consultas de funnel, conversión por plataforma y retención | SQL, DuckDB |
| Experimento | Test A/B de proporciones y control de cancelaciones | SciPy |
| Calidad | Comprobaciones de calidad: duplicados, fechas imposibles, coherencia del funnel | Python, SQL |
| Demo | App interactiva con funnel, resultado del test y semáforo de calidad | Streamlit, Plotly |

## Datos

Datos **100 % sintéticos**, generados con código y semilla fija (`random_state: 42`), por lo que cualquiera puede reproducirlos.
No contienen información de personas ni de empresas reales.

## Estructura del repositorio

```
├── config/          # Parámetros del proyecto (semilla, fechas, experimento)
├── data/
│   ├── raw/         # Datos generados (no se suben a GitHub)
│   └── processed/   # Base de datos DuckDB (no se sube a GitHub)
├── notebooks/       # Exploración y explicación paso a paso
├── reports/figures/ # Gráficos para el README y el informe
├── src/             # Código Python reutilizable
└── tests/           # Tests automáticos
```

## Cómo reproducirlo

```bash
git clone https://github.com/PaoAlbanData/subscription-funnel-ab-testing.git
cd subscription-funnel-ab-testing
python -m venv .venv
# Windows: .venv\Scripts\activate   |   Mac/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

Los siguientes pasos (generar datos, ejecutar el análisis, lanzar la app) se añadirán en cada fase.

## Autora

**Paola Albán** — Data Analytics · BI · IA aplicada
