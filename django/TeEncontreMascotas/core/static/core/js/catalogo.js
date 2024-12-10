const verDetalle = (id) => {
  const mascota = mascotas.find((m) => m.id === id);
  document.getElementById("detalleImg").src = mascota.img;
  document.getElementById("detalleTitulo").innerText = `${mascota.titulo} - ${mascota.tipo}`;
  document.getElementById("detalleDescripcion").innerText = mascota.descripcion;
  document.getElementById("detalleContacto").innerText = mascota.contacto;
  const detalleModal = new bootstrap.Modal(document.getElementById("detalleModal"));
  detalleModal.show();
};
