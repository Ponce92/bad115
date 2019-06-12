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
            }
        }
    });
    return false;
});

$('#btn_show_editar').on('click',function () {
    console.log($('#btn_show_editar').attr('data-url'));
    $.ajax({
        url:$('#btn_show_editar').attr('data-url'),
        type:'GET',
        dataType:'json',
        success:function (data) {
                $('#target_editar').html(data.html_form);
        }
    });
});