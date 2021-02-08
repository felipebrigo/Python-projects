$(function funcao_esconder() {
    $('#minimo').click(function() {
        if ($(this).is(':checked')) $('.minimo').show();
        else                        $('.minimo').hide();
    });
});