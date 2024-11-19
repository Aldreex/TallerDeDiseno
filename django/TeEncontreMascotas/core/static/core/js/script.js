/* CAPTURAMOS EL FORMULARIO CUANDO SE PRESIONA EL BOTON*/
document.getElementById("formulario").addEventListener("submit", function (e) {
  return null;
  // DETENER EL FORMULARIO
  e.preventDefault();

  // CAPTURAMOS LOS INPUTS
  const nombre = document.getElementById("txtNombre");
  const edad = document.getElementById("txtEdad");
  const correo = document.getElementById("txtCorreo");
  //const fecha = document.getElementById("txtFecha");
  //const genero = document.getElementById("cboGenero");

  // BANDERA O AUXILIAR
  let aux = true;

  //VALIDAMOS QUE SOLO SE INGRESEN LETRAS
  if (!/^[a-zA-Z\s]+$/.test(nombre.value)) {
    nombre.classList.add("is-invalid");
    aux = false;
  } else {
    nombre.classList.remove("is-invalid");
  }
  // VALIDAMOS QUE SOLO SE INGRESEN NUMEROS
  if (!/^\d+$/.test(edad.value)) {
    edad.classList.add("is-invalid");
    aux = false;
  } else {
    edad.classList.remove("is-invalid");
  }
  // VALIDAMOS QUE SOLO SE INGRESEN CORREOS @INACAPMAIL.CL
   // if (!/^[a-zA-Z0-9._%+-\s]$/.test(correo.value)) {
    // correo.classList.add("is-invalid");
    // aux = false;
 //  } else {
  //   correo.classList.remove("is-invalid");
  // }
  // SI LA VARIABLE AUX ES TRUE ES POR QUE ESTA TODO OK.
  if (aux) {
    // GUARDAR

    const persona = {
      nombre: nombre.value,
      edad: edad.value,
      correo: correo.value,
    //  fecha: fecha.value,
      
    };

    // CREAR UNA BD Y SI NO EXISTE SE CREA UN ARREGLO VACIO
    let basededatos = JSON.parse(localStorage.getItem("registros")) || [];
    // GUARDAMOS LA DATA
    basededatos.push(persona);
    // ACTUALIZAMOS EL LOCALSTORAGE
    localStorage.setItem("registros", JSON.stringify(basededatos));

    // ENVIA FORMULARIOS
    Swal.fire({
      title: "Guardado!",
      text: "Formulario ingresado correctamente!",
      icon: "success",
    });
    // LIMPIA EL FORMULARIO
    nombre.value = '';
    edad.value = '';
    correo.value = '';
    fecha.value = '';
  } else {
    // MUESTRA MENSAJE DE ERROR
    Swal.fire({
      title: "Error en Formulario",
      text: "Por favor corrige el formulario!",
      icon: "error",
    });
  }
});

function confirmarFormulario() {
  Swal.fire({
    title: "Guardado!",
    text: "Formulario ingresado correctamente!",
    icon: "success",
  });

}