/**
 * Created by Francisco Passos on 04/05/2017.
 */
$(document).ready(function () {
    $(".button-collapse").sideNav();
    $("#sidenav-overlay").addClass("reset-overlay");
    $('.tap-target').tapTarget('open');
    $('.modal').modal();
});

$(".carrega").click(function () {
    $('.button-collapse').sideNav('hide');
    $(".chamados").fadeIn(300);
});

$("#vizualizar_chamado").click(function () {
    $('.button-collapse').sideNav('hide');
    $(".chamados").fadeIn(300);
    $(".chamados").load("/chamados?p=teste");
});

function fechar() {
    $('.button-collapse').sideNav('hide');
    $(".chamados").fadeOut(300);
}

//função ocultar modal com teclado
document.onkeyup = function (e) {
    if (e.which == 27) {
        $('.button-collapse').sideNav('hide');
        $(".chamados").fadeOut(300);
    } else if (e.which == 113) {
        $('.button-collapse').sideNav('hide');
        $(".chamados").fadeIn(300);
        $(".chamados").load("/chamados");
        return false;
    } else if (e.which == 9) {
        $('.button-collapse').sideNav('show');
    }
}


$(".ocorrencias-periodo").click(function () {
    $('.button-collapse').sideNav('hide');
    $('#ocorrencias-tempo').modal('open');
});


