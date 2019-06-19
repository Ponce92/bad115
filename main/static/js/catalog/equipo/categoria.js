$('#btn_show_crear').on('click',function () {
    $.ajax({
        url:$('#btn_show_crear').attr('data-url'),
        type:'GET',
        dataType:'json',
        success:function (data) {
                $('#target_crear').html(data.html_form);
        }
    });
});

$('#btn_crear').on('click',function () {
    var form=$('#crear');
    $.ajax({
        url:form.attr('data-url'),
        data:form.serialize(),
        type:'POST',
        dataType:'json',
        success:function (data) {
            if(data.res){
                $('#crear').submit();
            }else{
                $('#target_crear').html(data.html_form);
                console.log(data.res);
            }
        }
    });
    return false;
});

$('.btn_show_editar').on('click',function () {
    $.ajax({
        url:$(this).attr('data-url'),
        type:'GET',
        dataType:'json',
        success:function (data) {
                $('#target_editar').html(data.html_form);
        }
    });
});

$('#btn_editar').on('click',function () {
    var form=$('#editar');
    $.ajax({
        url:form.attr('data-url'),
        data:form.serialize(),
        type:'GET',
        dataType:'json',
        success:function (data) {
            if(data.res){

                $('#editar').submit();
            }else{
                $('#target_editar').html(data.html_form);
            }
        }
    });
    return false;
});


function eliminar(codigo,nombre) {
    $('#sp_nombre').html(nombre )

}

//======================
