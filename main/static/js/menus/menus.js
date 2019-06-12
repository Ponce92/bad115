$('#add_menu').on('click',function () {

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
            }
        }
    });
    return false;
});

function eliminar() {
    var resp=confirm("Estas seguro??");
    if(resp){
        return true
    }
    event.preventDefault();
    return false;
}

function actualizar(url) {
    $.ajax({
        url:url,
        type:'GET',
        dataType:'json',
        success:function (data) {
            $('#f_editar').html(data.html_form);
        }
    });
}

$('#edit_menu').on('click',function () {

    var form=$('#editar_form');
    console.log(form.attr('data_url'));
    $.ajax({
        url:form.attr('data-url'),
        data:form.serialize(),
        type:'POST',
        dataType:'json',
        success:function (data) {
            if(data.res){
                $('#editar_form').submit();
            }else{
                $('#f_editar').html(data.html_form);
            }
        }
    });
    return false;
});