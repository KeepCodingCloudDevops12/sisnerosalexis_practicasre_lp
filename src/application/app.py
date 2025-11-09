# src/app.py

# --- IMPORTACIONES ---
# Asegúrate de tener uvicorn aquí si no estaba
import uvicorn
from fastapi import FastAPI
from prometheus_client import start_http_server, Counter

# --- INICIALIZACIÓN DE LA APP ---
app = FastAPI()

# --- DEFINICIÓN DE MÉTRICAS ---
SERVER_REQUESTS_TOTAL = Counter('server_requests_total', 'Total number of requests to this webserver')
HEALTHCHECK_REQUESTS_TOTAL = Counter('healthcheck_requests_total', 'Total number of requests to healthcheck')
MAIN_REQUESTS_TOTAL = Counter('main_requests_total', 'Total number of requests to main endpoint')
# Métrica para el nuevo endpoint
BYE_REQUESTS_TOTAL = Counter('bye_requests_total', 'Total number of requests to bye endpoint')

# --- DEFINICIÓN DE ENDPOINTS ---
@app.get("/")
def read_root():
    SERVER_REQUESTS_TOTAL.inc()
    MAIN_REQUESTS_TOTAL.inc()
    return {"message": "Hello World"}

@app.get("/health")
def health_check():
    SERVER_REQUESTS_TOTAL.inc()
    HEALTHCHECK_REQUESTS_TOTAL.inc()
    return {"health": "ok"}

@app.get("/bye")
def bye_endpoint():
    SERVER_REQUESTS_TOTAL.inc()
    BYE_REQUESTS_TOTAL.inc()
    return {"msg": "Bye Bye"}

# --- BLOQUE DE EJECUCIÓN DEL SERVIDOR (ESTA ES LA PARTE CLAVE) ---
if __name__ == "__main__":
    # Arranca el servidor de métricas de Prometheus en el puerto 8000
    start_http_server(8000)
    # Arranca el servidor de FastAPI (Uvicorn) en el puerto 8081
    uvicorn.run(app, host="0.0.0.0", port=8081)