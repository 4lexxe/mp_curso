/**
 * demo.js - Manejo interactivo de formularios para demostración
 */

document.addEventListener('DOMContentLoaded', function () {
  const form = document.querySelector('[data-demo-form]');
  const messageBox = document.querySelector('[data-demo-message]');

  if (form && messageBox) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();

      const nombre = document.getElementById('nombre')?.value || 'Estimado/a';
      const especialidad = document.getElementById('especialidad');
      const especialidadTexto = especialidad ? especialidad.options[especialidad.selectedIndex].text : 'la consulta';
      const fecha = document.getElementById('turno-fecha')?.value || 'la fecha solicitada';
      const horario = document.getElementById('horario')?.value || '';

      messageBox.className = 'alert alert-success mt-4 d-block shadow-sm';
      messageBox.innerHTML = `
        <div class="d-flex align-items-center gap-2 mb-2">
          <i class="bi bi-check-circle-fill fs-5 text-success"></i>
          <strong>¡Solicitud de turno registrada con éxito!</strong>
        </div>
        <p class="mb-0">
          Muchas gracias <strong>${nombre}</strong>. Hemos agendado tu turno para <strong>${especialidadTexto}</strong> para el día <strong>${fecha}</strong> a las <strong>${horario} hs</strong>. Te enviamos la confirmación a tu correo electrónico.
        </p>
      `;

      messageBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      form.reset();
    });
  }
});
