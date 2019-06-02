$('#crtFrom').on('submit',function () {

    var form=$(this);
    $.ajax({
        url:form.attr('data-url'),
        data:form.serialize(),
        type:'POST',
        dataType:'json',
        success:function (data) {
            if(data.data_state){
                alert('es valido')
            }else{
                alert("es in valido");
                $('#targetCrt').html(data.html_form);
            }
        }
    });
    return false;
});