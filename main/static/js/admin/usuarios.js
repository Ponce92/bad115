$('#btn_show_crear').on('click',function () {
    console.log($('#btn_show_crear').attr('data-url'));
    $.ajax({
        url:$('#btn_show_crear').attr('data-url'),
        type:'GET',
        dataType:'json',
        success:function (data) {
                $('#target_crear').html(data.html_form);
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