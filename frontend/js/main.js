// Este archivo se irá ampliando en cada fase.
// Por ahora, solo confirma en la consola que el backend está vivo,
// para verificar que frontend y backend pueden hablar entre sí.

const API_BASE_URL = "http://127.0.0.1:8000";

fetch(`${API_BASE_URL}/health`)
  .then((res) => res.json())
  .then((data) => {
    console.log("Backend respondió:", data);
  })
  .catch((err) => {
    console.warn(
      "No se pudo contactar al backend. ¿Está corriendo 'uvicorn app.main:app --reload'?",
      err
    );
  });
