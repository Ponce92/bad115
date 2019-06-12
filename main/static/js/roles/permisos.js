$('#btn_show_agregar').on('click',function () {
    console.log($('#btn_show_agregar').attr('data-url'));
    $.ajax({
        url:$('#btn_show_agregar').attr('data-url'),
        type:'GET',
        dataType:'json',
        success:function (data) {
                $('#target_agregar').html(data.html_form);
        }
    });
});

function agregarPermiso(permiso){
    $('#permiso').val(permiso);
    $('#frm_agregar').submit();
}

function eliminar(id) {
    console.log(id);
    $('#permisoe').val(id);
}