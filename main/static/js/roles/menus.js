$('#btn_show_agregar').on('click',function () {
    $.ajax({
        url:$('#btn_show_agregar').attr('data-url'),
        type:'GET',
        dataType:'json',
        success:function (data) {
                $('#target_agregar').html(data.html_form);
        }
    });
});

function agregarMenu(id){
    $('#menu').val(id);
    $('#frm_agregar').submit();
}

function eliminar(id) {
    $('#menue').val(id);
}