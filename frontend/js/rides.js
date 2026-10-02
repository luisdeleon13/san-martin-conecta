const API_BASE_URL = "http://127.0.0.1:8000";

const form = document.getElementById("ride-form");
const resultado = document.getElementById("resultado");
const tarifaEl = document.getElementById("tarifa");
const whatsappBtn = document.getElementById("whatsapp-btn");
const errorEl = document.getElementById("error");

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  errorEl.classList.add("oculto");
  resultado.classList.add("oculto");

  const formData = new FormData(form);
  const payload = {
    nombre: formData.get("nombre"),
    telefono: formData.get("telefono"),
    origen: formData.get("origen"),
    destino: formData.get("destino"),
    pasajeros: Number(formData.get("pasajeros")),
    fecha: formData.get("fecha"),
    hora: formData.get("hora"),
    observaciones: formData.get("observaciones") || null,
  };

  try {
    const response = await fetch(`${API_BASE_URL}/rides`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });

    if (!response.ok) {
      const detalle = await response.json().catch(() => null);
      throw new Error(detalle?.detail || "No se pudo registrar la solicitud.");
    }

    const ride = await response.json();

    tarifaEl.textContent = ride.tarifa_estimada;
    whatsappBtn.href = ride.whatsapp_link;
    resultado.classList.remove("oculto");
    form.reset();
  } catch (err) {
    errorEl.textContent = err.message || "Ocurrió un error. Intenta de nuevo.";
    errorEl.classList.remove("oculto");
  }
});
