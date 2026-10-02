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
